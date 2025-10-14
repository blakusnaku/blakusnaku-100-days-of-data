#
# BLOCK 2 - PYTHON ACTION: Create Top 10 Subset in pandas
# Project: day16_top10_customers
# Dataset: Superstore (orders)
# Author: blakusnaku
# Date: 2025-10-14
# ----------------------------------------------
# GOAL:
# - Load the exported TOp 10 Cusomters dataset from Block 1
# - Create a pandas DataFrame subset
# - Preview and verify top 10 customers by total sales
# ----------------------------------------------

import pandas as pd

# Step 1: Load dataset
df = pd.read_csv(r'day16_top10_customers/data/top10_customers.csv')

# Step 2 Validate top 10 customers by total sales
print(" Dataset loaded:")
print(df.info(),"\n")

# Preview first few rows
print(" Top 10 Customers Preview:")
print(df.head(10))

# Step 3: Additional checks / formatting
df['total_sales'] = df['total_sales'].round(2)
df_sorted = df.sort_values(by='total_sales', ascending=False)

# Step 4: Save verified subset
df_sorted.to_csv(r'day16_top10_customers/data/top10_customers_verified.csv', index=False)
print("\nExported: top10_customers_verified.csv")