----------------------------------------------------------
--  Block 1 — SQL ACTION : SQL JOINS CHEATSHEET
--  Project: day21_multi_table_model
--  Dataset: superstore (orders, returns, shipping_cost)
--  Author: blakusnaku
--  Date: 10-20-2025
----------------------------------------------------------
--  GOAL:
--  Create a comprehensive JOINs cheatsheet demonstrating
--  how multiple tables can be combined using SQL joins.
----------------------------------------------------------


---------------------------------------------------------
-- 🧩 1. INNER JOIN
-- Returns only records that have matching values in both tables
---------------------------------------------------------
SELECT 
    o.order_id,
    o.customer_id,
    r.return_reason
FROM orders o
INNER JOIN returns r 
    ON o.order_id = r.order_id;

---------------------------------------------------------
-- 🧩 2. LEFT JOIN
-- Returns all records from the left table (orders),
-- and matched records from the right table (returns).
---------------------------------------------------------
SELECT 
    o.order_id,
    o.customer_id,
    r.return_reason
FROM orders o
LEFT JOIN returns r 
    ON o.order_id = r.order_id;

---------------------------------------------------------
-- 🧩 3. RIGHT JOIN
-- Returns all records from the right table (returns),
-- and matched records from the left table (orders).
---------------------------------------------------------
SELECT 
    o.order_id,
    o.customer_id,
    r.return_reason
FROM orders o
RIGHT JOIN returns r 
    ON o.order_id = r.order_id;

---------------------------------------------------------
-- 🧩 4. FULL OUTER JOIN
-- Returns all records when there is a match in either left or right table.
---------------------------------------------------------
SELECT 
    o.order_id,
    o.customer_id,
    r.return_reason
FROM orders o
FULL OUTER JOIN returns r 
    ON o.order_id = r.order_id;

---------------------------------------------------------
-- 🧩 5. CROSS JOIN
-- Returns the Cartesian product (every combination) of two tables.
---------------------------------------------------------
SELECT 
    o.order_id,
    s.ship_mode
FROM orders o
CROSS JOIN shipping_cost s;

---------------------------------------------------------
-- 🧩 6. SELF JOIN
-- Joins a table to itself (useful for hierarchical or comparison logic)
---------------------------------------------------------
SELECT 
    a.order_id AS order_a,
    b.order_id AS order_b,
    a.customer_id
FROM orders a
INNER JOIN orders b
    ON a.customer_id = b.customer_id
WHERE a.order_id <> b.order_id;

/*
| JOIN Type | Description               | Rows Returned     |
|-----------|---------------------------|-------------------|
| INNER     | Only matching keys        | Matches only      |
| LEFT      | All from left + matches   | Left + matched    |
| RIGHT     | All from right + matches  | Right + matched   |
| FULL      | All from both             | Everything        |
| CROSS     | All combinations          | Cartesian product |
| SELF      | Table joins itself        | Context-based     |
*/
