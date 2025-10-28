################################
# Day: 30
# Date: 2025-10-28
# Block: 2 — PYTHON ACTION
# Task: Debug pandas KeyError on 'listing_id' merge
# Phase: STR Debug Series
# Dataset: listings_calendar_joined.csv
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/block2_python_action.py
#################################
# GOAL: Replicate and troubleshoot a KeyError: 'listing_id' when merging STR datasets
# We'll test scenarios where:
#   - column names mismatch (Listing_ID, listing_id, etc.)
#   - one of the DataFrames is missing the key
#   - a column becomes and index after loading
#################################

import pandas as pd

# load the two dummy raw tables again
listings = pd.read_csv(r'data/raw/listings_raw.csv')
calendar = pd.read_csv(r'data/raw/calendar_raw.csv')

# display columns to confirm
print(listings.columns)
print(calendar.columns)

# debug it (added after the error in first try)
listings.columns = listings.columns.str.strip().str.lower()
calendar.columns = calendar.columns.str.strip().str.lower()

# recreate the join (expected to fail) 
# changed calendar_raw.csv header from 'listing_id' to 'Listing_ID'
merged = pd.merge(listings, calendar, on="listing_id", how="left")

# (1) Expected error: 
#   KeyError: 'listing_id'
# (2) After inserting debug lines to strip + lower the merge performs as expected

merged.to_csv(r'data/interim/merged_debugged.csv', index=False)