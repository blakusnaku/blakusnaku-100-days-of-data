----------------------------------------------
-- 📦 PROJECT METADATA
----------------------------------------------
-- Day: 39
-- Process: str_schema.sql
-- Purpose: Create full STR database schema (raw + clean + BI)
-- Author: JP Malit
-- Database: data/str_market.db
----------------------------------------------


/*===========================================================
  1. DROP TABLES (for testing or clean rebuild)
===========================================================*/

DROP TABLE IF EXISTS listings_raw;
DROP TABLE IF EXISTS calendar_raw;
DROP TABLE IF EXISTS reviews_raw;

DROP TABLE IF EXISTS listings;
DROP TABLE IF EXISTS calendar;
DROP TABLE IF EXISTS reviews;


/*===========================================================
  2. RAW TABLES (direct imports from CSV & parquet)
===========================================================*/

CREATE TABLE IF NOT EXISTS listings_raw (
    listing_id              INTEGER,
    city_display            TEXT,
    host_id                 INTEGER,
    host_name               TEXT,
    property_type           TEXT,
    room_type               TEXT,
    accomodates             INTEGER,
    bathrooms               REAL,
    bedrooms                INTEGER,
    beds                    INTEGER,
    amenities               TEXT,
    price                   REAL,
    minimum_nights          INTEGER,
    maximum_nights          INTEGER,
    review_scores_rating    REAL,
    number_of_reviews       INTEGER,
    latitude                REAL,
    longitude               REAL,
    availability_365        INTEGER,
    adr                     REAL,
    occupancy_pct           REAL,
    revpar                  REAL,
    los                     REAL,
    city_key                TEXT
);

CREATE TABLE IF NOT EXISTS calendar_raw (
    listing_id          INTEGER,
    date                TEXT,
    available           TEXT,
    price               REAL,
    adjusted_price      REAL,
    minimum_nights      INTEGER,
    maximum_nights      INTEGER,
    city_key            TEXT,
    city_display        TEXT
);

CREATE TABLE IF NOT EXISTS reviews_raw (
    review_id       INTEGER,
    listing_id      INTEGER,
    reviewer_id     INTEGER,
    reviewer_name   TEXT,
    comments        TEXT,
    date            TEXT,
    city_key        TEXT,
    city_display    TEXT
);


/*===========================================================
  3. CLEAN / BI-READY TABLES (after transformations)
===========================================================*/

CREATE TABLE IF NOT EXISTS listings (
    listing_id              INTEGER PRIMARY KEY,
    city_display            TEXT,
    property_type           TEXT,
    room_type               TEXT,
    price                   REAL,
    adr                     REAL,
    revpar                  REAL,
    occupancy_pct           REAL,
    los                     REAL,
    review_scores_rating    REAL,
    beds                    REAL,
    bedrooms                REAL,
    bathrooms               REAL,
    latitude                REAL,
    longitude               REAL
);

CREATE TABLE IF NOT EXISTS calendar (
    calendar_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id              INTEGER,
    date                    TEXT,
    available               TEXT,
    price                   REAL,
    adjusted_price          REAL,
    minimum_nights          INTEGER,
    maximum_nights          INTEGER
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id               INTEGER PRIMARY KEY,
    listing_id              INTEGER,
    reviewer_id             INTEGER,
    reviewer_name           TEXT,
    comments                TEXT,
    date                    TEXT
);


/*===========================================================
  4. INDEXES
===========================================================*/

CREATE INDEX IF NOT EXISTS idx_raw_calendar_listing_date
    ON calendar_raw(listing_id, date);

CREATE INDEX IF NOT EXISTS idx_raw_reviews_listing
    ON reviews_raw(listing_id);

CREATE INDEX IF NOT EXISTS idx_listings_city
    ON listings(city_display);

CREATE INDEX IF NOT EXISTS idx_calendar_listing
    ON calendar(listing_id);

CREATE INDEX IF NOT EXISTS idx_reviews_listing
    ON reviews(listing_id);
