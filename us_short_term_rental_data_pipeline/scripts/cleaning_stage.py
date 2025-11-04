#============================================================
# PRJECT METADATA
#------------------------------------------------------------
# Day: 35
# Date: 2025-11-02
# Block 1 - Python Action
# Task: Clean text and numeric fields (price, rating, availability_365)
# Phase: Data Acquisition - Cleaning Stage
# Dataset: InsideAirbnbn (NY, Austin, LA)
# Tools: Python (pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File : scripts/cleaning_stage.py
#============================================================
# Goal:
#   Use etl_config.json as the data source to dynaimically locate city files, clean numeric and text fields (price, rating, availability_365), and output standardized interim CSVs per city.
#
# Pipeline Flow:
#   1. Load config from etl_config.json
#   2. Loop through all cities difined in config
#   3. Clean numeric/text columns
#   4. Save outputs to /data/interim/
#   5. Log cleaning summary to run_log.json
# 
# NOTES:
#   - Maintain consistency with schema_validation.py log format
#   - Outputs: clean_numeric_text_[city]_listings.csv
#============================================================

import os
import pandas as pd
import numpy as np
import json
import time

# load config
with open("etl_config.json","r") as f:
    config = json.load(f)

RAW_DIR = config["data_path"]
INTERIM_DIR = config["output_path"]
LOG_FILE = os.path.join(config["log_path"], "run_log.json")
INDENT = config["log_format"]["indent"]
SORT_KEYS = config["log_format"]["sort_keys"]

output_format = config["output_settings"]["format"]
output_compression = config["output_settings"]["compression"]
 

# BLOCK 1 - CLEAN NUMERIC/TEXT FIELDS

def clean_numeric_fields(df):
    # clean price
    if "price" in df.columns:
        df["price"] = (
            df["price"].astype(str)
            .str.replace(r"[\$,]","", regex=True)
            .replace("", np.nan)
            .astype(float)
        )
    
    # clean review_scores_rating
    if "review_scores_rating" in df.columns:
        df["review_scores_rating"] = (
            df["review_scores_rating"].replace(["NaN", "None", "no rating",""], np.nan).astype(float)
        )

    # clean availability_365
    if "availability_365" in df.columns:
        df["availability_365"] = (
            pd.to_numeric(df["availability_365"],errors="coerce")
            .fillna(0)
            .astype(int)
        )
    return df

# initialize log entries
log_entries = []

# loop through cities defined in config
for city in config["cities"]:
    city_name = city["name"]
    listings_file = [f for f in city["files"] if "listings" in f][0]
    input_path = os.path.join(RAW_DIR, city_name, listings_file)
    output_path = os.path.join(INTERIM_DIR, f"clean_numeric_text_{city_name}.csv")

    if os.path.exists(input_path):
        # read csv (gzip supportred automatically by pandas)
        df = pd.read_csv(input_path, compression="infer")
        cleaned_df = clean_numeric_fields(df)
        cleaned_df.to_csv(output_path, index=False)

        # record log
        log_entries.append({
            "city" : city_name,
            "rows": len(cleaned_df),
            "columns": list(cleaned_df.columns),
            "status": "Cleaned and saved",
            "input_file": input_path,
            "output_file": output_path
        })
    else:
        log_entries.append({
            "city": city_name,
            "status": "File not found",
            "expected_file": input_path
        })

# update run_log.json
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
else:
    logs = {}

logs["cleaning_stage_block1"] = log_entries

with open(LOG_FILE, "w") as f:
    json.dump(logs,f,indent=config["log_format"]["indent"])

print("Cleaned numeric/text fields saved to /data/interim/")

#========================================================
# BLOCK 2 - STANDARDIZE HEADERS AND REMOVE DUPLICATES
#========================================================
# GOAL:
# Ensure all datasets across cities share consistent column naming and remove duplicate rows
# before merging. This maintains schema alignment for # downstream ETL stages.
# 
# PIPELINE FLOW:
# 1. Load interim cleaned files from /data/interim/
# 2. Convert column names to lower_snake_case
# 3. Drop duplicate rows based on full record
# 4. Save standardized outputs to /data/interim/
# 5. Log results to run_log.json
# 
# NOTES:
# - Uses config-driven city list from etl_config.json
# - Outputs: standardized_[city]_listings.csv
#========================================================

