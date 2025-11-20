#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 4 — KPI MODELING
# Task: Calendar-Level KPI Calculations
# Phase: STR Pipeline — KPI Modeling (Stage 4)
# Dataset: InsideAirbnb Calendar (Harmonized)
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: modules/kpi/calendar_kpis.py
#===========================================================
#
# 🎯 GOAL:
# Compute calendar-level KPIs that help visualize market occupancy
# patterns in Power BI:
#  - occupancy_flag (1 = booked, 0 = available)
#  - occupancy_rate (overall)
#  - daily supply
#  - daily occupancy
#  - weekday vs weekend occupancy
#
# 🔁 PIPELINE FLOW:
# 1. Ensure safe boolean → numeric conversions
# 2. Create occupancy_flag from `available` column
# 3. Aggregate daily occupancy & supply metrics
# 4. Return KPI-enhanced calendar dataframe + daily summary table
#
# 📘 NOTES:
# - No numpy.nanmean
# - No skipna arguments (pandas native mean already safe)
# - No downcasting warnings
#===========================================================

import pandas as pd


def compute_calendar_kpis(df: pd.DataFrame, city_name: str):
    """
    Compute listing-level occupancy KPIs from the harmonized calendar dataset.

    Returns:
        calendar_with_kpis (DataFrame)
        daily_calendar_summary (DataFrame)
    """

    # -------------------------------------------------------
    # 1. ENSURE SAFE TYPES (avoid warnings)
    # -------------------------------------------------------
    if "available" in df.columns:
        # available = "t" or "f" → convert to boolean
        df["available"] = df["available"].astype(str).str.lower()
        df["available"] = df["available"].map({"t": True, "f": False})
    
    # Cast dates safely
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    
    # -------------------------------------------------------
    # 2. OCCUPANCY FLAG (1 = booked, 0 = available)
    # -------------------------------------------------------
    df["occupancy_flag"] = df["available"].apply(lambda x: 0 if x else 1)

    # -------------------------------------------------------
    # 3. DAILY OCCUPANCY SUMMARY TABLE
    # -------------------------------------------------------
    daily_summary = df.groupby("date").agg(
        total_listings=("listing_id", "count"),
        total_occupied=("occupancy_flag", "sum"),
    ).reset_index()

    # occupancy rate per day
    daily_summary["occupancy_rate"] = (
        daily_summary["total_occupied"] / daily_summary["total_listings"]
    )

    # weekday indicator (0 = Monday, 6 = Sunday)
    daily_summary["weekday"] = daily_summary["date"].dt.weekday
    daily_summary["is_weekend"] = daily_summary["weekday"].isin([5, 6]).astype(int)

    # add city for BI
    daily_summary["city"] = city_name

    # -------------------------------------------------------
    # 4. ADD CITY TAG TO ORIGINAL CALENDAR DATA
    # -------------------------------------------------------
    df["city"] = city_name

    return df, daily_summary
