#==================================================================
# 📦 PROJECT METADATA
#------------------------------------------------------------------
# Day: 44
# Date: 2025-11-11
# Process: verify_sql_import_analysis.py
# Block: 3 - Verify imported row coutns and integrity
# Phase: Data Analysis - Database Integration
# Dataset: str_market_ready.parquet
# Tool: Python (sqlite3, pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#==================================================================

import os
import sqlite3
import pandas as pd
import json

#load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

PROCESSED_DIR = "data/processed"
DB_PATH = os.path.join("data", "str_market.db")
PARQUET_FILE = os.path.join(PROCESSED_DIR, "str_market_ready.parquet")

def run_verify_sql_import():
    print(" === 🧮 Verifying Imported SQLite Data ===")

    # connect to db
    if not os.path.exists(DB_PATH):
        print(f"❌ Database file not found: {DB_PATH}")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    #count rows from SQLite
    cur.execute("SELECT COUNT(*) FROM listings;")
    db_count = cur.fetchone()[0]
    print(f"📊 Listings table row count (DB): {db_count:,}")

    #count rows from parquet
    if os.path.exists(PARQUET_FILE):
        parquet_df = pd.read_parquet(PARQUET_FILE)
        parquet_count = len(parquet_df)
        print(f"📂 Listings parquet row count: {parquet_count:,}")
    else:
        print(f"❌ Parquet file not found: {PARQUET_FILE}") 
        return
    
    #compare results
    if parquet_count == db_count:
        print("✅ row counts match. import verified successfully.")
    else:
        print(f"⚠ Mismatch detected! DB={db_count:,} vs Parquet={parquet_count:,}")

    # check column integrity
    db_cols = [r[1] for r in cur.execute("PRAGMA table_info(listings);").fetchall()]
    parquet_cols = list(parquet_df.columns)
    missing_in_db = [c for c in parquet_cols if c.lower() not in db_cols]

    if missing_in_db:
        print(f"⚠ Columns missing in DB schema: {missing_in_db}")
    else:
        print("✅ all columns in parquet exist in DB schema.")
    
    conn.close()
    print(" === ✅ verify_sql_import_analysis.py complete. ===")

if __name__ == "__main__":
    run_verify_sql_import()