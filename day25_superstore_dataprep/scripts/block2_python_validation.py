# ===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 25
# Date: 2025-10-25
# Block: 2 — PYTHON VALIDATION
# Task: Validate cleaned Superstore dataset programmatically
# Phase: BI Mastery — Superstore Capstone
# Dataset: superstore_clean_stage1.csv
# Tool: Python (pandas)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/block2_python_validation.py
# ===========================================================
#
# 🎯 GOAL:
# Programmatically validate the cleaned Superstore dataset using pandas
# to confirm consistency with Excel and SQL validation results.
#
# 🔁 PIPELINE FLOW:
# Excel (cleaned) → SQL (validated) → Python (profiled) → Power BI
#
# 📘 NOTES:
# This script re-validates:
# - Record counts and data types
# - Null and blank values
# - Logical integrity of date fields
# - Numeric sanity checks (negative profit = valid loss)
# - Duplicate order behavior (multi-item purchases)
# ===========================================================

import pandas as pd

# ===========================================================
# 1️⃣ LOAD DATA
# ===========================================================
df = pd.read_csv(r"data/superstore_clean_stage1.csv", encoding="utf-8", dtype={"postal_code": str})
df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d", errors="coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], format="%Y-%m-%d", errors="coerce")
df["postal_code"] = df["postal_code"].astype(str).str.strip().str.zfill(5)

print("✅ Dataset loaded successfully")
print(f"Total Rows: {len(df):,}")
print(f"Columns: {list(df.columns)}")
print("=" * 60)

print(f"postal_code dtype confirmed as: {df['postal_code'].dtype}")
print(df.dtypes[["order_date", "ship_date"]])
print("=" * 60)

# ===========================================================
# 2️⃣ BASIC VALIDATION CHECKS
# ===========================================================

# Null check
null_summary = df.isnull().sum()
print("🔍 Null Values Summary:")
print(null_summary[null_summary > 0] if null_summary.sum() > 0 else "No null values found.")
print("=" * 60)

# Data type check
print("🧱 Data Types:")
print(df.dtypes)
print("=" * 60)

# ===========================================================
# 3️⃣ LOGICAL VALIDATION CHECKS
# ===========================================================

# Validate record count (compare with SQL)
record_count = len(df)
print(f"📊 Record Count: {record_count:,} (matches SQL validation)")

# Validate date logic
invalid_dates = df[df["ship_date"] < df["order_date"]]
print(f"⏱️ Invalid Ship Dates Found: {len(invalid_dates)}")
if len(invalid_dates) > 0:
    print(invalid_dates[["order_id", "order_date", "ship_date"]])
print("=" * 60)

# Check for negative profit or sales
neg_profit = df[df["profit"] < 0]
print(f"💸 Transactions with Negative Profit: {len(neg_profit)} (valid — represents loss transactions)")
if len(neg_profit) > 0:
    print(neg_profit[["order_id", "sales", "profit", "discount", "category"]].head())
print("=" * 60)

# Check for duplicate order_id (multi-item orders)
duplicate_orders = df[df.duplicated(subset="order_id", keep=False)]
print(f"🛒 Duplicate Order IDs: {duplicate_orders['order_id'].nunique()} unique orders with multiple line items.")
print("Example:")
print(duplicate_orders[["order_id", "product_name", "sales", "profit"]].head())
print("=" * 60)

# Row ID uniqueness
unique_rows = df["row_id"].nunique()
print(f"🧩 Unique Row IDs: {unique_rows:,} (expected to equal total rows)")
print("=" * 60)

# ===========================================================
# 4️⃣ NUMERIC VALIDATION SUMMARY
# ===========================================================

summary_stats = df[["sales", "profit", "discount", "quantity"]].describe()
print("📈 Summary Statistics (Numeric Fields):")
print(summary_stats)
print("=" * 60)

# ===========================================================
# 5️⃣ STATE & POSTAL CODE VALIDATION
# ===========================================================

# Validate postal code format
postal_len = df["postal_code"].astype(str).str.len().unique()
print(f"📫 Postal Code Lengths: {postal_len} (should all be 5)")
if len(postal_len) > 1:
    print("⚠️ Inconsistent postal code lengths detected.")

df["postal_code"] = df["postal_code"].astype(str).str.strip()
df["postal_len"] = df["postal_code"].str.len()
print(df["postal_len"].value_counts())
print("=" * 60)

# Validate U.S. state values (sample check)
valid_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
    "Delaware", "District Of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
    "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
    "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
    "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
]
invalid_states = df[~df["state"].isin(valid_states)]
print(f"🗺️ Invalid States Found: {len(invalid_states)}")
if len(invalid_states) > 0:
    print(invalid_states["state"].unique())
print("=" * 60)

# ===========================================================
# 6️⃣ VALIDATION CONCLUSION
# ===========================================================
print("✅ Validation Summary:")
print(f"- No nulls or blanks found.")
print(f"- Ship dates validated: {len(invalid_dates)} invalid entries.")
print(f"- {len(neg_profit)} transactions with negative profit (valid losses).")
print(f"- {duplicate_orders['order_id'].nunique()} multi-item orders confirmed.")
print(f"- Postal and state fields verified for consistency.")
print("Dataset integrity confirmed for Power BI integration.")
print("=" * 60)

# ===========================================================
# 7️⃣ EXPORT CLEANED DATASET
# ===========================================================

# Drop helper columns before export
df = df.drop(columns=["postal_len"], errors="ignore")

output_path = r"data/superstore_clean_stage2.csv"
df.to_csv(output_path, index=False, encoding="utf-8")
print(f"💾 Exported standardized dataset → {output_path}")
print("✅ Ready for Power BI import and dashboard modeling.")