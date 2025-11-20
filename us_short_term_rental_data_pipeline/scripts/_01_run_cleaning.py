#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: City-Level Cleaning Pipeline Runner
# Phase: Cleaning Stage — Multi-City ETL
# Dataset: InsideAirbnb — listings/calendar
# Tool: Python (pandas, pyarrow)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: run_city_pipeline.py
#===========================================================
#
# 🎯 GOAL:
# Load raw datasets for each city, apply modular cleaning through
# run_cleaning(), and save processed outputs in Parquet format.
# 
# 🔁 PIPELINE FLOW:
# 1. Load global etl_config.json
# 2. Loop through configured cities
# 3. Load raw listings/calendar CSVs
# 4. Apply run_cleaning() per dataset
# 5. Save cleaned Parquet to processed_path
# 6. (Optional) Log run details to run_log.json
#
# 📘 NOTES:
# - This script is the orchestrator of the Cleaning Stage.
# - Cleaning logic lives in /cleaners and cleaning_stage.py.
# - No hardcoded schema — all driven by etl_config.json.
#===========================================================

import json
import pandas as pd
from modules.cleaning_stage import run_cleaning
import sys,os

def run_city_cleaning(config_path="etl_config.json"):
    """Main entrypoint to process all cities defined in config."""
    
    # 1. Load config
    with open(config_path, "r") as f:
        config = json.load(f)

    data_path = config["data_path"]
    processed_path = config["processed_path"]
    output_compression = config["output_settings"]["compression"]

    print("\n🧹 Starting STR Cleaning Pipeline...\n")

    # 2. Loop through cities
    for city in config["cities"]:
        city_name = city["name"]

        print(f"==============================================")
        print(f"   PROCESSING CITY → {city_name.upper()}")
        print(f"==============================================\n")

        city_folder = os.path.join(data_path, city_name)

        # 3. Load raw datasets
        listings_path = os.path.join(city_folder, "listings.csv.gz")
        calendar_path = os.path.join(city_folder, "calendar.csv.gz")

        print(f"📥 Loading listings → {listings_path}")
        listings_raw = pd.read_csv(listings_path, compression="gzip")

        print(f"📥 Loading calendar → {calendar_path}")
        calendar_raw = pd.read_csv(calendar_path, compression="gzip")

        # 4. Clean using modular cleaning architecture
        print("🧼 Cleaning listings...")
        listings_clean = run_cleaning(listings_raw, config, dataset_key="listings")

        print("🧼 Cleaning calendar...")
        calendar_clean = run_cleaning(calendar_raw, config, dataset_key="calendar")

        # 5. Save processed output to Parquet
        listings_out = os.path.join(processed_path, f"{city_name}_listings.parquet")
        calendar_out = os.path.join(processed_path, f"{city_name}_calendar.parquet")

        print(f"💾 Saving cleaned listings → {listings_out}")
        listings_clean.to_parquet(listings_out, compression=output_compression)

        print(f"💾 Saving cleaned calendar → {calendar_out}")
        calendar_clean.to_parquet(calendar_out, compression=output_compression)

        print(f"✔ Completed cleaning for {city_name}\n")

    print("\n🎉 ALL CITIES PROCESSED SUCCESSFULLY!\n")


# Allow script to run directly
if __name__ == "__main__":
    run_city_cleaning()
