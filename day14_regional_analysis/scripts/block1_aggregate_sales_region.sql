-- Block 1: Aggregate Sales by Region
-- Date: 2025-10-12
-- Dataset: superstore.db (orders table)
-- Description: Calculate total, average, and count of orders by region.


-- Preview the dataset
SELECT * FROM orders LIMIT 5;

-- Aggregate total sales by region
SELECT region,
    SUM(sales) AS total_sales,
    COUNT(order_id) AS num_orders,
    ROUND(AVG(sales), 2) AS avg_order_value
FROM orders
GROUP BY region
ORDER BY total_sales DESC;

--check total rows to confirm integrity
SELECT COUNT(*) FROM orders;