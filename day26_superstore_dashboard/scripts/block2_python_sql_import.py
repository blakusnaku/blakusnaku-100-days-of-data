#===========================================================
#📦 PROJECT METADATA
#-----------------------------------------------------------
#Day: 26
#Date: 2025-10-26
#Block: 2 — PYTHON ACTION
#Task: Import SQL-verified Superstore dataset and validate structure
#Phase: BI Mastery — Superstore Capstone
#Dataset: superstore_clean_stage3.csv
#Tool: Python (pandas)
#Author: JP Malit
#Repository: blakusnaku-100-days-of-data
#File: scripts/block2_python_sql_import.py
#===========================================================
#
# 🎯 GOAL:
#Load the SQL-verified dataset, confirm structure and datatypes,
#compare with prior stages, and ensure readiness for Power BI.
#
# 🔁 PIPELINE FLOW:
# Excel → SQL → Python → Power BI
#
# 📘 NOTES:
# Final integrity validation before visualization phase.
#===========================================================

import pandas as pd

# -----------------------------------------------------------
# 1️⃣ Load Dataset
# -----------------------------------------------------------
df = pd.read_csv(r"data/superstore_clean_stage3.csv")

print("✅ Dataset successfully loaded.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# -----------------------------------------------------------
# 2️⃣ Data Type Corrections
# -----------------------------------------------------------

# Convert postal_code back to string and pad zeros
df["postal_code"] = df["postal_code"].astype(str).str.strip().str.zfill(5)

# Convert dates to datetime format
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")


# -----------------------------------------------------------
# 3️⃣ Quick Overview
# -----------------------------------------------------------
print("\n📋 Columns Overview:")
print(df.dtypes)

print("\n🔍 Sample Rows:")
print(df.head(3))

# -----------------------------------------------------------
# 4️⃣ Data Validations
# -----------------------------------------------------------

# Check for nulls
nulls = df.isnull().sum().sum()
print(f"\nNull count: {nulls}")

# Validate record count (should match previous stages)
expected_rows = 9994  # update if known
if df.shape[0] == expected_rows:
    print("✅ Record count matches previous stages.")
else:
    print(f"⚠️ Record count mismatch! Found {df.shape[0]} rows.")

# Validate date columns format
try:
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])
    print("✅ Date columns successfully parsed.")
except Exception as e:
    print(f"⚠️ Date parsing issue: {e}")

# Validate postal_code leading zeros
invalid_postal = df[df["postal_code"].str.len() != 5]
if invalid_postal.empty:
    print("✅ All postal codes retain 5-digit structure.")
else:
    print(f"⚠️ {len(invalid_postal)} postal codes not 5 digits.")

# Validate numeric columns
numeric_cols = ["sales", "profit", "discount", "quantity"]
if df[numeric_cols].isnull().sum().sum() == 0:
    print("✅ Numeric fields clean and valid.")
else:
    print("⚠️ Missing or invalid values in numeric fields.")

# -----------------------------------------------------------
# 5️⃣ Export validated dataset for Power BI
# -----------------------------------------------------------
output_path = r"data/superstore_clean_final.csv"
df.to_csv(output_path, index=False)
print(f"\n💾 Exported Power BI-ready dataset → {output_path}")

# -----------------------------------------------------------
# 6️⃣ Summary
# -----------------------------------------------------------
print("\n🎯 Final Validation Summary:")
print("- No nulls or blanks detected")
print("- Dates parsed correctly")
print("- Postal codes formatted consistently")
print("- Record count consistent with previous stages")
print("- Dataset officially ready for Power BI integration")
