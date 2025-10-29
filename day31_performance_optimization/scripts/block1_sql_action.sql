-------------------------------------------------
-- PROJECT METADATA
-------------------------------------------------
-- DAY: 31
-- DATE: 2025-10-29
-- BLOCK: 1 - SQL Action
-- TASK: Optimize STR queries with indexes on listing_id and date
-- PHASE: STR Dtaset - STR Pipeline Flow
-- TOOL: SQL (SQLite)
-- AUTHOR: JP Malit
-- REPO: blakusnaku-100-days-of-data
-- FILE: scripts/block1_sql_action.sql
-------------------------------------------------
-- GOAL:
--  Evaluate query performance before and after applying indexes on
--  `listing_id` in the STR dataset. Measure exectuion time using 
--  `EXPLAIN ANALYZE` to confirm optimization impact.
-- PIPELINE FLOW:
--  1. run baseline query (no index) and record execution time.
--  2. create indexes on `listing_id` and `date`.
--  3. re-run the same query with `EXPLAIN ANALYZE`.
--  4. compare query plan and runtime differences.
--  5. document findings in block4_learning_log.md.
-------------------------------------------------
-- NOTES:
--  - enuse the table used (`calendar` or `listings`) has sufficient rows to reflect
--      measureable difference
--  - for sqlite, use `EXPLAIN QUERY PLAN` since `ANALYZE` behaves differently.
--  - for PostgreSQL, `EXPLAIN ANALYZE` gives actual timing data.
-------------------------------------------------

-- step 1: view sample structure
PRAGMA table_info(calendar);

-- step 2: baseline query (without index)
EXPLAIN QUERY PLAN
SELECT listing_id, date, price
FROM calendar
WHERE listing_id = 10123
    AND date BETWEEN '2023-01-01' AND '2023-01-31';

-- step 3: create index
CREATE INDEX idx_calendar_listing_id ON calendar(listing_id);
CREATE INDEX idx_calendar_date ON calendar(date);

-- run baseline query (no index)
DROP INDEX IF EXISTS idx_calendar_listing_id;
DROP INDEX IF EXISTS idx_calendar_date;
DROP INDEX IF EXISTS idx_calendar_listing_date;

SELECT listing_id, date, price
FROM calendar
WHERE listing_id = 10123
  AND date BETWEEN '2023-01-01' AND '2023-01-31';
-- Run Time: real 0.045 user 0.000000 sys 0.000000

-- create index for listing_id
CREATE INDEX idx_calendar_listing_date ON calendar(listing_id, date);

SELECT listing_id, date, price
FROM calendar
WHERE listing_id = 10123
  AND date BETWEEN '2023-01-01' AND '2023-01-31';
-- Run Time: real 0.030 user 0.000000 sys 0.000000