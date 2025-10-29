-- STEP 1: Drop if exists (for re-runs)
DROP TABLE IF EXISTS calendar;

-- STEP 2: Create table
CREATE TABLE calendar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id INTEGER NOT NULL,
    date DATE NOT NULL,
    price REAL,
    available BOOLEAN
);

-- STEP 3: Generate sample data (SQLite-compatible version)
-- Simulates 3 listings over a 2-year range (2023-01-01 to 2024-12-31)

WITH RECURSIVE
date_gen AS (
  SELECT DATE('2023-01-01') AS date
  UNION ALL
  SELECT DATE(date, '+1 day')
  FROM date_gen
  WHERE date < DATE('2024-12-31')
),
listings AS (
  SELECT 10123 AS listing_id
  UNION ALL
  SELECT 10245
  UNION ALL
  SELECT 10367
)
INSERT INTO calendar (listing_id, date, price, available)
SELECT
  l.listing_id,
  d.date,
  ROUND(2000 + (RANDOM() % 1500), 2) AS price, -- ₱2000–₱3500 range
  CASE WHEN (RANDOM() % 10) < 8 THEN 1 ELSE 0 END -- 80% availability
FROM listings l
CROSS JOIN date_gen d;

-- STEP 4: Confirm data
SELECT COUNT(*) AS total_rows FROM calendar;
SELECT * FROM calendar LIMIT 10;