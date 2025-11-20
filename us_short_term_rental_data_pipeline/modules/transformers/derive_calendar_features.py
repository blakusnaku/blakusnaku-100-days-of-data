#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 3 — Python ACTION
# Task: Calendar-Level Transformation Logic
# Phase: Transformation Stage — BI Prep
# Dataset: InsideAirbnb — calendar table
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: modules/transformers/derive_calendar_features.py
#===========================================================
#
# 🎯 GOAL:
# Transform daily calendar data to enable:
#   - daily occupancy calculations
#   - time-series trends
#   - day-of-week / month-of-year aggregations
#   - factual star schema structure
#
# ----------------------------------------------------------
# OUTPUT FIELDS INCLUDED:
#   listing_id
#   date
#   available (bool)
#   is_available (1/0)
#   is_booked (1/0)
#   day_of_week (0–6)
#   month
#   year
#
#===========================================================

import pandas as pd


# -----------------------------------------------------------
# Helpers
# -----------------------------------------------------------

def _safe_dt(series):
    """Convert to datetime safely, returning NaT when invalid."""
    return pd.to_datetime(series, errors="coerce")


def _normalize_available(val):
    """
    Normalize availability flags.
    Dataset uses:
      - "t"/"f"
      - True/False
      - "true"/"false"
    """
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        v = val.strip().lower()
        if v in ["t", "true", "available", "yes", "y", "1"]:
            return True
        if v in ["f", "false", "no", "n", "0", "unavailable"]:
            return False
    return False  # default fallback


# -----------------------------------------------------------
# Main transformation function
# -----------------------------------------------------------

def transform_calendar(df: pd.DataFrame, city_key: str) -> pd.DataFrame:
    """
    Clean & transform calendar dataset for STR analytics.
    """

    # -------------------------------------------------------
    # Normalize column names
    # -------------------------------------------------------
    df.columns = df.columns.str.lower().str.strip()

    # -------------------------------------------------------
    # Ensure required fields exist
    # -------------------------------------------------------
    required = ["listing_id", "date", "available"]
    for col in required:
        if col not in df.columns:
            df[col] = None

    # -------------------------------------------------------
    # Date conversion
    # -------------------------------------------------------
    df["date"] = _safe_dt(df["date"])

    # -------------------------------------------------------
    # Normalize availability flags
    # -------------------------------------------------------
    df["available"] = df["available"].apply(_normalize_available)

    # Boolean numeric versions for Power BI Facts
    df["is_available"] = df["available"].astype(int)
    df["is_booked"] = (df["available"] == False).astype(int)

    # -------------------------------------------------------
    # Time intelligence fields
    # -------------------------------------------------------
    df["day_of_week"] = df["date"].dt.weekday  # 0=Mon, 6=Sun
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    # -------------------------------------------------------
    # Sort & tidy
    # -------------------------------------------------------
    df = df.sort_values(["listing_id", "date"]).reset_index(drop=True)

    return df
