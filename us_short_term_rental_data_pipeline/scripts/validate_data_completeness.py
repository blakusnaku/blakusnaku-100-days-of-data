#============================================================
# 📦 PROJECT METADATA
#------------------------------------------------------------
# Day: 37
# Date: 2025-11-04
# Process: validation_stage.py
# Block: 1 - Data Completeness and Null Check
# Phase: Data Acquisition - Validation
# Dataset: listings_master_v1.parquet
# Tool: Python (pands, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/validation_stage.py
#============================================================
# 🎯 GOAL:
#   Generate a data quality report for the consolidated 
#   listings_master_v1.parquet file, summarizing completeness
#   and missing value percentages per column.
#
# 🔁 PIPELINE FLOW:
#   1. Load master dataset from /data/interim/
#   2. Compute missing values and % missing
#   3. Identify columns exceeding missing-value thresholds
#   4. Export summary report to /data/interim/data_quality_report.csv
#=============================================================

import os, json
import pandas as pd

#load config
with open("etl_config.json","r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
MASTER_PATH = os.path.join(INTERIM_DIR,"listings_master_v1.parquet")

def run_data_quality_check(threshold: float = 0.2):
    print("=== 🧩 Running Data Quality Report (Nulls and Completeness) ===")

    if not os.path.exists(MASTER_PATH):
        print(f"❌ Master dataset not found: {MASTER_PATH}")
        return None
    
    df = pd.read_parquet(MASTER_PATH)
    total_rows = len(df)

    #compute null counts and percentages
    null_counts = df.isnull().sum()
    percent_missing = (null_counts/total_rows)*100

    #combine into summary dataframe
    quality_df = pd.DataFrame({
        "column": df.columns,
        "dtype": df.dtypes.astype(str),
        "null_count": null_counts.values,
        "percent_missing": percent_missing.values.round(2)
    }).sort_values("percent_missing",ascending=False)

    #flag high missingness
    quality_df["flag_high_missing"] = quality_df["percent_missing"] > (threshold*100)

    #display top 10 columns by missing %
    print("\n📋 Top columns by missing percentage:")
    print(quality_df.head(10).to_string(index=False))

    high_missing = quality_df[quality_df["flag_high_missing"]]
    if not high_missing.empty:
        print(f"\n⚠ Columns exceeding {threshold*100:.0f}% missing threshold:")
        for col in high_missing["column"]:
            print(f"    - {col}")
    else:
        print("\n✅ No columns exceed missing threshold.")

    #save summary to csv
    output_path = os.path.join(INTERIM_DIR, "data_quality_report.csv")
    quality_df.to_csv(output_path, index = False)

    print(f"\n💾 Data quality report saved to {output_path}")
    print("=== ✅ validation_stage.py complete. ===\n")

    return quality_df

if __name__ == "__main__":
    run_data_quality_check()
