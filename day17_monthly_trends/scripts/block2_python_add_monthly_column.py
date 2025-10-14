################################################
# BLOCK 2 - PYTHON ACTION: Add monthly column
# Project: day17_monthly_trends
# Dataset: monthly_totals_raw.csv (extracted from Superstore dataset)
# Author: blakusnaku
# Date: 2025-10-15
# ----------------------------------------------
# GOAL:
# - Load monthly totals extracted from SQL (Block 1)
# - Convert 'month' column to datetime format
# - Create additional columns: month_name and year
# - Export cleaned dataset for Power BI visualization
################################################

import pandas as pd

# 1 Load data from Block 1
df = pd.read_csv(r'day17_monthly_totals/data/monthly_totals_raw.csv')

# 2 Convert 'month' column to datetime format 
df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

# 3 Create additional columns for analysis and visualization
df['month_name'] = df['month'].dt.strftime('%B')  # Full month name
df['year'] = df['month'].dt.year  # Year as integer

# 4 Reorder columns for better readability
df = df[['year','month','month_name','total_sales','total_profit','total_orders','total_quantity']]

# 5 Export cleaned dataset for Power BI
df.to_csv(r'day17_monthly_totals/data/monthly_totals_clean.csv', index=False, encoding='utf-8')

print("Monthly totals with additional columns saved to 'monthly_totals_clean.csv'")
print(df.head())