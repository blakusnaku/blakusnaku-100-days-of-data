/*
    Block 1 - SQL ACTION: Create View for Cleaned Dataset
    Project: day21_data_pipeline_integration
    Dataset: Superstore 
    Author: blakusnaku
    Date: 10-19-2025
    ----------------------------------------------------------------
    GOAL: To create a reusable SQL VIEW (`superstore_cleaned`) that serves as
    the standardized, cleaned version of the Superstore dataset.
    This view will:
      - Strip commas from numeric fields (sales, profit)
      - Ensure proper data types for analysis
      - Exclude null or invalid records
    The view will be used by Python for CSV export (Block 2) and
    Power BI for refreshed visualization (Block 3).
*/

--Create VIEW for Cleaned Superstore Data
DROP VIEW IF EXISTS superstore_cleaned;
CREATE VIEW superstore_cleaned AS
SELECT
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region,
    product_id,
    category,
    sub_category,
    product_name,
    CAST(REPLACE(sales, ',', '') AS REAL) AS sales,
    quantity,
    discount,
    CAST(REPLACE(profit, ',', '') AS REAL) AS profit
FROM orders
WHERE order_id IS NOT NULL
  AND sales IS NOT NULL
  AND profit IS NOT NULL;

-- Test the VIEW
SELECT * FROM superstore_cleaned LIMIT 10;
