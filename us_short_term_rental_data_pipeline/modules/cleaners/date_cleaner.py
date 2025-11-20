#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: Date Parsing & Standardization
# Phase: Cleaning Stage
# Dataset: InsideAirbnb — listings/calendar/reviews
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: cleaners/date_cleaner.py
#===========================================================
# 
# 🎯 GOAL:
# Convert date columns to YYYY-MM-DD format with coercion.
# 
# 🔁 PIPELINE FLOW:
# - Identify date columns from config
# - Convert to datetime
# - Cast to .date() objects
# 
# 📘 NOTES:
# Standardized dates ensure uniform behavior across multiple cities.
#
#===========================================================

import pandas as pd

def clean_date_columns(df, config, dataset_key):
    date_cols = [
        col for col, dtype in config["cleaning"]["dtypes"][dataset_key].items()
        if dtype == "date"
    ]

    for col in date_cols:
        if col not in df.columns:
            continue
        df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

    return df
