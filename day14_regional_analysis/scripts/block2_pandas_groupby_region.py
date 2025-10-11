# Block 2: Group Data in Pandas
# Date: 2025-10-12
# Dataset: superstore.csv
# Description: Group by region to compute total, count and average sales.

import pandas as pd

# Load dataset (keep header row)
df = pd.read_csv(r"day14_regional_analysis/data/superstore.csv")

# CLean numeric columns
for col in ['sales','quantity','discount','profit']:
    df[col] = (
        df[col]
        .astype(str)                        #ensure all are strings first
        .str.replace(",","",regex=False)    #remove commas
        .str.strip()                        #remove spaces
        .astype(float)                      #convert to float
    )


# Preview first few rows
print(df.head())

# Group by region and calculate aggregates
regional_sales = (
    df.groupby('region')
        .agg(
            total_sales=('sales', 'sum'),
            num_orders=('order_id', 'count'),
            avg_order_value=('sales', 'mean')
        )
        .round(2)
        .reset_index()
        .sort_values('total_sales',ascending=False)
)

print("\nRgional Sales summary:")
print(regional_sales)

# Save the grouped result for Power BI
regional_sales.to_csv(r'day14_regional_analysis/data/regions_summary.csv',index=False)
