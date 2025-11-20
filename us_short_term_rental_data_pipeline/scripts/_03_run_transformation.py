#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 3 — Python ACTION
# Task: City-Level Transformation Pipeline Runner
# Phase: Transformation Stage — BI Prep
# Dataset: InsideAirbnb — listings/calendar
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/_03_run_transformation.py
#===========================================================
#
# 🎯 GOAL:
# Execute the transformation logic on harmonized STR datasets
# to prepare clean analytical tables for KPI modeling and
# the Power BI star schema.
#
# 🔁 PIPELINE FLOW:
# 1. Load harmonized listings & calendar files
# 2. Apply listing transformation module
# 3. Apply calendar transformation module
# 4. Save outputs to /data/transformed/
#
# 📘 NOTES:
# - Detailed transformations live in modules/transformers/
# - This runner only orchestrates workflow per city
# - Output feeds directly into Stage 4 (KPI Modeling)
#
#===========================================================

import os
import json
import pandas as pd

from modules.transformers.derive_listing_features import transform_listings
from modules.transformers.derive_calendar_features import transform_calendar


def run_transformation(config_path="etl_config.json"):

    # ------------------------------------------------------
    # Load Configuration
    # ------------------------------------------------------
    with open(config_path, "r") as f:
        config = json.load(f)

    harmonized_path = "data/harmonized"
    output_path = "data/transformed"

    os.makedirs(output_path, exist_ok=True)

    print("\n🚀 Starting Transformation Stage (Stage 3)...\n")

    # ------------------------------------------------------
    # Loop per city (listings + calendar)
    # ------------------------------------------------------
    for city in config["cities"]:
        city_name = city["name"]

        print("==============================================")
        print(f"   TRANSFORMING CITY → {city_name.upper()}")
        print("==============================================")

        # ----------------------------------
        # 1. Load Harmonized Input Files
        # ----------------------------------
        listings_in = os.path.join(
            harmonized_path, f"{city_name}_listings_harmonized.parquet"
        )
        calendar_in = os.path.join(
            harmonized_path, f"{city_name}_calendar_harmonized.parquet"
        )

        if not os.path.exists(listings_in):
            print(f"⚠️ Missing harmonized listings for {city_name}. Skipping...\n")
            continue

        if not os.path.exists(calendar_in):
            print(f"⚠️ Missing harmonized calendar for {city_name}. Skipping...\n")
            continue

        listings_df = pd.read_parquet(listings_in)
        calendar_df = pd.read_parquet(calendar_in)

        # ----------------------------------
        # 2. Apply Transformations
        # ----------------------------------
        print("✨ Transforming listings...")
        listings_t = transform_listings(listings_df, city_name)

        print("✨ Transforming calendar...")
        calendar_t = transform_calendar(calendar_df, city_name)

        # ----------------------------------
        # 3. Save Outputs
        # ----------------------------------
        listings_out = os.path.join(
            output_path, f"{city_name}_listings_transformed.parquet"
        )
        calendar_out = os.path.join(
            output_path, f"{city_name}_calendar_transformed.parquet"
        )

        listings_t.to_parquet(
            listings_out, compression=config["output_settings"]["compression"]
        )
        calendar_t.to_parquet(
            calendar_out, compression=config["output_settings"]["compression"]
        )

        print(f"✔ Completed transformation for {city_name}\n")

    print("\n🎉 TRANSFORMATION STAGE COMPLETE!\n")


if __name__ == "__main__":
    run_transformation()
