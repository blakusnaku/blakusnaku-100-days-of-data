#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: Drop Fully Null Columns
# Phase: Cleaning Stage
# Dataset: InsideAirbnb
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: cleaners/missing_cleaner.py
#===========================================================
#
# 🎯 GOAL:
# Drop columns that contain only null values (optional based on config).
# 
# ===========================================================

def drop_all_null_columns(df, config):
    if config["cleaning"]["cleaning_rules"]["drop_columns_with_all_nulls"]:
        df = df.dropna(axis=1, how="all")
    return df
