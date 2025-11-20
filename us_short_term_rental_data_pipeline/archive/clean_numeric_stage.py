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
INTERIM_DIR = config["interim_path"]

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

def run_clean_numeric():
    print("=== 🧹 Cleanning Numeric Values ===")
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
    print("=== ✅ clean_numeric_stage.py complete ===\n")

if __name__ == "__main__":
    run_clean_numeric()