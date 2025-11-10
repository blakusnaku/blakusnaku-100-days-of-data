#===============================================
# 📦 PROJECT METADATA
#-----------------------------------------------
# Day: 42
# Date: 2025-11-09
# Process: extract_amenity_keywords.py
# BLock: 1 - Extract Keywords from listing titles
# Phase: Data Analysis - Feature Engineering
# Dataset: str_market_clean_v2.parquet
# Tool: Python (pandas, re, json)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
#===============================================

import os
import re
import json
import pandas as pd

#load config
CONFIG_PATH = "etl_config.json"
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

INTERIM_DIR = config["output_path"] 
OUTPUT_FILE = os.path.join(INTERIM_DIR, "str_market_with_amenities_v1.parquet")

def run_extract_amenity_keywords():
    print("\n=== 🔖 Extracting Amenity Keywords from Titles ===")

    #step 1: combine all harmonized listings
    harmonized_dfs = []
    for city in config['cities']:
        city_key = city['name']
        harmonized_path = os.path.join(INTERIM_DIR, f"harmonized_{city_key}_listings.csv")
        if os.path.exists(harmonized_path):
            df = pd.read_csv(harmonized_path, low_memory=False)
            df["city_key"] = city_key
            harmonized_dfs.append(df)
        else:
            print(f"⚠ No harmonized listings found. Exiting.")
            return
        
    if not harmonized_dfs:
        print("❌ No harmonized listings found. Exiting.")
        return

    listings_df = pd.concat(harmonized_dfs, ignore_index=True)
    print(f"Loaded {len(listings_df):,} total listings across cities")

    #extract amenities from titles
    listings_df["text_blob"] = (
        listings_df["description"].fillna("") + " " +
        listings_df["amenities"].fillna("")
    ).str.lower()

    keywords = [
        "wifi", "pool", "parking", "kitchen", "balcony", "gym", "pet", "view",
        "beach", "downtown", "garden", "fireplace", "bbq", "washer", "dryer",
        "tv", "hot tub", "spa", "breakfast", "lake", "rooftop", "patio",
        "workspace", "self check-in", "netflix", "air conditioning", "ac"
    ]

    for key in keywords:
        pattern = rf"\b{re.escape(key)}\b"
        listings_df[f"amenity_{key.replace(' ', '_')}"] = listings_df["text_blob"].str.contains(pattern, regex=True, case=False)

    amenity_cols = [c for c in listings_df.columns if c.startswith("amenity_")]
    listings_df["amenity_count"] = listings_df[amenity_cols].sum(axis=1)
    
    print(f"✅ {len(amenity_cols)} amenity flags | Avg amenities per listing: {listings_df['amenity_count'].mean():.2f}")

    # merge with cleaned dataset to preserve kpi fields
    clean_path = os.path.join(INTERIM_DIR, "str_market_clean_v2.parquet")
    clean_df = pd.read_parquet(clean_path)

    # ensure both sides have consistent key dtype
    clean_df["listing_id"] = clean_df["listing_id"].astype(str)
    listings_df["listing_id"] = listings_df["listing_id"].astype(str)


    # drop text blob column
    if "text_blob" in listings_df.columns:
        listings_df.drop(columns=["text_blob"], inplace=True)

    merged_df = pd.merge(
        clean_df,
        listings_df[["listing_id"] + amenity_cols + ["amenity_count"]],
        on="listing_id",
        how="left"
    )

    # save output
    merged_df.to_parquet(OUTPUT_FILE, index=False, compression="snappy")
    print(f"💾 Saved amenity-augmented dataset ➡ {OUTPUT_FILE}")
    print("=== ✅ extract_amenity_keywords.py complete ===\n")

if __name__ == '__main__':
    run_extract_amenity_keywords()