#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 3 — Python ACTION
# Task: Time Feature Engineering Module
# Phase: Transformation Stage
# Dataset: InsideAirbnb — listings/calendar
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: modules/transformers/time_features.py
#===========================================================
#
# 🎯 GOAL:
# Generate consistent time-based features for all datasets:
# - year, month, week, weekday
# - weekend flag
# - date_key (int: YYYYMMDD)
# 
# 🔁 PIPELINE FLOW:
# Used by listings and calendar transformers.
#
#===========================================================

import pandas as pd


def add_time_features(df, date_col):
    """Add year, month, week, weekday, date_key, is_weekend."""

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["week"] = df[date_col].dt.isocalendar().week.astype("Int64")
    df["weekday"] = df[date_col].dt.dayofweek
    df["is_weekend"] = df["weekday"].isin([5, 6])

    df["date_key"] = (
        df["year"].astype(str) +
        df["month"].astype(str).str.zfill(2) +
        df[date_col].dt.day.astype(str).str.zfill(2)
    ).astype("Int64")

    return df