#====================================================================
# 📦 PROJECT METADATA
#--------------------------------------------------------------------
# Day: 39
# Date: 2025-11-06
# Process: verify_sql_import.py
# Block : 3 - Verify imported row counts and integrity
# Phase: Data Acquisition - Database Stage
# Dataset: STR (InsideAirbnb)
# Tool: Python (sqlite3, pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/verify_sql_import.py
#====================================================================

import os
import json
import sqlite3
import pandas as pd

# load config
CONFIG_PATH = "etl_config.json"

with open(CONFIG_PATH,"r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
DB_PATH = os.path.join("data","str_market.db")
LOG_FILE = os.path.join(config["log_path"],"run_log.json")

INDENT = config["log_format"]["indent"]
SORT_KEYS = config["log_format"]["sort_keys"]

# connect to database

def connect_db():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"❌ Database not found: {DB_PATH}")
    return sqlite3.connect(DB_PATH)

#log helper
def append_log(stage,entry):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE,"r",encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = {}
    logs.setdefault(stage, []).append(entry)
    with open(LOG_FILE,"w",encoding="utf-8") as f:
        json.dump(logs,f,indent=INDENT, sort_keys=SORT_KEYS)

# verify row counts
def verify_counts(conn):
    print("=== 🧮 Verify Imported Row Coutns ===\n")

    city_results = []
    for city in config["cities"]:
        city_key = city["name"]

        #expected (from source)
        listings_path = os.path.join(INTERIM_DIR,f"harmonized_{city_key}_listings.csv")
        calendar_path = os.path.join(INTERIM_DIR,f"clean_merged_{city_key}.parquet")

        expected_listings = pd.read_csv(listings_path).shape[0] if os.path.exists(listings_path) else 0
        expected_calendar = pd.read_parquet(calendar_path).shape[0] if os.path.exists(calendar_path) else 0

        #actual (from sqlite)
        cur = conn.cursor()
        db_listings = cur.execute(
            "SELECT COUNT(*) FROM listings WHERE city_display = ?",
            (city['display_name'],)
        ).fetchone()[0]
        db_calendar = cur.execute(
            "SELECT COUNT(*) FROM calendar WHERE city_display = ?",
            (city['display_name'],)
        ).fetchone()[0]

        print(f"📊 {city['display_name']}")
        print(f"Listings -> DB: {db_listings:,} | File: {expected_listings:,}")
        print(f"Calendar -> DB: {db_calendar:,} | File: {expected_calendar:,}")

        city_results.append({
            "city": city_key,
            "expected_listings": expected_listings,
            "db_listings": db_listings,
            "expected_calendar": expected_calendar,
            "db_calendar": db_calendar,
            "status": "match" if db_listings and db_calendar else "mismatch"
        })
    return city_results

# run main
def run_verify_import():
    conn = connect_db()
    results = verify_counts(conn)
    conn.close()

    append_log("database_verification",results)
    print("✅ Verification results logged to run_log.json")
    print("=== ✅ verify_sql_import.py complete ===")

if __name__ == "__main__":
    run_verify_import()