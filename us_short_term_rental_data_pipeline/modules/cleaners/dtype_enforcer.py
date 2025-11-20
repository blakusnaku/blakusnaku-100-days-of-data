#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 1 — Python ACTION
# Task: Final Dtype Enforcement
# Phase: Cleaning Stage
# Dataset: InsideAirbnb
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: cleaners/dtype_enforcer.py
#===========================================================
#
# 🎯 GOAL:
# Strictly cast all columns to final dtypes as defined in config.
#
# 🔁 PIPELINE FLOW:
# - Look up dtype rules from config
# - Convert each column accordingly
#
# 📘 NOTES:
# Guaranteed schema alignment for BI and database insertion.
#
#===========================================================

import pandas as pd


def _convert_to_boolean(series):
    """
    Convert common truthy/falsy string patterns to pandas boolean dtype.
    Supports:
    - "t" / "f"
    - "true" / "false"
    - "1" / "0"
    - "yes" / "no"
    """
    truth_map = {
        "t": True,
        "true": True,
        "1": True,
        "yes": True,

        "f": False,
        "false": False,
        "0": False,
        "no": False,
    }

    # Normalize and map
    series = (
        series.astype("string")
        .str.strip()
        .str.lower()
        .map(truth_map)
        .astype("boolean")
    )

    return series


def enforce_dtypes(df, config, dataset_key):
    """Apply dtype rules from config['cleaning']['dtypes'][dataset_key]."""

    dtype_map = config["cleaning"]["dtypes"][dataset_key]

    for col, dtype in dtype_map.items():

        if col not in df.columns:
            continue

        # INT64 — nullable integers
        if dtype == "int":
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

        # FLOAT — allow NaN
        elif dtype == "float":
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # BOOLEAN — use safe truth-map logic
        elif dtype == "bool":
            df[col] = _convert_to_boolean(df[col])

        # STRING — normalized string dtype
        elif dtype == "string":
            df[col] = df[col].astype("string")

        # DATE — convert to Python date objects
        elif dtype == "date":
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

    return df