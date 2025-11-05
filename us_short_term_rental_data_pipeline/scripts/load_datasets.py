#============================================================
# PRJECT METADATA
#------------------------------------------------------------
# Day: 36
# Date: 2025-11-03
# Process: load_datasets.py
# Task: Load multiple city datasets (NY, Seattle, Portland)
# Phase: Data Acquistion
# Dataset: InsideAirbnb - Multi-city (processed)
# Tools: Python (pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File : scripts/load_datasets.py
#============================================================
# Goal:
#    Load cleaned processed datasets for each city to confirm structure consistency before harmonization.
#
# Pipeline Flow:
#   1. Read city list and settings from etl_config.json
#   2. Load each into pandas
#   3. Print shape and column validation summary
#   4. Confirm readiness for harmonization
# 
# NOTES:
#   -  Each file: data/processed/listings_<city>_clean.parquet
#   - Validation ensures same schema before merge
#============================================================

import os
import json
import pandas as pd

#load config
CONFIG_PATH = "etl_config.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

#directories and settings
RAW_DIR = config["data_path"]
INTERIM_DIR = config["output_path"]
LOG_FILE = os.path.join(config["log_path"], "run_log.json")
INDENT = config["log_format"]["indent"]
SORT_KEYS = config["log_format"]["sort_keys"]

output_format = config["output_settings"]["format"]
output_compression = config["output_settings"]["compression"]

#main function

def run_load():
    print("### Multi-city load validation ###")

    city_dfs = {}

    for city_cfg in config["cities"]:
        city_name = city_cfg["name"]
        display_name = city_cfg["display_name"]
        file_path = os.path.join(INTERIM_DIR,f"standardized_{city_name}_listings.csv")

        if not os.path.exists(file_path):
            print(f" Missing file for {display_name}: {file_path}")
            continue
        
        df = pd.read_csv(file_path)
        city_dfs[city_name] = df

        print(f"\n City: {display_name}")
        print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
        print(f"Columns: {list(df.columns)}")

    #schema consistency check
    print("\n### Schema Consistencty Check ###")
    if not city_dfs:
        print(" No city data loaded.")
        return None
    
    base_cols = set(next(iter(city_dfs.values())).columns)
    for city_name, df in city_dfs.items():
        diff = base_cols.symmetric_difference(set(df.columns))
        if diff:
            print(f"❌ {city_name.title()} schema mismatch: {diff}")
        else:
            print(f"✅ {city_name.title()} schema matches base reference.")
    
    print("\n load_datasets.py complete - all datasets successfully loaded \n")

if __name__ == "__main__":
    run_load()