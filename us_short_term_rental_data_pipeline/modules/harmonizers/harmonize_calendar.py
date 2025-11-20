#===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 2 — Python ACTION
# Task: Harmonize Calendar Dataset
# Phase: Harmonization Stage
# Dataset: InsideAirbnb — calendar
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: harmonizers/harmonize_calendar.py
#===========================================================
# 
# 🎯 GOAL:
# Apply minimal harmonization to the calendar dataset.
# InsideAirbnb calendar fields are already consistent across cities.
#
# 🔁 PIPELINE FLOW:
# 1. Add canonical city/state fields
# 2. Future hooks for price harmonization (ADR simulation phase)
# 
# 📘 NOTES:
# Calendar harmonization is light — most cleaning was done in Stage 1.
# 
#===========================================================

import json

def harmonize_calendar(df, config, city_name):

    # City/State canonical naming (same JSON used for listings)
    with open("mappings/city_state_map.json", "r") as f:
        city_state_map = json.load(f)

    if city_name in city_state_map:
        df["city"] = city_state_map[city_name]["city"]
        df["state"] = city_state_map[city_name]["state"]

    return df
