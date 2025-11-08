#============================================================
# 📦 PROJECT METADATA
#------------------------------------------------------------
# Day: 37
# Date: 2025-11-04
# Process: validate_missing_outliers.py
# Block: 2 - Handle Missing and Extreme values
# Phase: Data Acquisition - Validation
# Dataset: listings_master_v1.parquet
# Tool: Python (pandas, numpy, json)
# Author: JP Malit
#============================================================

import os, json
import pandas as pd
import numpy as np

#load config
with open("etl_config.json","r",encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
INPUT_FILE = os.path.join(INTERIM_DIR, "listings_master_v1.parquet")
OUTPUT_FILE = os.path.join(INTERIM_DIR, "validated_master_v2.parquet")

def run_missing_outlier_treatment():
    print("=== 🧹 Handling Missing and Extreme Values ===")

    if not os.path.exists(INPUT_FILE):
        print(f"❌ File not found: {INPUT_FILE}")
        return None

    df = pd.read_parquet(INPUT_FILE)
    initial_shape = df.shape

    # drop completely empty columns
    empty_cols = [c for c in df.columns if df[c].isnull().all()]
    if empty_cols:
        df = df.drop(columns=empty_cols)
        print(f"🗑️ Dropped empty columns: {empty_cols}")
    
    # fill categorical/text missing values
    text_cols = df.select_dtypes(include="object").columns
    df[text_cols] = df[text_cols].fillna("Unknown")

    # treat numeric columns
    num_cols = df.select_dtypes(include=["float64","int64"]).columns
    for col in num_cols:
        if col in ["price","availability_365","review_scores_rating"]:
            series = df[col]

            # replace negatives with Nan
            df.loc[series < 0, col] = np.nan

            # outlier capping for price
            if col == "price":
                q1, q3 = series.quantile([0.25,0.75])
                iqr = q3-q1
                upper,lower = q3 + 1.5 *iqr, q1 - 1.5*iqr
                df[col] = np.clip(series, lower,upper)

            # bound availability logically
            if col == "availability_365":
                df[col] = series.clip(0,365)

            # input missing with median
            median_val = df[col].median(skipna=True)
            df[col] = df[col].fillna(median_val)

    # final sanity check
    print(f"Initial shape: {initial_shape} ➡ Cleaned shape: {df.shape}")

    # save cleaned version
    df.to_parquet(OUTPUT_FILE, compression=config["output_settings"]["compression"], index = False)

    print(f"💾 Saved validated dataset ➡ {OUTPUT_FILE}") 
    print("=== ✅ validate_missing_outliers.py complete. ===\n")

    return df

if __name__ == "__main__":
    run_missing_outlier_treatment()