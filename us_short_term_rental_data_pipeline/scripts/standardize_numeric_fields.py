#=========================================================================
# 📦 PROJECT METADATA
#-------------------------------------------------------------------------
# Day: 41
# Date: 2025-11-08
# Block: 2 - standardize numeric fields
# Phase: Data Analysis
# Dataset: str_market_ready.parquet
# Tool: Python (pandas, numpy)
# Author: JP Malit
# Repository: blakusnaku_100-days-of-data
# File scripts/standarize_numeric_fields.py
#=========================================================================

import os,json
import pandas as pd
import numpy as np

#load config
CONFIG_PATH = "etl_config.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]

#load dataset
file_path = os.path.join("data","processed","str_market_ready.parquet")
df = pd.read_parquet(file_path)

def run_standardize_numeric_fields():
    print("=== 💡 Standardizing Numeric Columns ====")
    print(f"Loaded dataset: {len(df):,} rows\n")

    #identify numeric columns
    num_cols = ["price","adr","revpar","review_scores_rating"]
    print("Target numeric columns:", num_cols)

    #clean string artifacts (if any)
    for col in num_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace("[^0-9.\-]","",regex=True)
                .replace("", np.nan)
                .astype(float)
            )
            print(f"✅ Cleaned column: {col}")

    #ensure all are float64
    df[num_cols] = df[num_cols].astype("float64")

    #summary check
    print("\n📊 Numeric column summary:")
    print(df[num_cols].describe().T.round(2))

    #save standardized version
    output_path = os.path.join(INTERIM_DIR,"str_market_clean_v1.parquet")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)

    print(f"\n💾 Saved standardized dataset ➡ {output_path}")
    print("=== ✅ standrdize_numeric_fields.py complete ===")

if __name__ == "__main__":
    run_standardize_numeric_fields()