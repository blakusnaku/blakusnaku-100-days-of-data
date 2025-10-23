# ===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 28
# Date: 2025-10-26
# Block: 2 — PYTHON ACTION
# Task: Use .dt.year and .dt.month on reservation dates, clean dataset
# Phase: STR Analytics Phase
# Dataset: hotel_bookings.csv (imported to str_reservations table)
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/block2_python_action.py
# ===========================================================
#
# 🎯 GOAL:
# Clean STR dataset and add derived date columns (arrival_date, year, month)
#
# 🔁 PIPELINE FLOW:
# SQLite (str_analytics.db) → pandas DataFrame → cleaned CSV export
#
# 📘 NOTES:
# Apply all data quality fixes from Excel inspection:
# - Replace 'Undefined' meal/market_segment values
# - Fill NULL agent/company
# - Remove or flag negative ADR
# - Combine arrival_date_year + month + day into full arrival_date
# ===========================================================

import pandas as pd
import numpy as np
import sqlite3

# Connect to database
conn = sqlite3.connect(r"data/str_analytics.db")

df = pd.read_sql_query("SELECT * FROM str_reservations", conn)
print(f"✅ Loaded {len(df):,} rows from database")

# Cleaning: handling missing and unidentified values

df['meal'] = df['meal'].replace('Undefined', 'No Meal') # replace 'Undefined' meal with 'No Meal'
df['market_segment'] = df['market_segment'].replace('Undefined', 'Unkown') # replace 'Undefined' market_segment with 'Unknown'

# Replace text 'NULL' and blanks with NaN, then fill
df['agent'] = df['agent'].replace(['NULL', 'null', ''], np.nan).fillna('No Agent')
df['company'] = df['company'].replace(['NULL', 'null', ''], np.nan).fillna('No Company')

# Convert children to numeric, replacing 'NA', 'na', blanks with 0
df['children'] = df['children'].replace(['NA', 'na', ''], 0)
df['children'] = pd.to_numeric(df['children'], errors='coerce').fillna(0).astype(int)

# Cleaning: handling negative ADR values
# Flag invalid ADR entries
df['adr_flag'] = np.where(df['adr'] < 0, 'Invalid', 'Valid')

# Count flagged entries
invalid_count = df[df['adr_flag'] == 'Invalid'].shape[0]
print(f"⚠️ Found {invalid_count} invalid ADR entries (flagged for review)")

# Remove invalid entries from main dataset
df = df[df['adr'] >= 0]

# Create full arrival date column
# Combine year, month, day into a single date
df['arrival_date'] = pd.to_datetime(
    df['arrival_date_year'].astype(str) + '-' +
    df['arrival_date_month'].astype(str) + '-' +
    df['arrival_date_day_of_month'].astype(str),
    format='%Y-%B-%d',
    errors='coerce'
)

# Extract year and month from arrival_date
df['arrival_year'] = df['arrival_date'].dt.year
df['arrival_month'] = df['arrival_date'].dt.month

# Validation summary
print("🧾 Data Cleaning Summary:")
print(f"Unique meals: {df['meal'].unique()}")
print(f"Unique market segments: {df['market_segment'].unique()}")
print(f"ADR min: {df['adr'].min()} | max: {df['adr'].max()}")
print(f"Missing arrival_date values: {df['arrival_date'].isna().sum()}")

# Export cleaned data to CSV
df.to_csv(r"data/str_reservations_clean.csv", index=False)
print("✅ Exported cleaned dataset -> data/str_reservations_clean.csv")

# Close connection
conn.close()