# Read both CSV files (orders and customers) into pandas.
# Merge them so each order shows its customer name, region and email.
# Keep all orders even if a customer is missing - that's a LEFT JOIN in SQL

# Block 2 - Replicate SQL Join in pandas
# Combine Orders and Custoemrs into on dataframe using a LEFT JOIN Logic.

import pandas as pd

#Step 1. Load the CSV files
orders = pd.read_csv("day13_sql/orders.csv")
customers = pd.read_csv("day13_sql/customers.csv")

#Step 2. Merge (JOIN) the two Dataframes
# how = 'Left' means keep all rows from orders (Left table) even if no matching customer exsists
merged_df = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="left"
)

#Step 3. View first few rows
print(merged_df.head())

#Step 4. Save the merged dataset for the next block (Power BI)
merged_df.to_csv("day13_sql/orders_customers_joined_pandas.csv", index=False)

# ##Reflection
# This panda merge does the same as SQL LEFT JOIN.
# It keeps all orders and fills customer details where available.
# 