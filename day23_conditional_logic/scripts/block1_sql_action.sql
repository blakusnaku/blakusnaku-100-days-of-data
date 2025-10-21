/*
===========================================================
📦 PROJECT METADATA
-----------------------------------------------------------
Day: 23
Date: 2025-10-21
Block: 1 — SQL ACTION
Task: Query data with CASE statements
Phase: SQL Fundamentals
Dataset: superstore
Tool: SQLite
Author: JP Malit
Repository: blakusnaku-100-days-of-data
File: scripts/block1_sql_action.sql
===========================================================

🎯 GOAL:
Use CASE statements to classify orders based on sales value.
Apply conditional logic to label each order as 'High Value',
'Medium Value', or 'Low Value'.

🔁 PIPELINE FLOW:
SQL → Python (np.where) → Power BI (category filter) → GitHub Reflection

📘 NOTES:
- Demonstrates row-level conditional logic.
- Bridges SQL → Python → Power BI logic consistency.
- Output will feed into later blocks for visual and analytical comparison.

===========================================================
*/

SELECT
    order_id,
    customer_name,
    region,
    sales,
    CASE
        WHEN sales >= 500 THEN 'High Value'
        WHEN sales BETWEEN 200 AND 499 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS sales_category
FROM orders
ORDER BY sales DESC;
