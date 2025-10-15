################################################
# Block 1 - SQL ACTION: LEFT JOIN
#   Project: day18_left_join
#   Dataset: Mock data for orders and returns
#   Author: blakusnaku
#   Date: 10-16-2025
# ----------------------------------------------
# GOAL:Recreate the SQL LEFT JOIN between 'orders' and 'returns' tables
# using pandas.merge(), keeping all orders even if not returned.
################################################

import pandas as pd

# load data
orders = pd.read_csv(r'data/orders.csv')
returns = pd.read_csv(r'data/returns.csv')

# do left join
merged = pd.merge(
    orders,
    returns,
    how='left',
    on='order_id'   #join using the common key
)

# preview joined data
print(merged.head(10))

# analyz returned vs not returned
merged['status'] = merged['return_reason'].apply(
    lambda x: 'returned' if pd.notnull(x) else 'not returned'
)

summary = merged['status'].value_counts().reset_index()
summary.columns = ['status', 'count_orders']

print("\n Returned vs Not Returned:")
print(summary)

merged.to_csv(r'data/orders_returned_left_join.csv', index=False)
print("\n File saved: orders_returned_left_join.csv")