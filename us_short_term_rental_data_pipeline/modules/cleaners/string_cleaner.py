#===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: String Normalization
# Phase: Cleaning Stage
# Dataset: InsideAirbnb
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: cleaners/string_cleaner.py
#===========================================================
# 
# 🎯 GOAL:
# Ensure object columns are converted to string dtype for consistency.
#
# 🔁 PIPELINE FLOW:
# - Identify object columns
# - Cast to string dtype
# 
# 📘 NOTES:
# Guaranteed consistent string representation across the entire pipeline.
#
#===========================================================

def clean_string_columns(df, config, dataset_key):
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype("string")
    return df
 