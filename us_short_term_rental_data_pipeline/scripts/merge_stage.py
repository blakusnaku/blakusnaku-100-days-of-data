#===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 36
# Date: 2025-11-03
# Process: merge_stage.py
# Task: Combine harmonized city datasets into master file
# Phase: Data Acquisition
# Dataset: InsideAirbnb — multi-city harmonized listings
# Tool: Python (pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/merge_stage.py
# ===========================================================
# 
# 🎯 GOAL:
#    Merge all harmonized city listings into one consolidated
#    multi-city master dataset for downstream processing.
#
# 🔁 PIPELINE FLOW:
#     1. Read all harmonized_<city>_listing.csv from /data/interim/
#     2. Concatenate vertically into a single DataFrame
#    3. Validate row and column consistency
#    4. Save combined dataset as listings_master_v1.parquet
#===========================================================

import os, json
import pandas as pd

# --- Load configuration ---
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
output_format = config["output_settings"]["format"]
output_compression = config["output_settings"]["compression"]

def run_merge():
    print("=== 🧩 Combining Harmonized Datasets into Master File ===")

    city_dfs = []
    city_rows = {}

    # --- Load harmonized datasets for each city ---
    for city_cfg in config["cities"]:
        city_key = city_cfg["name"]
        display = city_cfg["display_name"]
        file_path = os.path.join(INTERIM_DIR, f"harmonized_{city_key}_listings.csv")

        if not os.path.exists(file_path):
            print(f"⚠️  Missing harmonized file for {display}: {file_path}")
            continue

        df = pd.read_csv(file_path)
        city_dfs.append(df)
        city_rows[display] = len(df)

        print(f"📍 Loaded {display}: {len(df):,} rows")

    if not city_dfs:
        print("❌ No harmonized datasets found. Exiting merge stage.")
        return None

    # --- Concatenate all city dataframes ---
    master_df = pd.concat(city_dfs, ignore_index=True)
    total_rows = len(master_df)
    total_cols = len(master_df.columns)

    print("\n-----------------------------------------")
    for city, rows in city_rows.items():
        print(f"{city}: {rows:,} rows")
    print("-----------------------------------------")
    print(f"Total combined rows: {total_rows:,}")
    print(f"Total columns: {total_cols}")

    # --- Validate key columns exist ---
    for col in ["city_key", "city_display"]:
        if col not in master_df.columns:
            print(f"⚠️  Warning: Missing expected metadata column '{col}'")

    # --- Save master dataset ---
    output_path = os.path.join(INTERIM_DIR, "listings_master_v1.parquet")

    master_df.to_parquet(
        output_path,
        compression=output_compression,
        index=False
    )

    print(f"💾 Saved consolidated dataset to {output_path}")
    print("✅ merge_stage.py complete — multi-city master file ready.\n")

    return master_df

if __name__ == "__main__":
    run_merge()

