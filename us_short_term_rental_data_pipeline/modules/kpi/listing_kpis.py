#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 4 — KPI MODELING
# Task: Listing-level KPI Computation (Simulated ADR + RevPAR)
# Phase: STR Pipeline — Stage 4
# Dataset: InsideAirbnb (Transformed + Harmonized)
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: modules/kpi/listing_kpis.py
#===========================================================
#
# 🎯 GOAL:
# Compute listing-level STR KPIs:
#   - reviews_per_month_calc
#   - engagement_score
#   - occupancy_score
#   - simulated_adr (Hybrid Option C)
#   - simulated_revpar
#
#===========================================================

import pandas as pd


# -----------------------------------------------------------
# Safe numeric helpers
# -----------------------------------------------------------

def _safe_num_scalar(value, default=0.0):
    """Safe conversion for single numeric values."""
    num = pd.to_numeric(value, errors="coerce")
    return default if pd.isna(num) else float(num)


def _safe_num_series(series, default=0.0):
    """Safe conversion for pandas Series."""
    series = pd.to_numeric(series, errors="coerce")
    return series.fillna(default)


# -----------------------------------------------------------
# Rating bucket helper
# -----------------------------------------------------------

def _bucket_rating(score):
    """Return: high / mid / low rating bucket."""
    score = _safe_num_scalar(score, 0)
    if score >= 4.6:
        return "high"
    if score >= 4.0:
        return "mid"
    return "low"


# -----------------------------------------------------------
# Hybrid ADR simulation engine
# -----------------------------------------------------------

def _simulate_adr_for_row(row, city_key, cfg):
    """
    Option C Hybrid ADR logic:
      base ADR + bedroom adj + accommodates adj
      × city multiplier × rating multiplier
    """

    # Base price by room type
    rt = row.get("room_type", "Private room")
    base_map = cfg.get("base_adr_by_room_type", {})
    base_price = base_map.get(rt, 60)

    # City multiplier
    city_mult = cfg.get("city_multiplier", {}).get(city_key, 1.0)

    # Numeric adjustments
    bedrooms = _safe_num_scalar(row.get("bedrooms"), 0)
    accommodates = _safe_num_scalar(row.get("accommodates"), 1)
    rating = _safe_num_scalar(row.get("review_scores_rating"), 0)

    bedroom_adj = cfg.get("bedroom_adjustment", 15)
    accommodates_adj = cfg.get("accommodates_adjustment", 4)

    # Rating multiplier
    rating_bucket = _bucket_rating(rating)
    rating_mult = cfg.get("review_rating_adjustment", {}).get(
        rating_bucket, 1.00
    )

    # Compute ADR
    adr = (
        base_price
        + bedrooms * bedroom_adj
        + accommodates * accommodates_adj
    )

    adr *= city_mult
    adr *= rating_mult

    return round(adr, 2)


# -----------------------------------------------------------
# Listing level KPI computation
# -----------------------------------------------------------

def compute_listing_kpis(df: pd.DataFrame, city_key: str, pricing_cfg: dict):
    """
    Compute listing-level STR KPIs for a single city.
    """

    # -------------------------------------------------------
    # Reviews per month
    # -------------------------------------------------------
    df["reviews_per_month_calc"] = (
        df["number_of_reviews"] /
        ((df["listing_age_days"] / 30).replace(0, pd.NA))
    )

    df["reviews_per_month_calc"] = (
        df["reviews_per_month_calc"]
        .fillna(0)
        .astype(float)
    )

    # -------------------------------------------------------
    # Engagement Score:
    #   70% review velocity
    #   30% availability signal
    # -------------------------------------------------------
    availability = _safe_num_series(df["availability_365"].clip(lower=0), 0)

    df["engagement_score"] = (
        (df["reviews_per_month_calc"] * 0.7)
        + ((availability / 365) * 0.3)
    ).astype(float)

    # -------------------------------------------------------
    # Occupancy Score:
    #   1 - (availability_365 / 365)
    # -------------------------------------------------------
    df["occupancy_score"] = (
        1 - (availability / 365)
    ).clip(lower=0, upper=1)

    # -------------------------------------------------------
    # Simulated ADR (per listing)
    # -------------------------------------------------------
    df["simulated_adr"] = df.apply(
        lambda row: _simulate_adr_for_row(row, city_key, pricing_cfg),
        axis=1
    )

    # -------------------------------------------------------
    # Simulated RevPAR
    # -------------------------------------------------------
    df["simulated_revpar"] = (
        df["simulated_adr"] * df["occupancy_score"]
    ).round(2)

    # -------------------------------------------------------
    # Sort listings by revenue potential for readability
    # -------------------------------------------------------
    df = df.sort_values(
        by=["simulated_revpar", "engagement_score"],
        ascending=False
    ).reset_index(drop=True)

    return df