# convert to snake_case
def to_snake_case(name):
    return (
        name.strip()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("/", "_")
        .lower()
    )

# standardize headers and drop duplicates
def standardize_and_dedupe(df):
    # convert all column names
    df.columns = [to_snake_case(col) for col in df.columns]
    # drop duplicates
    df = df.drop_duplicates()
    return df

# initizalize log entries
block2_logs = []

for city in config["cities"]:
    city_name = city["name"]
    input_path = os.path.join(INTERIM_DIR, f"clean_numeric_text_{city_name}.csv")
    output_path = os.path.join(INTERIM_DIR, f"standardized_{city_name}_listings.csv")

    if os.path.exists(input_path):
        df = pd.read_csv(input_path)
        std_df = standardize_and_dedupe(df)
        std_df.to_csv(output_path, index = False)

        block2_logs.append({
            "city": city_name,
            "input_file": input_path,
            "output_file": output_path,
            "rows_before": len(df),
            "rows_after": len(std_df),
            "duplicates_removed": len(df) - len(std_df),
            "columns": list(std_df.columns),
            "status": "Standardized and saved"
        })
    else:
        block2_logs.append({
            "city": city_name,
            "status": "File not found",
            "expected_file": input_path
        })

# update run_log.json
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
else:
    logs = {}

logs["cleaning_stage_block2"] = block2_logs

with open(LOG_FILE, "w", encoding=config["log_format"]["encoding"]) as f:
    json.dump(logs, f, indent= config["log_format"]["indent"], sort_keys = config["log_format"]["sort_keys"])

print("Standardized headers and removed duplicates")



#========================================================
# BLOCK 3 - MERGE LISTINGS + CALENDAR
#========================================================
# GOAL:
#   Merge standardized listings and calendar into one unified DataFrame
#   per city. Save results to /data/processed/ as compressed CSVs.
#
# PIPELINE FLOW:
#   1. Read standardized_[city]_listings.csv
#   2. Read calendar.csv.gz
#   3. Merge on listing_id (rename id → listing_id if needed)
#   4. Save merged dataset to /data/processed/
#   5. Log results to run_log.json
#========================================================

PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

block3_logs = []

