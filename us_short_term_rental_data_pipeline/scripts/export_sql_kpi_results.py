#=============================================================
# 📦 PROJECT METADATA
#-------------------------------------------------------------
# Day: 45
# Date: 2025-11-12
# Process: export_sql_kpi_results.py
# Block: 3 - Export SQL KPI Results
# Phase: Data Analysis - SQL Output INtegration
# Dataset: data/str_market.db (table: listings)
# Tool: Python (sqlite3, pandas, os)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#=============================================================

import os
import json
import pandas as pd
import sqlite3

CONFIG_PATH = 'etl_config.json'
with open(CONFIG_PATH, 'r') as config_file:
    config = json.load(config_file)

INTERIM_PATH = config['interim_path']
DB_PATH = os.path.join('data', 'str_market.db')
PROCESSED_PATH = config['processed_path']
OUTPUT_CSV = os.path.join(PROCESSED_PATH, "sql_output_kpi.csv")

# SQL Queries

SQL_BY_CITY = """
SELECT 
  city_display,
  COUNT(*) AS listings,
  ROUND(AVG(adr), 2) AS avg_adr,
  ROUND(AVG(revpar), 2) AS avg_revpar,
  ROUND(AVG(occupancy_pct), 2) AS avg_occupancy
FROM listings
GROUP BY city_display
ORDER BY avg_revpar DESC;
"""

SQL_BY_PROPERTY_TYPE = """
SELECT 
  city_display,
  property_type,
  COUNT(*) AS total_listings,
  ROUND(AVG(adr), 2) AS avg_adr,
  ROUND(AVG(revpar), 2) AS avg_revpar,
  ROUND(AVG(occupancy_pct), 2) AS avg_occupancy
FROM listings
GROUP BY city_display, property_type
ORDER BY city_display, avg_revpar DESC;
"""

def run_eport_sql_kpis():
    print("=== 📤 Exporting SQL KPI Outputs to CSV ===")

    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}")
        return
    
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        df_city = pd.read_sql_query(SQL_BY_CITY, conn)
        df_type = pd.read_sql_query(SQL_BY_PROPERTY_TYPE, conn)

    print(f"Loaded {len(df_city)} rows for city-level KPIs.")
    print(f"Loaded {len(df_type)} rows for property-type KPIs.")

    #label summary type for stacking
    df_city['summarty_type'] = 'city_summary'
    df_type['summarty_type'] = 'property_type_summary'

    #combine into one master export
    export_df = pd.concat([df_city, df_type], ignore_index=True)

    export_df.to_csv(OUTPUT_CSV, index=False)

    print(f"💾 Saved SQL KPI summart ➡ {OUTPUT_CSV}")
    print("=== ✅ export_sql_kpi_results.py complete ===\n")

if __name__ == "__main__":
    run_eport_sql_kpis()