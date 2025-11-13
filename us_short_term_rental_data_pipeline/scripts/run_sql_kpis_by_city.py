#=============================================================
# 📦 PROJECT METADATA
#-------------------------------------------------------------
# Day: 45
# Date: 2025-11-12
# Process: run_sql_kpis_by_city.py
# Block - 1 ADR / RevPAR / Occupyancy by City (SQL)
# Phase: Data Analysis - SQL Validation
# Dataset: data/str_market.db (table: listings)
# Tool: Python (sqlite, pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#=============================================================

import os
import sqlite3
import pandas as pd
import json

CONFIG_PATH = 'etl_config.json'

# load config
with open(CONFIG_PATH) as f:
    config = json.load(f)

INTERIM_PATH = config['output_path']
DB_PATH = os.path.join('data', 'str_market.db')
PREVIEW_OUT = os.path.join(INTERIM_PATH, 'sql_kpis_by_city_preview.csv')

SQL = """
SELECT
  city_display,
  ROUND(AVG(adr), 2)            AS avg_adr,
  ROUND(AVG(revpar), 2)         AS avg_revpar,
  ROUND(AVG(occupancy_pct), 2)  AS avg_occupancy
FROM listings
GROUP BY city_display
ORDER BY avg_revpar DESC;
"""

def run_sql_kpis_by_city():
    print("=== 🧮 ADR / RevPAR / Occupancy by City (SQL) ===")
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}")
        return

    os.makedirs(os.path.dirname(PREVIEW_OUT), exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(SQL, conn)

    print("\n📊 City KPI Summary (SQL):")
    print(df.to_string(index=False))
    
    # previe file
    df.to_csv(PREVIEW_OUT, index=False)
    print(f"\n💾 Preview saved ➡ {PREVIEW_OUT}")
    print("=== ✅ run_sql_kpis_by_city.py completed ===\n")

if __name__ == "__main__":
    run_sql_kpis_by_city()

