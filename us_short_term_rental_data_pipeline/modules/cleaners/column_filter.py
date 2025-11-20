#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: Modular Column Filtering for STR Pipeline
# Phase: Cleaning Stage
# Dataset: InsideAirbnb — listings/calendar/reviews
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: cleaners/column_filter.py
# ===========================================================
# 
# 🎯 GOAL:
# Keep only the columns defined in config['cleaning']['use_columns'].
# Drops all extra columns to maintain a strict, dashboard-aligned schema.
# 
# 🔁 PIPELINE FLOW:
# - Read raw dataframe
# - Normalize column names (optional)
# - Filter to allowlisted columns
# 
# 📘 NOTES:
# Allowlist-driven filtering ensures the BI dashboard schema is easy to change
# without editing Python code — only config needs to be updated.
# 
# ===========================================================

def filter_columns(df, config, dataset_key):
    """Keep only config-allowed columns."""
    allowed = config["cleaning"]["use_columns"][dataset_key]
    cols_to_keep = [col for col in allowed if col in df.columns]
    return df[cols_to_keep].copy()
