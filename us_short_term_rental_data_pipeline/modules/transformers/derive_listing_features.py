#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 3 — Python ACTION
# Task: Listing-Level Transformation Logic
# Phase: Transformation Stage — BI Prep
# Dataset: InsideAirbnb — listings table
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: modules/transformers/derive_listing_features.py
#===========================================================
#
# 🎯 GOAL:
# Apply all business-logic transformations to harmonized
# listings datasets, preparing them for KPI modeling and 
# Power BI star-schema integration.
#
# Includes:
#   - Column normalization
#   - Date conversions
#   - RoomType + PropertyType standardization
#   - Neighbourhood cleanup
#   - LISTING AGE DAYS creation
#
#===========================================================

import pandas as pd


# -----------------------------------------------------------
# Helper functions
# -----------------------------------------------------------

def _safe_dt(series):
    """Convert to datetime, return NaT on failure."""
    return pd.to_datetime(series, errors="coerce")


def _normalize_room_type(room):
    """Normalize common room_type variants."""
    if not isinstance(room, str):
        return "Other"
    r = room.strip().lower()

    if "entire" in r:
        return "Entire home/apt"
    if "private" in r:
        return "Private room"
    if "shared" in r:
        return "Shared room"
    if "hotel" in r:
        return "Hotel room"
    return "Other"


def _normalize_property_type(ptype):
    if not isinstance(ptype, str):
        return "Other"
    p = ptype.strip().lower()
    if "apartment" in p or "condo" in p:
        return "Apartment"
    if "house" in p:
        return "House"
    if "loft" in p:
        return "Loft"
    return ptype  # fallback


def _clean_neighbourhood(n):
    """Remove missing / placeholder neighbourhood names."""
    if not isinstance(n, str):
        return None
    n = n.strip()
    return n if n.lower() not in ["unknown", ""] else None


# -----------------------------------------------------------
# Main transformation function
# -----------------------------------------------------------

def transform_listings(df: pd.DataFrame, city_key: str) -> pd.DataFrame:
    """
    Apply core transformation logic to listings dataset.
    """

    # -------------------------------------------------------
    # Normalization
    # -------------------------------------------------------
    df.columns = df.columns.str.lower().str.strip()

    # Standardize room types + property types
    df["room_type"] = df["room_type"].apply(_normalize_room_type)
    if "property_type" in df.columns:
        df["property_type"] = df["property_type"].apply(_normalize_property_type)

    # Neighbourhood cleanup
    if "neighbourhood_cleansed" in df.columns:
        df["neighbourhood_cleansed"] = df["neighbourhood_cleansed"].apply(_clean_neighbourhood)

    # -------------------------------------------------------
    # Date conversions
    # -------------------------------------------------------
    if "last_scraped" in df.columns:
        df["last_scraped"] = _safe_dt(df["last_scraped"])
    if "first_review" in df.columns:
        df["first_review"] = _safe_dt(df.get("first_review"))
    if "host_since" in df.columns:
        df["host_since"] = _safe_dt(df.get("host_since"))

    # -------------------------------------------------------
    # LISTING AGE DAYS (Robust for missing columns)
    # -------------------------------------------------------

    # Convert possible reference dates
    last_scraped = pd.to_datetime(df.get("last_scraped"), errors="coerce")

    # Columns might not exist → use .get()
    first_review = pd.to_datetime(df.get("first_review"), errors="coerce")
    host_since = pd.to_datetime(df.get("host_since"), errors="coerce")

    # Start with all NA
    df["listing_age_days"] = pd.NA

    # 1️⃣ If first_review exists → use it
    if "first_review" in df.columns:
        df["listing_age_days"] = (last_scraped - first_review).dt.days

    # 2️⃣ If host_since exists → fill missing ages with it
    if "host_since" in df.columns:
        missing = df["listing_age_days"].isna()
        df.loc[missing, "listing_age_days"] = (
            last_scraped[missing] - host_since[missing]
        ).dt.days

    # 3️⃣ Final fallback: replace missing or invalid ages with 90 days
    df["listing_age_days"] = pd.to_numeric(df["listing_age_days"], errors="coerce")
    df["listing_age_days"] = df["listing_age_days"].fillna(90)

    # 4️⃣ No negative ages allowed
    df["listing_age_days"] = df["listing_age_days"].clip(lower=30)


    # -------------------------------------------------------
    # Availability cleanup (ensure numeric)
    # -------------------------------------------------------
    if "availability_365" in df.columns:
        df["availability_365"] = pd.to_numeric(
            df["availability_365"], errors="coerce"
        ).fillna(0).clip(lower=0, upper=365)

    # -------------------------------------------------------
    # Numeric standardization (prevent dtype errors later)
    # -------------------------------------------------------
    numeric_fields = [
        "number_of_reviews", "review_scores_rating", "accommodates",
        "bedrooms", "beds", "bathrooms", "minimum_nights",
        "maximum_nights"
    ]

    for col in numeric_fields:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # -------------------------------------------------------
    # Final clean ordering (optional)
    # -------------------------------------------------------
    if "id" in df.columns:
        df = df.sort_values("id").reset_index(drop=True)

    return df
