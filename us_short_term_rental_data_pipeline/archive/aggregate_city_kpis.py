#============================================
# 📦 PROJECT METADATA
#--------------------------------------------
# Day: 43
# Date: 2025-11-10
# Process: aggregate_city_kpis.py
# Block: 1 - Group data by city for ADR and Occupancy
# Phase: Data Analysis - KPI Aggregation
# Dataset: str_market_with_amenities_v1.parquet
# Tool: Python (pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#============================================

import os
import json
import pandas as pd

#load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR  =config['interim_path']
OUTPUT_FILE = os.path.join(INTERIM_DIR, "city_kpi_summary.csv")

def run_aggergate_city_kpis():
    print("=== 🏦 Aggregating City-Level KPIS ===")

    #load dataset
    data_path = os.path.join(INTERIM_DIR, "str_market_with_amenities_v1.parquet")
    df = pd.read_parquet(data_path)
    print(f"Loaded dataset: {len(df):,} rows")

    #group by city_display
    city_summary = (
        df.groupby("city_display")
        .agg(
            listings = ("listing_id", "count"),
            avg_adr = ("adr", "mean"),
            avg_revpar = ("revpar", "mean"),
            avg_occupancy = ("occupancy_pct", "mean"),
            avg_rating = ("review_scores_rating", "mean"),
        )
        .reset_index()
        .round(2)
    )

    print("\n🏦 City-Level KPI Summary:")
    print(city_summary.to_string(index=False))

    #save summary to csv
    city_summary.to_csv(OUTPUT_FILE, index=False)
    print(f"\n💾 Saved City KPI Summary ➡ {OUTPUT_FILE}")
    print("=== ✅ aggregate_city_kpis.py complete. ===")

if __name__ == "__main__":
    run_aggergate_city_kpis()