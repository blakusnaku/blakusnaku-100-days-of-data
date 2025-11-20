#===========================================================
# 📦 PROJECT METADATA
#-----------------------------------------------------------
# Day: 51
# Date: 2025-11-18
# Block: 3 — Python ACTION
# Task: Listing Flags Module
# Phase: Transformation Stage
# Dataset: InsideAirbnb — listings
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: modules/transformers/listing_flags.py
#===========================================================
#
# 🎯 GOAL:
# Generate boolean flags for segmentation in Power BI:
# - entire_home, private_room, shared_room
# - high_rating, low_review_count
# - long_stay_ready
#
#===========================================================

import pandas as pd


def add_listing_flags(df):

    df["is_entire_home"] = df["room_type"].eq("entire_home")
    df["is_private_room"] = df["room_type"].eq("private_room")
    df["is_shared_room"] = df["room_type"].eq("shared_room")

    df["is_high_rating"] = df["review_scores_rating"].fillna(0) >= 4.8
    df["is_low_review_count"] = df["number_of_reviews"].fillna(0) < 5

    df["is_longstay_ready"] = df["minimum_nights"].fillna(0) <= 7

    return df
