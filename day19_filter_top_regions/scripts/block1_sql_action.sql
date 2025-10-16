/*
    Block 1 - SQL ACTION: TOP REGIONS USING SUBQUERIES
    Project: day19_filter_top_regions
    Dataset: superstore
    Author: blakusnaku
    Date: 10-17-2025
    ----------------------------------------------------------------
    GOAL: USE SUBQUERIES TO FILTER TOP REGIONS
*/

-- step 1: run the schema to create the table
--  .read scripts/superstore_schema.sql

-- step 2: import the data into the table and validate
--  .mode csv
--  .import --skip 1 data/superstore.csv orders

-- step 3: confirm the data is loaded
SELECT COUNT(*) FROM orders;
SELECT DISTINCT region FROM orders;

-- step 4: subquery for top 2 regions
SELECT region, SUM(sales) AS total_sales
FROM orders
WHERE region IN (
    SELECT region
    FROM (
        SELECT region, SUM(sales) AS total_sales
        FROM orders
        GROUP BY region
        ORDER BY total_sales DESC
        LIMIT 2
    ) AS top_regions
)
GROUP BY region
ORDER BY total_sales DESC;