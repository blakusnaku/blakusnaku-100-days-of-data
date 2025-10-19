################################################
# BLOCK 2 - PYTHON ACTION: Average Order Value
# Project: day20_average_order_value
# Dataset: superstore
# Author: blakusnaku
# Date: 10-18-2025
# ----------------------------------------------
# GOAL:
################################################

import pandas as pd

# 🧩 1️⃣ DATA LOADING & SAFETY CHECK
try:
    # Change this path per project
    df = pd.read_csv("data/superstore.csv")  # or pd.read_excel("Superstore.xlsx")
    #print("✅ Data loaded successfully!")
    #print("Shape:", df.shape)
    #print("Preview:")
    #print(df.head(), "\n")
except FileNotFoundError:
    #print("❌ File not found. Check the path or filename.")
    exit()
except Exception as e:
    #print("⚠️ Error while loading data:", e)
    exit()

# 🧮 2️⃣ ANALYSIS / TRANSFORMATION SECTION  

## 1. Clean numberic columns
df['sales'] = (
    df['sales']
    .astype(str)               # ensure string type
    .str.replace(',', '', regex=True)  # remove commas
    .astype(float)             # convert to float
)


print("Total rows:", len(df))
print("Unique orders:", df['order_id'].nunique())
print("Total sales:", df['sales'].sum())

## 1. Compute overall AOV
order_sales = df.groupby('order_id', as_index=False)['sales'].sum()
aov_overall = round(order_sales['sales'].mean(), 2)
 
## 2. Compute AOV per Customer
aov_per_customer = (
    df.groupby(['customer_id', 'order_id'], as_index=False)['sales'].sum()
      .groupby('customer_id')['sales'].mean()
      .reset_index(name='avg_order_value')
      .sort_values(by='avg_order_value', ascending=False)
)

# 🎯 3️⃣ EXPORT OR VISUALIZATION PREP 

# Export cleaned data for Power BI
aov_per_customer.to_csv(r'data/aov_per_customer.csv', index=False)

# 📘 Notes:
# - Always verify df.head() after loading.
# - Keep print() checkpoints for traceability.
# - Save outputs into the /data/ folder for Power BI or next block.
