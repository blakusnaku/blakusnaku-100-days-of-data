#=========================================================
# 📦 PROJECT METADATA
#---------------------------------------------------------
# Day: 42
# Date: 2025-11-09
# Process: analyze_amenity_impact.py
# Block: 2 - Count frequency and compute average ADR per amenity
# Phase: Data analysis - Feature Exploration
# Dataset: str_market_with_amenities_v1.parquet
# Tool: Python (pandas, json, os)
# Author: JP Malit
#=========================================================

import os
import json
import pandas as pd

#load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["interim_path"]
INPUT_FILE = os.path.join(INTERIM_DIR, "str_market_with_amenities_v1.parquet")
OUTPUT_FILE = os.path.join(INTERIM_DIR, "amenity_impact_summary.csv")

def run_analyze_amenity_impact():
    print("=== 📊 Analyzing Amenity Impact on ADR ===\n")

    df = pd.read_parquet(INPUT_FILE)
    amenity_cols = [c for c in df.columns if c.startswith("amenity_")]

    records = []
    for col in amenity_cols:
        listings_with = df[col].sum()
        avg_adr = df.loc[df[col] == True, "adr"].mean()

        records.append({
            "amenity": col.replace("amenity_","").replace("_"," ").title(),
            "listings_with": int(listings_with),
            "avg_adr": round(avg_adr, 2)                           
        })
    
    summary_df = pd.DataFrame(records).sort_values("avg_adr",ascending=False)
    summary_df.to_csv(OUTPUT_FILE, index=False)

    print(summary_df.head(10).to_string(index=False))
    print(f"\n💾 Saved amenity impact summary ➡ {OUTPUT_FILE}")
    print("=== ✅ analyze_amenity_impact.py complete ===\n")

if __name__ == "__main__":
    run_analyze_amenity_impact()