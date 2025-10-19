################################################
#    Block 2 - PYTHON ACTION: Export SQL View Results to CSV
#    Project: day21_data_pipeline_integration
#    Dataset: Superstore
#    Author: blakusnaku
#    Date: 10-19-2025
#    ----------------------------------------------------------------
#    GOAL:
#    To connect to the SQLite database, query the `superstore_cleaned` view,
#    and export its results as a clean CSV file (`superstore_cleaned.csv`)
#    for use in Power BI (Block 3).
#    Ensures ISO date format (YYYY-MM-DD) and consistent numeric formatting.
################################################

import sqlite3
import pandas as pd

# connect to the SQLite database
conn = sqlite3.connect(r'data/superstore.db')

# load data from the sql view
query = "SELECT * FROM superstore_cleaned;"
df = pd.read_sql_query(query, conn)

# clean column names for consistency
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# confirm the format before export
print("Preview of exported dataset:")
print(df.head())

# export to CSV (preserving ISO date format and numeric formatting)
df.to_csv(r'data/superstore_cleaned.csv', index=False, date_format='%Y-%m-%d', float_format='%.2f')

#close connection
conn.close()

print("\nExport complete! File saved as data/superstore_cleaned.csv") 
 