#======================================================================
# 📦 PROJECT METADATA
#----------------------------------------------------------------------
# Day: 43
# Date: 2025-11-10
# Process: export_city_property_summary.py
# Block: 3 - Export summary CSV (avg_rates_by_city_and_type.csv)
# Phase: Data Analysis
# Dataset: str_market_clean_v2.parquet
# Tool: Python (pandas)
# Autthor: JP Malit
# Repository: blakusnaku-100-days-of-data
#======================================================================

import os
import json
import pandas as pd 

#load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR  =config['output_path']
CLEAN_FILE = os.path.join(INTERIM_DIR, "str_market_clean_v2.parquet")

def run_export_summary():
    print("=== 📊 Exporting KPI Summary by City and Property Type ===")

    if not os.path.exists(CLEAN_FILE):
        print(f"❌ Missing dataset: {CLEAN_FILE}")
        return
    
    #load dataset
    df = pd.read_parquet(CLEAN_FILE)
    print(f"Loaded dataset: {len(df):,} rows")

    #drop nulls for grouping
    df = df.dropna(subset=["city_display", "property_type", "adr", "revpar", "occupancy_pct"])

    #group by city + property type
    summary = (
        df.groupby(["city_display", "property_type"])
        .agg(
            listings = ("listing_id", "count"),
            avg_adr = ("adr", "mean"),
            avg_revpar = ("revpar", "mean"),
            avg_occupancy = ("occupancy_pct", "mean"),
        )
        .reset_index()
        .round(2)
        .sort_values(by=["city_display", "property_type"])
    )

    print("\n🏦 City + Property Type Summary:")
    print(summary.to_string(index=False))

    #export summart csv
    output_file = os.path.join(INTERIM_DIR, "avg_rates_by_city_and_type.csv")
    summary.to_csv(output_file, index=False)
    print(f"\n💾 Saved Summary ➡ {output_file}")
    print("=== ✅ export_city_property_summary.py complete. ===")

if __name__ == "__main__":
    run_export_summary()