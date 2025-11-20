#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 2 — Python ACTION
# Task: City-Level Harmonization Pipeline Runner
# Phase: Harmonization Stage — Multi-City ETL
# Dataset: InsideAirbnb — listings/calendar
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/02_run_harmonization.py
#===========================================================
# 
# 🎯 GOAL:
# Apply semantic harmonization rules across all cleaned datasets.
# Transforms inconsistent categories into a unified, canonical structure
# (e.g., property_type, room_type, neighbourhood names, city/state fields).
# 
# 🔁 PIPELINE FLOW:
# 1. Load cleaned outputs (Stage 1)
# 2. Apply harmonization functions (property mappings, room type standardization, etc.)
# 3. Save harmonized outputs to /data/harmonized/
# 
# 📘 NOTES:
# - This script should remain an orchestrator only.
# - All harmonization logic lives inside /harmonizers/.
# - This ensures full modularity in your ETL design.
# 
#===========================================================
  
import json
import pandas as pd
from modules.harmonizers.harmonize_listings import harmonize_listings
from modules.harmonizers.harmonize_calendar import harmonize_calendar
import sys,os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def run_harmonization(config_path="etl_config.json"):
    """Run semantic harmonization for all cities using cleaned outputs."""

    # Load Config
    with open(config_path, "r") as f:
        config = json.load(f)

    processed_path = config["processed_path"]
    output_path = "data/harmonized"
    os.makedirs(output_path, exist_ok=True)

    print("\n🚀 Starting Harmonization Stage (Stage 2)...\n")

    for city in config["cities"]:
        city_name = city["name"]

        print(f"==============================================")
        print(f"   HARMONIZING CITY → {city_name.upper()}")
        print(f"==============================================")

        # ------------------------------
        # 1. LOAD CLEANED INPUT DATA
        # ------------------------------
        listings_in = os.path.join(processed_path, f"{city_name}_listings.parquet")
        calendar_in = os.path.join(processed_path, f"{city_name}_calendar.parquet")

        print(f"📥 Loading cleaned listings → {listings_in}")
        listings_df = pd.read_parquet(listings_in)

        print(f"📥 Loading cleaned calendar → {calendar_in}")
        calendar_df = pd.read_parquet(calendar_in)

        # ------------------------------
        # 2. APPLY HARMONIZATION MODULES
        # ------------------------------
        print("🔧 Harmonizing listings...")
        listings_h = harmonize_listings(listings_df, config, city_name)

        print("🔧 Harmonizing calendar...")
        calendar_h = harmonize_calendar(calendar_df, config, city_name)

        # ------------------------------
        # 3. SAVE OUTPUTS
        # ------------------------------
        listings_out = os.path.join(output_path, f"{city_name}_listings_harmonized.parquet")
        calendar_out = os.path.join(output_path, f"{city_name}_calendar_harmonized.parquet")

        print(f"💾 Saving harmonized listings → {listings_out}")
        listings_h.to_parquet(listings_out, compression=config["output_settings"]["compression"])

        print(f"💾 Saving harmonized calendar → {calendar_out}")
        calendar_h.to_parquet(calendar_out, compression=config["output_settings"]["compression"])

        print(f"✔ Completed harmonization for {city_name}\n")

    print("\n🎉 HARMONIZATION STAGE COMPLETE!\n")


if __name__ == "__main__":
    run_harmonization()
