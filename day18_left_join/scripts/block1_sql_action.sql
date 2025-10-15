/*
    Block 1 - SQL ACTION: LEFT JOIN
    Project: day18_left_join
    Dataset: Mock data for orders and returns
    Author: blakusnaku
    Date: 10-16-2025
    ----------------------------------------------------------------
    GOAL: Demonstrate the behavior of LEFT JOIN between 'orders' and 'returns'
    tables, showing all orders while including return info (if available).
*/

-- Create Orders Table
CREATE TABLE orders(
    order_id TEXT PRIMARY KEY,
    customer_name TEXT,
    order_date TEXT,
    region TEXT,
    SALES REAL
);

-- Create Returns Table
CREATE TABLE returns(
    return_id TEXT PRIMARY KEY,
    order_id TEXT,
    return_date TEXT,
    return_reason TEXT
);

-- LEFT JOIN: combine all orders with their return info
SELECT
    o.order_id,
    o.customer_name,
    o.order_date,
    o.sales,
    r.return_reason
FROM orders AS o
LEFT JOIN returns AS r
    ON o.order_id = r.order_id
ORDER BY o.order_id;

-- CHECK TOTAL RETURNED VS NOT RETURNED
SELECT
    CASE
        WHEN r.order_id IS NULL THEN 'not returned'
        ELSE 'returned'
    END AS status,
    COUNT(*) AS count_orders
FROM orders AS o
LEFT JOIN returns AS r
    ON o.order_id = r.order_id
GROUP BY status;