#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: Base Cleaning Utilities (Whitespace, Nulls, Case Normalization)
# Phase: Cleaning Stage
# Dataset: InsideAirbnb — Common Columns
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: cleaners/base_cleaner.py
#===========================================================
#
# 🎯 GOAL:
# Provide foundational cleaning steps for string normalization, whitespace
# cleanup, empty→null conversion, and deduplication.
# 
# 🔁 PIPELINE FLOW:
# - Normalize column names
# - Strip whitespace
# - Convert blanks to nulls
# - Deduplicate rows
# 
# 📘 NOTES:
# These are global rules applied across all dataset types.
#
#===========================================================

import numpy as np

def normalize_column_names(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def strip_whitespace(df):
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.strip()
    return df

def convert_empty_strings_to_null(df):
    df = df.replace({"": np.nan, " ": np.nan})
    return df

def deduplicate_rows(df):
    return df.drop_duplicates()
