#=============================================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------------------------
# Day: 43
# Date: 2025-11-10
# Process: analyze_revpar_by_property.py
# Block: 2 - Aggregate by property_type for RevPAR analysis
# Phase: Data Analysis
# Dataset: str_market_clean_v2.parquet
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#=============================================================================

import os
import json
import pandas as pd

#load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR  =config['output_path']
CLEAN_FILE  =os.path.join(INTERIM_DIR, "str_market_clean_v2.parquet")

def run_revpar_analysis():
    print("=== 💰 Analyzing RevPAR by Property Type ===")

    if not os.path.exists(CLEAN_FILE):
        print(f"❌ Missing dataset: {CLEAN_FILE}")
        return

    #load dataset
    df = pd.read_parquet(CLEAN_FILE)
    print(f"Loaded dataset: {len(df):,} rows")

    #drop rows missing RevPAR or property_type
    df = df.dropna(subset=["revpar", "property_type"])

    #aggregate KPIs
    prop_summary = (
        df.groupby("property_type")
        .agg(
            listings = ("listing_id", "count"),
            avg_adr = ("adr", "mean"),
            avg_revpar = ("revpar", "mean"),
            avg_occupancy = ("occupancy_pct", "mean"),
        )
        .reset_index()
        .round(2)
        .sort_values(by="avg_revpar", ascending=False)
    )

    print("\n 🏠 Average Revenue by Property Type:")
    print(prop_summary.to_string(index=False))

    #save output
    output_file = os.path.join(INTERIM_DIR, "revpar_by_property_type.csv")
    prop_summary.to_csv(output_file, index=False)
    print(f"\n💾 Saved RevPAR by Property Type ➡ {output_file}")
    print("=== ✅ analyze_revpar_by_property.py complete. ===")

if __name__ == "__main__":
    run_revpar_analysis()