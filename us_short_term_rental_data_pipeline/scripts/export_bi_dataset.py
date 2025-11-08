#=================================================
# 📦 PROJECT METADATA
#-------------------------------------------------
# Day: 40
# Date: 2025-11-07
# Process: export_bi_dataset.py
# Block: 3 - Export final dataset for BI integration
# Phase: Data Acquisition - BI Preparation
# Dataset: validate KPIs + harominzed listings
# Tool: Python (pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#==================================================

import os
import json
import pandas as pd

#load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH,"r",encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

#input files
kpi_path = os.path.join(INTERIM_DIR,"kpi_dataset_v1.parquet")

def run_export_bi_dataset():
    print("\n=== 📦 Exporting BI-Ready Dataset ===")

    #load kpi dataset
    kpi_df = pd.read_parquet(kpi_path)
    print(f"Loaded KPI dataset: {len(kpi_df):,} rows")

    # concatenate all harmonized listings
    listing_dfs = []
    for city in config["cities"]:
        city_key  =city["name"]
        harmonized_path = os.path.join(INTERIM_DIR, f"harmonized_{city_key}_listings.csv")

        if os.path.exists(harmonized_path):
            df = pd.read_csv(harmonized_path, low_memory=False)
            listing_dfs.append(df)
        else:
            print(f"⚠ Missing harmonized file {city_key}")
    
    if listing_dfs:
        listings_df = pd.concat(listing_dfs,ignore_index=True)
        print(f"Combined harmonized listings: {len(listings_df):,} rows")
    else:
        print("❌ No harmonized listings found - aborting export")
        return

    # normalize key column name
    if "id" in listings_df.columns:
        listings_df.rename(columns={"id":"listing_id"}, inplace=True)
    
    # ✅ Normalize key dtype to string
    listings_df["listing_id"] = listings_df["listing_id"].astype(str)
    kpi_df["listing_id"] = kpi_df["listing_id"].astype(str)
    
    # check key overlap
    overlap = len(set(kpi_df["listing_id"]).intersection(set(listings_df["listing_id"])))
    print(f"Key overlap: {overlap:,} / {len(kpi_df):,}")
 
    # merge listings + kpi dataset
    merged_df = pd.merge(
        listings_df,
        kpi_df,
        on="listing_id",
        how="left",
        suffixes=("","_kpi"),
        validate="one_to_one"
    )

    # select columns relevant for BI visualization
    columns_to_keep = [
        "listing_id", "city_display", "price", "adr", "revpar", "occupancy_pct", "los", "review_scores_rating", "property_type",
        "room_type", "accomodates", "beds", "bedrooms", "bathrooms", "latitude", "longtitude"
    ]
    merged_df = merged_df[[c for c in columns_to_keep if c in merged_df.columns]]

    #save outputs (parquet + csv preview)
    parquet_out = os.path.join(PROCESSED_DIR, "str_market_ready.parquet")
    csv_out = os.path.join(PROCESSED_DIR, "str_market_ready.csv")

    merged_df.to_parquet(parquet_out, index=False, compression="snappy")
    merged_df.to_csv(csv_out, index=False)

    print(f"💾 Saved BI dataset ➡ {parquet_out}")
    print(f"📄 CSV preview file ➡ {csv_out}")
    print(f"Columns: {list(merged_df.columns)}")
    print(f"Rows exported: {len(merged_df):,}")
    print("=== ✅ export_bi_dataset.py complete ===\n")

if __name__ == "__main__":
    run_export_bi_dataset()