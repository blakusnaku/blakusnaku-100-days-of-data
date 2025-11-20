#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 4 — KPI MODELING
# Task: Compute listing-level & city-level KPIs (with Simulated ADR/RevPAR)
# Phase: STR Pipeline — Stage 4
# Dataset: InsideAirbnb (Transformed + Harmonized)
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/_04_run_kpi_modeling.py
#===========================================================
#
# 🎯 GOAL:
# Compute all KPI metrics needed for STR dashboarding:
#   - Listing-level KPIs (engagement score, occupancy proxy, simulated ADR/RevPAR)
#   - City-level KPIs (market supply, averages, ratios)
#
# 🔁 PIPELINE FLOW:
# 1. Load transformed listings (per city)
# 2. Generate listing-level KPIs using pricing model from config
# 3. Aggregate into city-level KPI summary
# 4. Save KPI outputs (per city + combined)
#
# 📘 NOTES:
# - Fully modular structure → modules/kpi/
# - Simulated ADR uses pricing rules from etl_config.json
# - Warnings removed using safe casting & clipping
#
#===========================================================

import os
import json
import pandas as pd

from modules.kpi.listing_kpis import compute_listing_kpis
from modules.kpi.city_kpis import compute_city_kpis


def run_kpi_modeling(config_path="etl_config.json"):

    print("\n🔹 Stage 4: KPI Modeling\n")
    print("🚀 Starting KPI Modeling Stage (Stage 4)...\n")

    # ---- Load config -----------------------------------------------------
    with open(config_path, "r") as f:
        config = json.load(f)

    transformed_path = config["transformed_path"]
    output_path = config["kpi_output_path"]
    pricing_cfg = config.get("simulated_pricing", {})

    os.makedirs(output_path, exist_ok=True)

    all_city_listings = []

    # ----------------------------------------------------------------------
    #                PROCESS LISTINGS PER CITY
    # ----------------------------------------------------------------------
    for city in config["cities"]:
        city_name = city["name"]
        print("=" * 46)
        print(f"   KPI MODELING FOR CITY → {city_name.upper()}")
        print("=" * 46)

        # ---- Load transformed listings -----------------------------------
        listings_file = os.path.join(
            transformed_path, f"{city_name}_listings_transformed.parquet"
        )

        if not os.path.exists(listings_file):
            print(f"⚠️ Missing transformed listings for {city_name}. Skipping...\n")
            continue

        listings_df = pd.read_parquet(listings_file)

        # ---- Listing-Level KPIs (Simulated ADR added) --------------------
        listings_kpi = compute_listing_kpis(
            df=listings_df.copy(),
            city_key=city_name,
            pricing_cfg=pricing_cfg,
        )

        # ---- Save per-city listing KPI dataset ---------------------------
        city_kpi_path = os.path.join(
            output_path, f"{city_name}_listings_kpi.parquet"
        )
        listings_kpi.to_parquet(city_kpi_path, index=False)
        print(f"✔ Saved listing KPIs → {city_kpi_path}")

        # accumulate for city-level aggregation
        all_city_listings.append(listings_kpi)

    # ----------------------------------------------------------------------
    #                        CITY-LEVEL KPI AGGREGATION
    # ----------------------------------------------------------------------
    print("\n🏙  Generating city-level KPIs...")

    if all_city_listings:
        all_listings_df = pd.concat(all_city_listings, ignore_index=True)
        city_kpis = compute_city_kpis(all_listings_df)

        output_city_kpi_path = os.path.join(output_path, "city_kpis.parquet")
        city_kpis.to_parquet(output_city_kpi_path, index=False)

        print(f"✔ Saved city-level KPIs → {output_city_kpi_path}")
    else:
        print("⚠️ No listings available. City-level KPIs skipped.")

    print("\n🎉 KPI MODELING STAGE COMPLETE!\n")
