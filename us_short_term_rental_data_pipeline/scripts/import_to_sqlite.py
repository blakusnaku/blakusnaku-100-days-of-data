#=========================================
# 📦 PROJECT METADATA
#-----------------------------------------
# Day: 39
# Date: 2025-11-06
# Process: import_to_sqlite.py
# Block: 2 - Import cleaned CSVs into SQLite
# Phase: Data Acquisition - Database Stage
# Dataset: Harmonized listings + merged calendar (InsideAirbnb)
# Tool: Python (pandas, sqlite3, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/import_to_sqlite.py
#==========================================

import os
import json
import sqlite3
import pandas as pd

# load config
CONFIG_PATH = "etl_config.json"

with open(CONFIG_PATH,"r",encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
DB_PATH = os.path.join("data","str_market.db")
LOG_FILE = os.path.join(config["log_path"], "run_log.json")
INDENT = config["log_format"]["indent"]
SORT_KEYS = config["log_format"]["sort_keys"]

PIPELINE_STAGE = config["pipeline_mode"]["stage"]
ROW_LIMIT = config["pipeline_mode"]["row_limit"]

# utility function - log helper
def append_log(stage, entry):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r",encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = {}
    logs.setdefault(stage,[]).append(entry)
    with open(LOG_FILE,"w",encoding="utf-8") as f:
        json.dump(logs,f,indent=INDENT, sort_keys=SORT_KEYS)

# connect to sqlite database
def connect_db():
    os.makedirs("data",exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn

#import function for any CSV source
def import_to_sqlite(df,table_name,conn,source_file):
    try:
        #get existing columns from sqlite table
        cursor = conn.execute(f"PRAGMA table_info({table_name})")
        existing_cols = [row[1] for row in cursor.fetchall()]

        #keep only matching columns
        df = df[[c for c in df.columns if c in existing_cols]]

        df.to_sql(table_name,conn,if_exists="append",index=False)
        print(f"✅ Imported {len(df):,} rows ➡ {table_name} ({os.path.basename(source_file)})")
        return {"status": "success","rows":len(df),"table": table_name,"file":source_file}
    except Exception as e:
        print(f"❌ Failed to import {table_name}({source_file}): {e}")
        return {"status": "error", "table": table_name, "file": source_file, "error": str(e)}

# MAIN FUCNTION
def run_import_to_sqlite():
    print("=== 📋 Importing Cleaned CSVs into SQLite Database ===")

    conn = connect_db()
    total_logs = []

    # wipe existing tables when in testing mode
    if PIPELINE_STAGE == "testing":
        cur = conn.cursor()
        for tbl in ["listings", "calendar"]:
            try:
                cur.execute(f"DELETE FROM {tbl};")
                print(f"🧹 Cleared existing data from '{tbl}' table.")
            except sqlite3.OperationalError:
                # Table may not exist yet (first run)
                pass
        conn.commit()

    #import listings frist (harmonized)
    print("\n📂 Importing harmonized listings...")
    for city_cfg in config["cities"]:
        city_key = city_cfg["name"]
        path = os.path.join(INTERIM_DIR, f"harmonized_{city_key}_listings.csv")

        if os.path.exists(path):
            df = pd.read_csv(path,low_memory=False)
            if PIPELINE_STAGE == "testing":
                df = df.head(ROW_LIMIT)
            log_entry = import_to_sqlite(df,"listings",conn,path)
            total_logs.append(log_entry)
        else:
            print(f"⚠ Missing harmonized file for {city_key}: {path}")
 
    #import merged calendars
    print("\n📅 Importing merged calendards...")
    for city in config["cities"]:
        city_key = city["name"]
        path = os.path.join(INTERIM_DIR, f"clean_merged_{city_key}.parquet")

        if os.path.exists(path):
            df = pd.read_parquet(path)
            if PIPELINE_STAGE == "testing":
                df = df.head(ROW_LIMIT)
            log_entry = import_to_sqlite(df,"calendar",conn,path)
            total_logs.append(log_entry)
        else:
            print(f"⚠ Missing calendar file for {city_key}: {path}")

    conn.commit()
    conn.close()

    append_log("database_import", total_logs)
    print("\n💾 All imports commited and logged to run_log.json")
    print("=== ✅ import_to_sqlite.py complete ===")

if __name__ == "__main__":
    run_import_to_sqlite()