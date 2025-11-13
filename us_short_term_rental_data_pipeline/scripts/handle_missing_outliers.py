#=======================================================================================
# 📦 PROJECT METADATA
#---------------------------------------------------------------------------------------
# Day: 41
# Date: 2025-11-08
# Process: handle_missing_outliers.py
# Block: 3 - Handle Missing Values and Detect Outliers
# Phase: Data Analysis - Data Preparation
# Dataset: str_market_clean_v1.parquet
# Tools: Python (pandas, numpy, json)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#=======================================================================================

import os
import json
import numpy as np
import pandas as pd

#load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INETERIM_DIR = config["interim_path"]
INPUT_FILE = os.path.join(INETERIM_DIR, "str_market_clean_v1.parquet")
OUTPUT_FILE = os.path.join(INETERIM_DIR, "str_market_clean_v2.parquet")

def run_handle_missing_outliers():
    print("=== 🧹 Handling Missing Values and Detecting Outliers ===")

    #load cleaned dataset
    df = pd.read_parquet(INPUT_FILE)
    print(f"Loaded dataset: {len(df):,} rows")

    # 1️⃣ handle missing values
    print("🔍Missing Values Summary:")
    miss_summary = df.isna().sum().sort_values(ascending=False)
    print(miss_summary.head(10))

    # strategy:
    # - review_scores_rating: fill with median (neutral)
    # - price / adr / revpar: drop rows where there are missing
    # - bedrooms/ beds / bathrooms: fill with mode (most common)
    # - others: keep as-is

    median_rating = df["review_scores_rating"].median()
    mode_bedrooms = df["bedrooms"].mode()[0]
    mode_beds = df["beds"].mode()[0]
    mode_baths = df["bathrooms"].mode()[0]

    df["review_scores_rating"] = df["review_scores_rating"].fillna(median_rating)
    df["bedrooms"]             = df["bedrooms"].fillna(mode_bedrooms)
    df["beds"]                 = df["beds"].fillna(mode_beds)
    df["bathrooms"]            = df["bathrooms"].fillna(mode_baths)

    df.dropna(subset=["price", "adr", "revpar"], inplace=True)

    print(f"✅ After cleaning missing values, {len(df):,} rows remaining")

    # 2️⃣ outlier detection and treatment
    numeric_cols = ["price", "adr", "revpar", "occupancy_pct", "los"]
    print("📊 Outlier thresholds (1st-99th percentile):")

    for col in numeric_cols:
        low,high = df[col].quantile([0.01, 0.99]).values
        print(f"{col:<15} {low:>8.2f} ➡ {high:>8.2f}")
        df[col] = df[col].clip(lower=low, upper=high)
        
    # 3️⃣ save clean dataset
    df.to_parquet(OUTPUT_FILE, index=False, compression="snappy")

    print(f"💾 Saved cleaned dataset ➡ {OUTPUT_FILE}")
    print(f"Final shape: {df.shape[0]:,} rows x {df.shape[1]} columns")
    print("=== ✅ handle_missing_outliers.py compelte ===\n")

if __name__ == '__main__':
    run_handle_missing_outliers()