#========================================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------------------
# Day: 38
# Date: 2025-11-05
# Process: generate_kpi_summary.py
# Task: Aggregate KPIs per city and expoert to summart CSV
# Phase: Data Acquistion - KPI Transformation
# Dataset: kpi_dataset_v1.parquet
# Tool: Python (pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# Files: script/generate_kpi_summary.py
#========================================================================

import os
import json
import pandas as pd

from scripts.metrics_utils import summarize_city_kpis

# load config
CONFIG_PATH = "etl_config.json"

with open(CONFIG_PATH,"r",encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
LOG_PATH = config["log_path"]
INDENT = config["log_format"]["indent"]
SORT_KEYS = config["log_format"]["sort_keys"]

# define input output paths
INPUT_FILE = os.path.join(INTERIM_DIR,"kpi_dataset_v1.parquet")
OUTPUT_FILE = os.path.join(INTERIM_DIR, "city_kpi_summary.csv")

# main funciton
def run_kpi_summary():
    print("=== 📊 Generating City-Level KPI Summary ===")

    if not os.path.exists(INPUT_FILE):
        print(f"❌ KPI dataset not found :{INPUT_FILE}")
        return None

    df = pd.read_parquet(INPUT_FILE)
    print(f"Loaded KPI dataset: {INPUT_FILE}")
    print(f"Rows: {len(df):,} | Columns: {len(df.columns)}")

    # generate city-level summary
    summary = summarize_city_kpis(df)

    print("\n🏦 City KPI Summary:")
    print(summary.to_string(index=False))

    #save output
    summary.to_csv(OUTPUT_FILE, index=False)
    print(f"\n💾 Saved city KPI summary ➡ {OUTPUT_FILE}")

    #log results
    log_file = os.path.join(LOG_PATH,"run_log.json")
    if os.path.exists(log_file):
        with open(log_file,"r",encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = {}
    
    logs["city_kpi_summary"] = {
        "stage": "generate_kpi_summary",
        "rows_processed": len(df),
        "cities": summary["city_display"].tolist(),
        "output_file": OUTPUT_FILE,
    }

    with open(log_file,"w",encoding="utf-8") as f:
        json.dump(logs,f,indent=INDENT, sort_keys=SORT_KEYS)

    print("📋 Logged city KPI summary results to run_log.json")
    print("=== ✅ generate_kpi_summary.py complete ===")

if __name__ == "__main__":
    run_kpi_summary()