for city in config["cities"]:
    city_name = city["name"]

    listings_path = os.path.join(INTERIM_DIR, f"standardized_{city_name}_listings.csv")
    calendar_file = [f for f in city["files"] if "calendar" in f][0]
    calendar_path = os.path.join(RAW_DIR, city_name, calendar_file)
    output_path = os.path.join(PROCESSED_DIR, f"clean_merged_{city_name}.csv.gz")
    

    if os.path.exists(listings_path) and os.path.exists(calendar_path):
        
        #track start time
        start_time = time.perf_counter()

        #read data
        listings_df = pd.read_csv(listings_path, low_memory = False)
        
        #normalize listings key
        if "id" in listings_df.columns:
            listings_df.rename(columns={"id": "listing_id"}, inplace = True)

        # determine file size
        calendar_size_mb = os.path.getsize(calendar_path)/(1024*1024)
        print(f"\n {city_name.title()}: Calendar file size = {calendar_size_mb:.1f} MB")

        # chunked merge mode (for large files >50MB)
        if calendar_size_mb >20:
            print(f"{city_name.title()}: Large file detected. using chunked merge...")
            chunk_iter = pd.read_csv(calendar_path, compression="infer", low_memory=False,chunksize=500_000)

            first = True
            row_counter = 0
            for chunk in chunk_iter:
                # normalize join key inside chunk
                if "id" in chunk.columns and "listing_id" not in chunk.columns:
                    chunk.rename(columns={"id": "listing_id"}, inplace=True)
                
                merged_chunk = chunk.merge(listings_df, on="listing_id", how="left", validate="many_to_one")
                row_counter += len(merged_chunk)

                if output_format == "parquet":
                    # Write Parquet in append-like fashion (needs fastparquet or pyarrow backend)
                    merged_chunk.to_parquet(
                        output_path.replace(".csv.gz", ".parquet"),
                        compression=output_compression,
                        index=False,
                        append=not first
                    )
                else:
                    # Default: CSV or CSV.GZ depending on compression
                    merged_chunk.to_csv(
                        output_path,
                        mode="w" if first else "a",
                        index=False,
                        compression=output_compression if output_format == "csv" else "gzip",
                        header=first
                    )
                first = False
            
            #track end time
            end_time = time.perf_counter()
            duration = end_time - start_time
            print(f"⏱️  Chunked merge for {city_name.title()} completed in {duration:.2f} seconds")

            print(f"{city_name.title()}: {row_counter:,} rows saved (streamed merge)")

            block3_logs.append({
                "city" : city_name,
                "rows_calendar": "chunked",
                "rows_lostings" : len(listings_df),
                "rows_merged": row_counter,
                "merge_time_sec": round(duration, 2),
                "status": "Merged and saved (chunked mode)",
                "output_file": output_path
            })

        # normal merge mode ( for smaller datasets )
        else:
            calendar_df = pd.read_csv(calendar_path, compression="infer", low_memory = False)

            print(f"Checking merge keys for {city_name.title()}")
            print("Calendar columns:", list(calendar_df.columns)[:10])
            print("Listings columns:", list(listings_df.columns)[:10])
            print("Calendar rows:", len(calendar_df))
            print("Listings rows:", len(listings_df))

            #normalize calendar key if needed
            if "id" in calendar_df.columns and "listing_id" not in calendar_df.columns:
                calendar_df.rename(columns={"id":"listing_id"}, inplace = True)
            
            #merge safely
            merged_df = pd.merge(
                calendar_df,
                listings_df,
                on="listing_id",
                how="left",
                validate="many_to_one"
            )
            
            #track end time
            end_time = time.perf_counter()
            duration = end_time - start_time
            print(f"⏱️  Merge time for {city_name.title()}: {duration:.2f} seconds")

            #sanity check for abnormal size
            row_ratio = len(merged_df) / max(len(calendar_df),1)
            if row_ratio > 5:
                print(f" {city_name}: Merge produced {row_ratio:.1f}x more rows than calendar")
            
            # save based on config
            if output_format == "parquet":
                merged_df.to_parquet(
                    output_path.replace(".csv.gz", ".parquet"),
                    compression=output_compression,
                    index=False
                )
            elif output_format == "csv":
                merged_df.to_csv(
                    output_path,
                    index=False,
                    compression=output_compression if output_compression else None
                )
            else:
                print(f"Unknown output format '{output_format}', skipping save.")
            
            print(f"{city_name.title()}: {len(merged_df):,} rows saved to {output_path}")

            block3_logs.append({
                "city": city_name,
                "rows_calendar": len(calendar_df),
                "rows_listings": len(listings_df),
                "rows_merged": len(merged_df),
                "ratio_vs_calendar": round(row_ratio, 2),
                "merge_time_sec": round(duration,2),
                "status": "Merged and saved (safe join)",
                "output_file": output_path

            })
    else:
        #missing input handling
        missing = []
        if not os.path.exists(listings_path):
            missing.append(listings_path)
        if not os.path.exists(calendar_path):
            missing.append(calendar_path)
        
        print(f" {city_name}: Missing required file(s): {missing}")
        block3_logs.append({
            "city": city_name,
            "status": "Missing required file(s)",
            "missing": missing
        })

# update run_log.json
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
else:
    logs = {}

logs["cleaning_stage_block3"] = block3_logs

with open(LOG_FILE, "w", encoding=config["log_format"]["encoding"]) as f:
    json.dump(
        logs,
        f,
        indent = config["log_format"]["indent"],
        sort_keys= config["log_format"]["sort_keys"]
    )

print("compressed mereged datasets saved to /data/processed/")