#========================================================================================
# 📦 PROJECT METADATA
#----------------------------------------------------------------------------------------
# Day: 41
# Date: 2025-11-08
# Block: 1 - Data Inspection
# Phase: Data Analysis
# Dataset: str_market_ready_parquet
# Tool: Python(pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/insepect_str_market_data.py
#========================================================================================

import pandas as pd
import os

#load config
CONFIG_PATH = "etl_config.json"

#load dataset
file_path = os.path.join("data","processed","str_market_ready.parquet")

def run_inspect_str_market_data():
    print("=== 🧭 Inspecting BI-Ready STR Dataset ===")

    df = pd.read_parquet(file_path)
    print(f"Loaded dataset: {len(df):,} rows x {len(df.columns)} columns\n")

    #basic structure
    print("📋 Columns:")
    print(list(df.columns))
    print("\n📋 Data types:")
    print(df.dtypes)

    #missing values
    print("\n⚠ Missing Values Summary:")
    print(df.isna().sum().sort_values(ascending=False).head(15))

    #descriptive statistics (numeric only)
    print("\n📊 Summary Statistics:")
    print(df.describe().T.round(2))

    #unique values check (categoricals)
    categorical_cols = [c for c in df.columns if df[c].dtype == "object"]
    print("\n🏷️ Categorical Column Cardinalities:")
    for col in categorical_cols:
        unique_count = df[col].nunique()
        print(f"{col:<25} ➡ {unique_count} unique")

    print("Inspection complete - dataset structure verified.")
    print("===✅ inspect_str_market_data.py complete===")

if __name__ == "__main__":
    run_inspect_str_market_data()