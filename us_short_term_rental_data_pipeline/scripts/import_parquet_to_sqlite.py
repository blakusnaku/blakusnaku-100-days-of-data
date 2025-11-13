#==================================================================
# 📦 PROJECT METADATA
#------------------------------------------------------------------
# Day: 44
# Date: 2025-11-11
# Process: import_partquet_to_sqlite.py
# Block: 2 - Import cleaned Parquet files into SQLite
# Phase: Data Analysis - Database Integration
# Dataset: str_market_ready.parquet
# Tool: Python (pandas, sqlite3, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#==================================================================

import os
import sqlite3
import pandas as pd
import json

# Load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

PROCESSED_DIR = config['processed_path']
DB_PATH = config['db_path'] 
PARQUET_PATH = os.path.join(PROCESSED_DIR, "str_market_ready.parquet") #input file

def run_import_parquet_to_sqlite():
    print("=== 🧠 Import BI-Ready Parquet into SQLite Database ===")

    if not os.path.exists(PARQUET_PATH):
        print(f"❌ BI-ready Parquet file not found: {PARQUET_PATH}")
        return
    
    #connect to sqlite
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
 
    #load parquet file
    df = pd.read_parquet(PARQUET_PATH)
    print(f"Loaded Parquet dataset: {len(df):,} rows x {len(df.columns):,} columns.")

    #conver column names to match sql schema
    df.columns = [c.lower() for c in df.columns]
    if "longtitude" in df.columns:
        df.rename(columns={"longtitude": "longitude"}, inplace=True)

    # push to sqlite
    df.to_sql("listings", conn, if_exists="replace", index=False)
    conn.commit()

    print(f"💾 Successfully imported {len(df):,} rows into 'listings' table.")
    print(f"📂 Database path: {DB_PATH}")

    conn.close()
    print("=== ✅ import_parquet_to_sqlite.py completed ===")

if __name__ == "__main__":
    run_import_parquet_to_sqlite()