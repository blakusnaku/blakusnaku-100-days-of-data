##############################################
# PROJECT METADATA
##############################################
# Day: 32
# Date: 2025-10-30
# Block: 2 - Python Action
# Task: Validate dataset shape and nulls in pandas
# Phase: STR Pipeline Flow
# Dataset: clean_final.csv
# Tool: Python (pandas)
# Author: JP Malit
# Repo: blakusnaku-100-days-of-data
# File: scripts/block2_python_action.py
#############################################
# GOAL:
#   load the merged STR dataset (`clean_final.csv`) and verify:
#       - shape consistency
#       - missing values
#       - data types
#       - descriptive overview
#
# PIPELINE FLOW:
#   clean_final.csv -> pandas dataframe -> df.info(), df.isnull(), df.describe()
###############################################

import pandas as pd

# load dataset
df = pd.read_csv(r'data/processed/clean_final.csv')

# convert date column to datetime
df["date"] = pd.to_datetime(df["date"],errors="coerce")

# verify conversion
print("Date Column Type:",df['date'].dtype)
print(df["date"].head())

# basic shape check
print("Database Shape:", df.shape)
print("-" *50)

# column data types
print("Data Types:")
print(df.dtypes)
print('-'*50)

# missing values check
print("Null values per column:")
print(df.isnull().sum())
print("-"*50)

# quick descriptive stats
print("Descriptive Summary:")
print(df.describe(include="all").transpose())
print('-'*50)

# validate unique listings
unique_listings = df["listing_id"].nunique()
print(f"Unique Listings: {unique_listings}")

# check available flag distribution
print('\nAvailability Breakdown:')
print(df["available"].value_counts())

# export to clean_final_validated.csv
df.to_csv(r'data/processed/clean_final_validated.csv', index=False)
print("\n Export complete! -> data/processed/clean_final_validated.csv")
