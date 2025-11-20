#===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: Full Modular Cleaning Orchestration
# Phase: Cleaning Stage
# Dataset: InsideAirbnb — Multi-City Pipeline
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: cleaning_stage.py
#===========================================================
#
# 🎯 GOAL:
# Orchestrate all modular cleaning steps into a unified cleaning pipeline
# for each dataset (listings, calendar, reviews).
# 
# 🔁 PIPELINE FLOW:
# 1. Normalize column names
# 2. Filter to config-allowed columns
# 3. Global cleaning (whitespace, empty→null, dedupe)
# 4. Numeric cleaning
# 5. Date cleaning
# 6. String cleaning
# 7. Drop all-null columns (optional)
# 8. Enforce final dtypes
# 
# 📘 NOTES:
# This function should be called per dataset_type per city run.
# Allows fully automated cleaning for any new city added to config.
# 
#===========================================================

from modules.cleaners.column_filter import filter_columns
from modules.cleaners.base_cleaner import (
    normalize_column_names,
    strip_whitespace,
    convert_empty_strings_to_null,
    deduplicate_rows
)
from modules.cleaners.numeric_cleaner import clean_numeric_columns
from modules.cleaners.date_cleaner import clean_date_columns
from modules.cleaners.string_cleaner import clean_string_columns
from modules.cleaners.missing_cleaner import drop_all_null_columns
from modules.cleaners.dtype_enforcer import enforce_dtypes


def run_cleaning(df, config, dataset_key):

    # 1. Normalize column names
    if config["cleaning"]["cleaning_rules"]["normalize_column_names"]:
        df = normalize_column_names(df)

    # 2. Restrict to allowed columns
    df = filter_columns(df, config, dataset_key)

    # 3. Global cleaning operations
    if config["cleaning"]["cleaning_rules"]["strip_whitespace"]:
        df = strip_whitespace(df)

    if config["cleaning"]["cleaning_rules"]["convert_empty_strings_to_null"]:
        df = convert_empty_strings_to_null(df)

    if config["cleaning"]["cleaning_rules"]["deduplicate_rows"]:
        df = deduplicate_rows(df)

    # 4. Modular cleaners
    df = clean_numeric_columns(df, config, dataset_key)
    df = clean_date_columns(df, config, dataset_key)
    df = clean_string_columns(df, config, dataset_key)

    # 5. Optional: drop fully-null cols
    df = drop_all_null_columns(df, config)

    # 6. Final dtype enforcement
    df = enforce_dtypes(df, config, dataset_key)

    return df
