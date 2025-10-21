################################################
# BLOCK 2 - PYTHON ACTION: 
# Project: day21_multi_table_model
# Dataset: orders,returns,shipping_cost
# Author: blakusnaku
# Date: 10-20-2025
# ----------------------------------------------
# GOAL:Recreate SQL joins using pandas merges with 3 tables.
################################################

import pandas as pd
import sqlite3

# COnnect to your existing database   
conn = sqlite3.connect(r'data/orders.db')

# Load the three tables
orders = pd.read_sql_query("SELECT * FROM orders", conn)
shipping = pd.read_sql_query("SELECT * FROM shipping_cost", conn)
returns = pd.read_sql_query("SELECT * FROM returns", conn)

# Close the connection
conn.close()

#Preview the data
print("Orders:",orders.shape)
print("Shipping:",shipping.shape)
print("Returns:",returns.shape)

# inner join - orders + returns
inner_merge = pd.merge(orders, returns, on='order_id', how='inner')
print(inner_merge.head())
print("Rows:", len(inner_merge))

# left join - orders + returns
left_merge = pd.merge(orders, returns, on='order_id', how='left')
print(left_merge.head())
print("Rows:", len(left_merge))

# left join - orders + shipping
orders_shipping = pd.merge(orders, shipping, on='order_id', how='left')
print(orders_shipping.head())

# multi-table merge - orders + shipping + returns
merged_all = (
    orders
    .merge(shipping, on='order_id', how='left')
    .merge(returns, on='order_id', how='left')
)

print(merged_all.head(10))
print("Final shape:", merged_all.shape)

merged_all.to_csv(r'data/merged_orders.csv', index=False)
print("✅ Merged dataset saved to ../data/merged_orders.csv")

orders.to_csv(r'data/orders.csv', index=False)
shipping.to_csv(r'data/shipping_cost.csv', index=False)
returns.to_csv(r'data/returns.csv', index=False)
