/*===========================================================
📦 PROJECT METADATA
-----------------------------------------------------------
Day: 28
Date: 2025-10-26
Block: 1 — SQL ACTION
Task: Test YEAR() and MONTH() functions using booking_date
Phase: STR Analytics Phase
Dataset: hotel_bookings.csv
Tool: SQL (SQLite)
Author: JP Malit
Repository: blakusnaku-100-days-of-data
File: scripts/block1_sql_action.sql
===========================================================

🎯 GOAL: Extract year and month component from booking_date to prepare for time-based grouping and seasonal analysis.

🔁 PIPELINE FLOW: 
hotel_bookings.csv (raw data)
    -> SQL date extraction
    -> derived columns (year, month)
    
📘 NOTES:
    -> SQLite used STRFTIME('%Y', date_column) and STRFTIME('%m', date_column) for extraction.
    -> Ensure booking_date is in 'YYYY-MM-DD' format (did during examination phase in Excel)

===========================================================*/

--1. preview data sample
SELECT 
    hotel,
    reservation_status_date AS booking_date
FROM str_reservations
LIMIT 5;

--2. extract year and month from booking_date
SELECT
    hotel,
    reservation_status_date AS booking_date,
    STRFTIME('%Y', reservation_status_date) AS booking_year,
    STRFTIME('%m', reservation_status_date) AS booking_month
FROM str_reservations
LIMIT 10;

--3. verify year distribution
SELECT
    STRFTIME('%Y', reservation_status_date) AS booking_year,
    COUNT(*) AS total_bookings
FROM str_reservations
GROUP BY booking_year
ORDER BY booking_year;

--4. check for nulls or invalid dates
SELECT
    COUNT(*) AS null_dates
FROM str_reservations
WHERE reservation_status_date IS NULL
   OR reservation_status_date = '';