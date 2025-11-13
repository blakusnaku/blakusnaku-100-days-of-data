#==============================================================
# 📦 PROJECT METADATA
#--------------------------------------------------------------
# Day: 45
# Date: 2025-11-12
# Process: run_sql_kpis_by_property_type.py
# Block: 2 - KPI Aggregation by Property Type
# Phase: Data Analysis - SQL Validation
# Dataset: data/str_market.db (table: listings)
# Tool: Python (sqlite3, pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#==============================================================

import os
import json
import sqlite3
import pandas as pd

CONFIG_PATH = 'etl_config.json'

# load config
with open(CONFIG_PATH) as f:
    config = json.load(f)

INTERIM_PATH = config['interim_path']
DB_PATH = config['db_path']
OUTPUT_PREVIEW = os.path.join(INTERIM_PATH, "sql_kpi_by_property_type_preview.csv")

SQL = """
SELECT
    city_display,
    property_type,
    COUNT(*)                    AS total_listings,
    ROUND(AVG(adr), 2)          AS avg_adr,
    ROUND(AVG(revpar),2)        AS avg_revpar,
    ROUND(AVG(occupancy_pct),2) AS avg_occupancy
FROM listings
GROUP BY city_display, property_type
ORDER BY city_display, avg_revpar DESC;
"""

def run_sql_kpis_by_property_type():
    print("=== 🏦 KPI Aggregation by City + Property Type (SQL) ===")

    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found: {DB_PATH}")
        return

    os.makedirs(os.path.dirname(OUTPUT_PREVIEW), exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(SQL, conn)

    print("\n 📊 KPI Summary by Property Type:")
    print(df.head(15).to_string(index=False))

    df.to_csv(OUTPUT_PREVIEW, index=False)
    print(f"\n💾 Preview saved ➡ {OUTPUT_PREVIEW}")
    print("=== ✅ run_sql_kpis_by_property_type.py completed ===\n")

if __name__ == "__main__":
    run_sql_kpis_by_property_type()