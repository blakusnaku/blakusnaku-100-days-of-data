#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: Numeric Cleaning (Comma Removal, Coercion)
# Phase: Cleaning Stage
# Dataset: InsideAirbnb — listings/calendar
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: cleaners/numeric_cleaner.py
#===========================================================
# 
# 🎯 GOAL:
# Clean numeric fields by removing commas and coercing values to numeric.
# 
# 🔁 PIPELINE FLOW:
# - Identify numeric columns from config
# - Remove commas
# - Convert to numeric with coercion
# 
# 📘 NOTES:
# Ensures downstream aggregation (SUM, AVG, etc.) is always accurate.
# 
#===========================================================

import pandas as pd

def clean_numeric_columns(df, config, dataset_key):
    numeric_cols = [
        col for col, dtype in config["cleaning"]["dtypes"][dataset_key].items()
        if dtype in ["float", "int"]
    ]

    for col in numeric_cols:
        if col not in df.columns:
            continue

        df[col] = df[col].astype(str).str.replace(",", "", regex=False)
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df
