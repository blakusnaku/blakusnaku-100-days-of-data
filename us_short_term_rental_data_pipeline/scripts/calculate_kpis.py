#========================================================================
# 📦 PROJECT METADA
#------------------------------------------------------------------------
# Day: 38
# Date: 2025-11-05
# Process: calculate_kpis.py
# Task: Compute ADR, RevPAR, Occupancy %, and LOS metrics
# Phase: Data Acquisition - KPI Transformation
# Dataset: validated_master_v2.parquet
# Tool: Python (pandas, json, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/calculate_kpis.py
#========================================================================

import os
import json
import pandas as pd
import numpy as np

from scripts.metrics_utils import (
    compute_adr,compute_occupancy,compute_revpar,compute_los
)

# ⚙ load config
CONFIG_PATH = "etl_config.json"

with open(CONFIG_PATH,"r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"]
LOG_PATH = config["log_path"]
INDENT = config["log_format"]["indent"]
SORT_KEYS = config["log_format"]["sort_keys"]

def run_calculate_kpis():
    print("=== 💡 Calculating STR KPIs ===")

    # load validated dataset
    validated_path = os.path.join(INTERIM_DIR, "validated_master_v2.parquet")
    df = pd.read_parquet(validated_path)

    print(f"Loaded validated dataset: {validated_path}")
    print(f"Rows: {len(df):,} | Columns: {len(df.columns)}")

    #----------------------
    # Compute metrics
    #----------------------

    #ADR - Average Daily Rate
    df["adr"] = compute_adr(df)

    #Occupancy % (already derived, but ensure bounded)
    df["occupancy_pct"] = compute_occupancy(df)

    #RevPar - Revenue Per Available Room
    df["revpar"] = compute_revpar(df)

    # LOS - Length of Stay (proxy using minimum_nights)
    df["los"] = compute_los(df)

    #---------------------
    # Save KPI dataset
    #---------------------
    output_path = os.path.join(INTERIM_DIR,"kpi_dataset_v1.parquet")
    df.to_parquet(output_path, index=False, compression="snappy")

    print(f"✅ KPI dataset saved ➡ {output_path}")
    print(df.sample(5)[["city_display", "adr", "revpar", "occupancy_pct", "los"]])

    #---------------------
    # Log update
    #---------------------
    log_entry = {
        "stage": "calcute_kpis",
        "rows_processed": len(df),
        "columns_added": ["adr","revpar","occupancy_pct","los"],
        "output_file": output_path,
    }

    log_file = os.path.join(LOG_PATH,"run_log.json")
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = {}

    logs["calculate_kpis"] = log_entry

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=INDENT, sort_keys=SORT_KEYS)

    print("📋 Logged KPI calculation results to run_log.json")
    print("=== ✅ calculate_kpis.py complete ===\n\n")

if __name__ == "__main__":
    run_calculate_kpis()