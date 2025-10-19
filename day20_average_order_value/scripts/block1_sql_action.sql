/*
    Block 1 - SQL ACTION: COMPUTE AVERAGE ORDER VALUE PER CUSTOMER OR PER ORDER
    Project: day20_average_order_value
    Dataset: superstore
    Author: blakusnaku
    Date: 10-18-2025
    ----------------------------------------------------------------
    GOAL: Compute Average Order Value (AOV) using SQL.
*/

-- 1. read superstore_schema.sql to create the orders table and import data before running this script.

-- 2. AOV per Customer
SELECT
    customer_id,
    ROUND(SUM(sales)/COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM orders
GROUP BY customer_id
ORDER BY avg_order_value DESC;

-- 3. AOV for Entire Store
SELECT
    ROUND(SUM(sales) *1.0 / COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM orders;

-- 4. Check raw counts
SELECT
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(sales) AS total_sales
FROM orders;