################################################
# BLOCK 2 - PYTHON ACTION: Boolean Mask in pandas
# Project: day19_filter_top_regions
# Dataset: superstore
# Author: blakusnaku
# Date: 10-17-2025
# ----------------------------------------------
# GOAL:Filter your DataFrame to show only rows where Region belongs to your top 2 regions (based on total sales). 
################################################

import pandas as pd

# 🧩 1️⃣ DATA LOADING & SAFETY CHECK
try:
    df = pd.read_csv("data/superstore.csv") 
    print("Data loaded successfully!")
    print("Shape:", df.shape)
    print("Preview:")
    print(df.head(), "\n")
except FileNotFoundError:
    print("File not found. Check the path or filename.")
    exit()
except Exception as e:
    print("Error while loading data:", e)
    exit()

# Clean and convert 'sales' to numeric
df['sales'] = (
    df['sales']
    .astype(str)            # Ensure it's string for replace
    .str.replace(',','')    # Remove commas
    .astype(float)          # Convert to float
)

# 🧮 2️⃣ ANALYSIS / TRANSFORMATION SECTION

# calculate total sales by region
region_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)
print("Total Sales by Region:")
print(region_sales, "\n")

# get top 2 region names
top_regions = region_sales.head(2).index
print("Top 2 Regions:", list(top_regions))

# apply boolean mask

filtered_df = df[df['region'].isin(top_regions)]
print("Filter applied. Shape:", filtered_df.shape)
print(filtered_df['region'].value_counts(), "\n")

# verify totals
print("Verifying totals match SQL output:")
print(filtered_df.groupby('region')['sales'].sum())

# 🎯 3️⃣ EXPORT OR VISUALIZATION PREP

# export filtered data for power bi next block
filtered_df.to_csv("data/top_regions_filtered.csv", index=False)
print("Saved filtered dataset to data/top_regions_filtered.csv")

# 📘 Notes:
# - Always verify df.head() after loading.
# - Keep print() checkpoints for traceability.
# - Save outputs into the /data/ folder for Power BI or next block.