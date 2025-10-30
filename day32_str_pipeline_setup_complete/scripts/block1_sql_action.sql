------------------------------------------
-- PROJECT METADATA
------------------------------------------
-- Day: 32
-- Date: 2025-10-30
-- Block: 1 - SQL Action
-- Task: Create final cleaned STR dataset (merged listings + calendar)
-- Phase: STR Pipeline Flow
-- Dataset: STR (listings.csv, calendar.csv)
-- Tool: SQlite
-- Author: JP Malit
-- Repository: blakusnaku-100-days-of-data
-- File: scripts/block1_sql_action.sql
------------------------------------------
-- GOAL:
--  Merge listings and calendar data to produce a clean, unified dataset
--      'clean_final' that will serve as the foundation for STR performance analysis
--
-- PIPELINE FLOW:
--  listings + calendar -> join on listings_id -> filter valid prices & dates -> save as clean_final
--
-- NOTES:
--  - Ensure data types are consistent (`REAL` for numeric, `TEXT` for IDs/dates)
--  - Remove reows with null or zero `price`
--  - Filter out invalid date ranges (future > 2025 or malformed)
------------------------------------------

-- Clean listings table
CREATE TABLE listings_clean as
SELECT
    listing_id,
    host_id,
    neighbourhood,
    room_type,
    accommodates,
    CAST(REPLACE(REPLACE(price,'$',''),',','') AS REAL) AS price
FROM listings
WHERE listing_id IS NOT NULL
    AND price IS NOT NULL
    AND TRIM(price) != '';

-- Clean calendar table
CREATE TABLE calendar_clean AS
SELECT
    listing_id,
    date,
    CAST(REPLACE(REPLACE(price,'$',''),',','') AS REAL) AS price,
    available,
    minimum_nights,
    maximum_nights
FROM calendar
WHERE listing_id IS NOT NULL
    AND price IS NOT NULL
    AND TRIM(price) != '';

SELECT COUNT(*) AS listings_clean_rows FROM listings_clean;
SELECT COUNT(*) AS calendar_clean_rows FROM calendar_clean;

-- CREATE clean_final
-- Drop old version if it exists
DROP TABLE IF EXISTS clean_final;

-- Merge listings and calendar data
CREATE TABLE clean_final AS
SELECT
    c.listing_id,
    l.host_id,
    l.neighbourhood,
    l.room_type,
    l.accommodates,
    l.price AS base_price,
    c.date,
    c.price AS daily_price,
    c.available,
    c.minimum_nights,
    c.maximum_nights
FROM calendar_clean AS c
LEFT JOIN listings_clean AS l
    ON c.listing_id = l.listing_id
WHERE c.price IS NOT NULL
    AND c.price > 0
    AND date(c.date) BETWEEN date('2025-01-01') AND date('2025-12-31');

-- Quick Validation
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT listing_id) AS total_listings
FROM clean_final;

-- Preview top rows
SELECT * FROM clean_final LIMIT 10;