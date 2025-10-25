/*===========================================================
📦 PROJECT METADATA
-----------------------------------------------------------
Day: 29
Date: 2025-10-27
Block: 1 — SQL ACTION
Task: Export hotel bookings snapshot with LIMIT
Phase: STR Analytics Transition
Dataset: hotel_bookings_cleaned.csv
Tool: SQLite
Author: JP Malit
Repository: blakusnaku-100-days-of-data
File: scripts/block1_sql_action.sql
===========================================================

🎯 GOAL: Export a manageable snapshot of cleaned_hotel_bookings dataset to be used for Power BI model testing and schema validation

🔁 PIPELINE FLOW:
SQL (extract) -> Python (prep and merge) -> Power BI (visualize)

📘 NOTES:
using LIMIT ensures we test smaller subsets before importing large files

===========================================================*/

-- step 1: run hotel_bookings_schema.sql to create hotel_bookings table

-- step 2: export a 10-record sample
SELECT *
FROM hotel_bookings
LIMIT 10;

-- step 3: export highest ADR values (top 10)
SELECT *
FROM hotel_bookings
ORDER BY adr DESC
LIMIT 10;

-- step 4: export subset for a specific hotel type
SELECT *
FROM hotel_bookings
WHERE hotel = 'Resort Hotel'
LIMIT 10;

-- step 5: export as CSV
-- .headers on
-- .mode csv
-- .output data/hotel_bookings_snapshot.csv
-- SELECT * FROM hotel_bookings LIMIT 10;
-- .output stdout