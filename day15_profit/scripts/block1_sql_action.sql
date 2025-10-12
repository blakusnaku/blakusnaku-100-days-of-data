/*
    Block 1 - SQL ACTION: Create Calculated Profit Column
    Project: day15_profit
    Dataset: Superstore
    Author: blakusnaku
    Date: 2025-10-13
    ----------------------------------------------------------------
    GOAL:
    - Load Superstore dataset
    - Add calculated profit column
    - Verify with preview query
*/

-- Step 1: import data
-- .mode csv
-- .import ../data/superstore_noheader.csv - superstore.csv 

-- Step 1: Check first few rows
-- SELECT * FROM orders LIMIT 5;

-- Step 2: Add new profit column
-- ALTER TABLE orders ADD COLUMN profit_calc REAL;

-- Step 3: Compute profit
-- Assuming cost ~ 60% of sales

UPDATE orders
SET profit_calc = sales - (sales * 0.6);

-- Step 4: Verify
SELECT 
    order_id, 
    sales, 
    profit_calc, 
    profit,
    ROUND(profit_calc - profit, 2) AS diff
FROM orders
LIMIT 10;