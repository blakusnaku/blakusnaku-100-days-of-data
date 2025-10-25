# ===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 29
# Date: 2025-10-27
# Block: 2 — PYTHON ACTION
# Task: Save cleaned bookings + listings CSVs
# Phase: STR Analytics Transition
# Dataset: hotel_bookings_cleaned.csv
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/block2_python_action.py
# ===========================================================

"""
🎯 GOAL:
Load the exported hotel_bookings snapshot and prepare cleaned CSVs
for bookings and listings datasets used in Power BI modeling.

🔁 PIPELINE FLOW:
SQL (export) → Python (clean & split) → Power BI (visualize)

📘 NOTES:
This script validates columns, handles missing values, and saves
two derived CSVs: bookings_cleaned.csv and listings_cleaned.csv.
"""

# import libraries
import pandas as pd

# load snapshot
file_path = r"data/hotel_bookings_cleaned.csv"
df = pd.read_csv(file_path)

print("loaded snapshot:")
print(df.head(),"\n")

## basic cleaning

# remove any fully empty columns
df.dropna(axis=1, how='all', inplace=True)

# strip whitespace from headers
df.columns = df.columns.str.strip()

# fill missing values for key numeric fields
for col in ['lead_time']:
    if col in df.columns:
        df[col] = df[col].fillna(0)

print(" after basic cleaning:")
print(df.head(),"\n")

## split datasets

# bookings dataset - core reservation details
bookings_cols = [
    'hotel', 'is_canceled', 'lead_time', 'arrival_date_year',
    'arrival_date_month', 'arrival_date_day_of_month']

bokings_df = df[bookings_cols].copy()

# listings dataset - property-related attributes (mock sample)
listings_cols = ['hotel', 'country', 'market_segment', 'distribution_channel']
listings_df = df[listings_cols].drop_duplicates(subset=['hotel']).copy()

## save
bokings_df.to_csv(r"data/bookings_cleaned.csv", index=False)
listings_df.to_csv(r"data/listings_cleaned.csv", index=False)

print("Saved cleaned datasets:")
print(" - bookings_cleaned.csv")
print(" - listings_cleaned.csv")

##END##