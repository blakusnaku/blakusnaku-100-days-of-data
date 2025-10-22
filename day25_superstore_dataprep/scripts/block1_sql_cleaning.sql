/*===========================================================
📦 PROJECT METADATA
-----------------------------------------------------------
Day: 25
Date: 2025-10-25
Block: 1 — SQL CLEANING & VALIDATION
Task: Import and validate cleaned Superstore dataset
Phase: BI Mastery — Superstore Capstone
Dataset: superstore_clean_stage1.csv
Tool: SQLite via VS Code (SQLTools / SQLite extension)
Author: JP Malit
Repository: blakusnaku-100-days-of-data
File: scripts/block1_sql_cleaning.sql
===========================================================

🎯 GOAL:
Import the cleaned Superstore dataset into SQLite (executed in VS Code) 
and perform structural and logical validation to ensure consistency 
with Excel cleaning results before proceeding to Python and Power BI integration.

🔁 PIPELINE FLOW:
Excel (cleaned) → SQL (validated) → Python → Power BI

📘 NOTES:
This SQL validation confirms data readiness for integration by checking:
- Schema structure and column data types
- Record count and null values
- Logical integrity between date and regional fields
- Duplicates and unique row identifiers
===========================================================*/


-- ==========================================================
-- 1️⃣ CREATE TABLE STRUCTURE
-- ==========================================================

DROP TABLE IF EXISTS superstore;
CREATE TABLE superstore (
    row_id INTEGER PRIMARY KEY,
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

-- ==========================================================
-- 2️⃣ IMPORT CLEANED DATA (VS CODE / SQLITE CLI)
-- ==========================================================
-- In VS Code terminal:
--   .mode csv
--   .import data/superstore_clean_stage1.csv superstore
--
-- Confirm the import using:
--   SELECT COUNT(*) FROM superstore;

-- ==========================================================
-- 3️⃣ VALIDATION QUERIES
-- ==========================================================

-- ✅ Check record count
SELECT COUNT(*) AS total_records FROM superstore;

-- ✅ Check for nulls in key fields
SELECT *
FROM superstore
WHERE order_id IS NULL
   OR sales IS NULL
   OR profit IS NULL
   OR order_date IS NULL
   OR customer_id IS NULL;

-- ✅ Validate date logic (ship_date should not be earlier than order_date)
SELECT order_id, order_date, ship_date
FROM superstore
WHERE ship_date < order_date;

-- ✅ Verify numeric columns are all positive (optional)
-- (Negative profit values are valid and indicate loss transactions)
SELECT *
FROM superstore
WHERE sales < 0 OR profit < 0 OR quantity <= 0;

-- ✅ Validate state and region consistency
SELECT DISTINCT region, state
FROM superstore
ORDER BY region, state;

-- ✅ Detect duplicates in order_id
SELECT order_id, COUNT(*) AS count
FROM superstore
GROUP BY order_id
HAVING COUNT(*) > 1;

-- ✅ Check unique row_id
SELECT COUNT(DISTINCT row_id) AS unique_rows,
       COUNT(*) AS total_rows
FROM superstore;

-- ✅ Review summary stats for sanity check
SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(discount), 2) AS avg_discount,
    COUNT(DISTINCT customer_id) AS total_customers
FROM superstore;

-- ✅ Verify all postal codes are 5 characters long
SELECT DISTINCT postal_code
FROM superstore
WHERE LENGTH(postal_code) != 5;

-- ==========================================================
-- 4️⃣ FINDINGS NOTE
-- ==========================================================
-- Query Result: Negative Profit Validation
-- ----------------------------------------------------------
--   SELECT * FROM superstore
--   WHERE sales < 0 OR profit < 0 OR quantity <= 0;
--
-- Observation:
--   Several rows returned where profit < 0,
--   confirming legitimate loss transactions within the Superstore data.
--   These were retained intentionally to preserve business realism.

-- Query Result: Duplicate Order Validation
-- ----------------------------------------------------------
--   SELECT order_id, COUNT(*) AS count
--   FROM superstore
--   GROUP BY order_id
--   HAVING COUNT(*) > 1;
--
-- Observation:
--   Returned multiple order IDs appearing more than once.
--   ✅ Confirmed valid behavior — represents customers purchasing multiple
--   products under a single order. Each row corresponds to a line item.

-- ==========================================================
-- 5️⃣ EXPORT: CLEAN VERIFIED DATASET
-- ==========================================================
-- After validation, export verified dataset via VS Code terminal:
--   .headers on
--   .mode csv
--   .output data/superstore_clean_final.csv
--   SELECT * FROM superstore;
--   .output stdout