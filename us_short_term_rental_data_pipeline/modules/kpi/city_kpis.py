#==========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 4 — KPI MODELING
# Task: City-Level KPI Computations (with Simulated ADR/RevPAR)
# Phase: STR Pipeline — KPI Modeling (Stage 4)
# Dataset: InsideAirbnb Listings (KPI-Enhanced)
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: modules/kpi/city_kpis.py
#===========================================================

from __future__ import annotations

import pandas as pd


def compute_city_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """Compute city-level KPI aggregation from listing-level data."""
    df = df.copy()

    # Ensure numeric types
    numeric_columns = [
        "review_scores_rating",
        "reviews_per_month_calc",
        "listing_engagement_score",
        "bedrooms",
        "bathrooms",
        "accommodates",
        "simulated_adr",
        "simulated_revpar",
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    grouped = df.groupby("city", dropna=False)

    # Safe retrieval for optional columns
    def safe_mean(col: str) -> pd.Series:
        if col in df.columns:
            return grouped[col].mean()
        return pd.Series([pd.NA] * len(grouped), index=grouped.size().index)

    entire_home_ratio = (
        (df["room_type"] == "Entire home/apt")
        .groupby(df["city"])
        .mean()
    )

    city_kpi_df = pd.DataFrame({
        "city": grouped.size().index,
        "total_listings": grouped.size().values,

        # Review metrics
        "avg_review_scores_rating": safe_mean("review_scores_rating").values,
        "avg_reviews_per_month_calc": safe_mean("reviews_per_month_calc").values,

        # Listing quality
        "avg_listing_engagement_score": safe_mean("listing_engagement_score").values,

        # Supply indicators
        "avg_bedrooms": safe_mean("bedrooms").values,
        "avg_bathrooms": safe_mean("bathrooms").values,
        "avg_accommodates": safe_mean("accommodates").values,

        # Pricing metrics (simulated)
        "avg_simulated_adr": safe_mean("simulated_adr").values,
        "avg_simulated_revpar": safe_mean("simulated_revpar").values,

        # Market mix
        "entire_home_ratio": entire_home_ratio.values,
    })

    return city_kpi_df
