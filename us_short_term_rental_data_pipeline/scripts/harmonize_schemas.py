#============================================================
# PRJECT METADATA
#------------------------------------------------------------
# Day: 36
# Date: 2025-11-03
# Process: harmonize_schemas.py
# Task: Add city column and align schemas for cross-city merge
# Phase: Data Acquisition
# Dataset: InsideAirbnb — standardized listings
# Tool: Python (pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/harmonize_schemas.py
#===========================================================

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


def run_harmonize():
    print("### Harmonizing shemas and adding city columns ###")

    city_dfs = {}

    #load standardized listings
    for city_cfg in config["cities"]:
        city_key    = city_cfg["name"]         
        display     = city_cfg["display_name"]

        file_path = os.path.join(INTERIM_DIR, f"standardized_{city_key}_listings.csv")
        if not os.path.exists(file_path):
            print(f" Missing file for {display}")
            continue
        
        df = pd.read_csv(file_path)

        #add metadata columns
        df["city_key"] = city_key
        df["city_display"] = display

        city_dfs[city_key] = df
        print(f" {display}: loaded {df.shape[0]:,}rows.")
    
    if not city_dfs:
        print("❌ No city data found. Exiting harmonization.")
        return None
    
    #choose a reference schema (first city)
    ref_city = list(city_dfs.keys())[0]
    ref_cols = list(city_dfs[ref_city].columns)
    print(f"\n Reference schema: {ref_city} ({len(ref_cols)} columns)")

    #align all schemas to match the reference
    for city, df in city_dfs.items():

        #add missing columns
        missing_cols = set(ref_cols) - set(df.columns)
        for col in missing_cols:
            df[col] = pd.NA
        
        #reorder columns
        df = df[ref_cols]
        city_dfs[city] = df

        print(f"✅ {city}: aligned with reference schema ({len(df.columns)} cols)")

        #save harmonized output
        out_path = os.path.join(INTERIM_DIR,f"harmonized_{city}_listings.csv")
        df.to_csv(out_path, index=False)
        print(f"💾 Saved: {out_path}")
    
    print("\n✅ harmonize_schemas.py complete — all listings aligned and city columns added.\n")
    return city_dfs

if __name__ == "__main__":
    run_harmonize()