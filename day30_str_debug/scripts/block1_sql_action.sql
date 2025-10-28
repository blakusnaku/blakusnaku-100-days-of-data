/*===========================================================
📦 PROJECT METADATA
-----------------------------------------------------------
Day: 30
Date: 2025-10-28
Block: 1 — SQL ACTION
Task: Review and join STR dummy tables (listings + calendar)
Phase: STR Debug Series
Dataset: listings_raw.csv, calendar_raw.csv
Tool: SQLite
Author: JP Malit
Repository: blakusnaku-100-days-of-data
File: scripts/block1_sql_action.sql
===========================================================

🎯 GOAL: Practice clean joins, verify key consistency (listings_id), and prep for Python merge debugging.

🔁 PIPELINE FLOW:
1 Load and inspect base tables
2 Run join test on listing_id
3 Check for nulls or mismatched rows
4 Create a joined table for Block 2 

===========================================================*/

-- create tables
CREATE TABLE listings (
    listing_id INTEGER PRIMARY KEY,
    property_name TEXT,
    city TEXT,
    room_type TEXT,
    price REAL,
    host_id TEXT
);

CREATE TABLE calendar (
    listing_id INTEGER,
    date TEXT,
    available TEXT,
    price REAL,
    adr REAL,
    occupancy REAL
);

-- quick sanity check
SELECT COUNT(*) AS listings_count FROM listings;
SELECT COUNT(*) AS calendar_count FROM calendar;

-- verify key integrity
SELECT DISTINCT listing_id
FROM calendar
WHERE listing_id NOT IN (SELECT listing_id FROM listings)

--- perform the join a
CREATE TABLE listings_calendar_joined AS
SELECT
    l.listing_id,
    l.property_name,
    l.city,
    l.room_type,
    c.date,
    c.available,
    c.price AS calendar_price,
    c.adr,
    c.occupancy
FROM listings AS l
LEFT JOIN calendar AS c
    ON l.listing_id = c.listing_id
ORDER BY l.listing_id, c.date;
