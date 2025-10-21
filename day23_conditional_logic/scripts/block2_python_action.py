# ===========================================================
# 📦 PROJECT METADATA
# -----------------------------------------------------------
# Day: 23
# Date: 2025-10-21
# Block: 2 — PYTHON ACTION
# Task: Use np.where for same logic
# Phase: Python Foundations
# Dataset: superstore_cleaned.csv
# Tool: Python (pandas, numpy)
# Author: JP Malit
# Repository: blakusnaku-100-days-of-data
# File: scripts/block2_python_action.py
# ===========================================================

"""
🎯 GOAL:
Replicate SQL CASE logic using numpy.where() to classify orders
into 'High Value', 'Medium Value', or 'Low Value' categories.

🔁 PIPELINE FLOW:
SQL (CASE) → Python (np.where) → Power BI (Category Filter) → GitHub Reflection

📘 NOTES:
- Demonstrates vectorized conditional logic with np.where().
- Matches classification thresholds from Block 1.
- Output saved as superstore_with_category.csv for Power BI use.
"""

#import necessary libraries
import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv(r'data/superstore.csv')

# apply np.where to classify sales
df['sales_category'] = np.where(
    df['sales'] >= 500, 'High Value',
    np.where(df['sales'].between(200, 499), 'Medium Value', 'Low Value')
)

# save the modified dataset
output_path = r'data/superstore_with_category.csv'
df.to_csv(output_path, index=False)

# display sample output
print(df[['order_id', 'customer_name', 'region', 'sales', 'sales_category']].head(10))
print(f"\n✅ File saved to: {output_path}")
