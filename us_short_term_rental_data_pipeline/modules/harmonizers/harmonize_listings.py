#===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 2 — Python ACTION
# Task: Harmonize Listings Dataset (property types, room types, city/state)
# Phase: Harmonization Stage
# Dataset: InsideAirbnb — listings
# Tool: Python (pandas, json)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: harmonizers/harmonize_listings.py
#===========================================================
#
# 🎯 GOAL:
# Apply semantic harmonization to listings data using JSON-based mappings.
# Unify inconsistent categories across multiple cities.
# 
# 🔁 PIPELINE FLOW:
# 1. Load mapping JSONs
# 2. Standardize:
#    - property_type
#    - room_type
#    - neighbourhood_cleansed
#    - city/state canonical names
# 3. Return harmonized dataframe
# 
# 📘 NOTES:
# All mappings are editable in /mappings/*.json — no code edits required.
# 
# ===========================================================

import json
import pandas as pd
import os


def _load_mapping(file_path):
    """Load a mapping JSON (safe load)."""
    with open(file_path, "r") as f:
        return json.load(f)


def harmonize_listings(df, config, city_name):

    # Load mapping JSONs
    property_map = _load_mapping("mappings/property_type_map.json")
    room_map = _load_mapping("mappings/room_type_map.json")
    neighbourhood_map = _load_mapping("mappings/neighbourhood_map.json")
    city_state_map = _load_mapping("mappings/city_state_map.json")

    # Apply property type harmonization
    if "property_type" in df.columns:
        df["property_type"] = (
            df["property_type"]
            .astype("string")
            .map(property_map)
            .fillna(df["property_type"])  # fallback to original
        )

    # Apply room type harmonization
    if "room_type" in df.columns:
        df["room_type"] = (
            df["room_type"]
            .astype("string")
            .map(room_map)
            .fillna(df["room_type"])
        )

    # Neighbourhood harmonization (per city)
    if city_name in neighbourhood_map:
        mapping = neighbourhood_map[city_name]
        if "neighbourhood_cleansed" in df.columns:
            df["neighbourhood_cleansed"] = (
                df["neighbourhood_cleansed"]
                .astype("string")
                .map(mapping)
                .fillna(df["neighbourhood_cleansed"])
            )

    # Standardize city/state fields from JSON canonical values
    if city_name in city_state_map:
        df["city"] = city_state_map[city_name]["city"]
        df["state"] = city_state_map[city_name]["state"]

    return df
