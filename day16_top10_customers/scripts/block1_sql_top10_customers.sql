/*
    Block 1: SQL ACTION - Filter Top 10 Customers
    Project: day16_top10_customers
    Dataset: Superstore
    Author: blakusnaku
    Date: 10-14-2025 
    ----------------------------------------------------------------
    GOAL:
    - Query top 10 customers by total sales
    - Aggregte by Customer ID and Customer Name
    - Export result for Python subset analysis
*/

--- Query top 10 customers by total sales
SELECT
    [customer_id],
    [customer_name],
    ROUND(SUM(sales),2) AS total_sales
FROM orders
GROUP BY [customer_id], [customer_name]
ORDER BY total_sales DESC
LIMIT 10;