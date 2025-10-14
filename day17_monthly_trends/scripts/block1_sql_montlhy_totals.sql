/*
    Block 1 - SQL ACTION: Monthly Totals Extraction
    Project: day17_monthly_totals
    Dataset: Superstore
    Author: blakusnaku
    Date: 10-15-2023
    ----------------------------------------------------------------
    GOAL: 
    - Extract monthly totals of sales, profit, orders, and quantity from the Superstore dataset.
*/


-- .open day17_monthly_totals/data/superstore.db
-- CREATE TABLE 
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    row_id TEXT,
    order_id TEXT,
    order_date TEXT,
    ship_date TEXT,
    ship_mode TEXT,
    customer_id TEXT,
    customer_name TEXT,
    segment TEXT,
    country TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    region TEXT,
    product_id TEXT,
    category TEXT,
    sub_category TEXT,
    product_name TEXT,
    sales REAL,
    quantity INTEGER,
    discount REAL,
    profit REAL
);


--
-- .mode csv
-- .import day17_monthly_totals/data/superstore.csv orders

-- Validate Data Load
SELECT COUNT(*) FROM orders;
SELECT * FROM orders LIMIT 5;

-- Extract Monthly Totals (Superstore Dataset)
SELECT
    STRFTIME('%Y-%m', order_date) AS month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_quantity
FROM orders
GROUP BY STRFTIME('%Y-%m', order_date)
ORDER BY month ASC;