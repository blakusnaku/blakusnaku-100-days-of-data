#========================================================================
# 📦 PROJECT METADATA
#------------------------------------------------------------------------
# Day: 37
# Date: 2025-11-04
# Process: validate_numeric_consistency.py
# Block: 3 - Validate Numeric Consistency
# Phase: Data Acquisition - Validation
# Dataset: validated_mmaster_v2.parquet
# Tools: Python (pandas, numpy, json)
# Author: JP Malit
#========================================================================

import os, json
import pandas as pd
import numpy as np

#load config
with open("etl_config.json","r",encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
INPUT_FILE = os.path.join(INTERIM_DIR, "validated_master_v2.parquet")
OUTPUT_FILE = os.path.join(INTERIM_DIR, "numeric_validation_report.csv")

def run_numeric_validation():
    print("=== 📊 Validating Numeric Consistency ===")

    if not os.path.exists(INPUT_FILE):
        print(f"❌ Validation dataset not found: {INPUT_FILE}"),
        return None

    df = pd.read_parquet(INPUT_FILE)
    total_rows = len(df)

    # compute derived metrics
    df["adr"] = df["price"]
    df["occupancy_pct"] = ((365 - df["availability_365"])/365*100).clip(0,100)

    # basic sanity filters
    anomalies = {
        "price_leq_zero": (df["price"] <=0).sum(),
        "occupancy_gt_100": (df["occupancy_pct"] > 100).sum(),
        "occupancy_lt_0": (df["occupancy_pct"] < 0).sum(),
        "rating_gt_100": (df["review_scores_rating"] > 100).sum(),
        "rating_lt_0": (df["review_scores_rating"] <0).sum()
    }

    print("\n🔍 Anomaly summary:")
    for key, val in anomalies.items():
        if val>0:
            print(f" ⚠ {key}:{val:,} rows")
    if all(v==0 for v in anomalies.values()):
        print("✅ No numeric anomalies detected.")
    
    # aggregated summary by city
    summary = (
        df.groupby("city_display")
        .agg(
            listings=("listing_id","count"),
            avg_price=("adr","mean"),
            median_price=("adr","median"),
            avg_occupancy=("occupancy_pct","mean"),
            avg_rating=("review_scores_rating","mean")
        )
        .reset_index()
        .round(2)
    )

    print("\n📊 City-level summary:")
    print(summary.to_string(index=False))

    #save numeric validation report
    summary.to_csv(OUTPUT_FILE, index=False)
    print(f"\n💾 Saved numeric validation report ➡ {OUTPUT_FILE}")
    print("Numeric metrics validated.\n")
    print("=== ✅ validate_numeric_consistency.py complete. ===\n")

    return summary

if __name__ == "__main__":
    run_numeric_validation()