#
# BLOCK 2 - PYTHON ACTION: Add Calculated Profit Column
# Project: day15_profit
# Dataset: Superstore (orders)
# Author: blakusnaku
# Date: 2025-10-13
# ----------------------------------------------
# GOAL:
# - Load superstore dataset into pandas
# - Add profit_calc = sales * 0.4
# - Compare with actual profit column
# - Save new version for Power BI visualization
# ----------------------------------------------

import pandas as pd

# Step 1: Load dataset
df = pd.read_csv(r'day15_profit/data/superstore.csv')

# Step 2: CLean numeric columns
for col in ['sales','profit']:
    df[col] = (
        df[col]
        .astype(str)                        #ensure all are strings first
        .str.replace(",","",regex=False)    #remove commas
        .str.replace(r"[^\d.\-]", "", regex=True)  # drop currency/symbols if any
        .str.strip()                        #remove spaces
        .astype(float)                      #convert to float
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Optional: quick sanity check on parsing quality
null_report = {c: int(df[c].isna().sum()) for c in ["sales", "profit"]}
print("Nulls after cleaning:", null_report)

# Step 3: Add new claculated profit column (40% margin assumption)
df['profit_calc'] = df['sales'] * 0.4

# Step 4: Compare with actual profit column
df['diff'] = round(df['profit_calc'] - df['profit'],2)

# Step 5: Preview results
print(df[['sales','profit','profit_calc','diff']].head(10))

# Step 6: Save updated version for Power BI
df.to_csv(r'day15_profit/data/superstore_with_profit.csv', index=False)
print("\nExported: superstore_with_profit.csv")