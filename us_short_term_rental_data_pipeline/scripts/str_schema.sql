----------------------------------------------
-- 📦 PROJECT METADATA
----------------------------------------------
-- Day: 39
-- Date: 2025-11-06
-- Process: str_schema.sql
-- Task: Define STR database structure and relationships
-- Phase: Data Acquisition - Database Creation
-- Author: JP Malit
-- Repository: blakusnaku-100-days-of-data
-- Database: data/str_market.db
----------------------------------------------

-- Drop existings tables (for testing runs)
DROP TABLE IF EXISTS listings;
DROP TABLE IF EXISTS calendar;
DROP TABLE IF EXISTS reviews;

-----------------------
-- TABLE: listings
-----------------------
CREATE TABLE IF NOT EXISTS listings (
    listing_id              INTEGER PRIMARY KEY,
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
    number_of_reviewa       INTEGER,
    latitude                REAL,
    longtitude              REAL,
    availability_365        INTEGER,
    adr                     REAL,
    occupancy_pct           REAL,
    revpar                  REAL,
    los                     REAL,
    city_key                TEXT
);

-----------------------
-- TABLE: calendar
-----------------------
CREATE TABLE IF NOT EXISTS calendar (
    listing_id                  INTEGER,
    date                        DATE,
    available                   TEXT,
    price                       REAL,
    adjusted_price              REAL,
    minimum_nights              INTEGER,
    maximum_nights              INTEGER,
    city_key                    TEXT,
    city_display                TEXT,
    FOREIGN KEY (listing_id)    REFERENCES listings(listing_id)
);

-----------------------
-- TABLE: reviews
-----------------------
CREATE TABLE IF NOT EXISTS reviews (
    review_id                   INTEGER PRIMARY KEY,
    listing_id                  INTEGER,
    reviewer_id                 INTEGER,
    reviewer_name               TEXT,
    comments                    TEXT,
    date                        DATE,
    city_key                    TEXT,
    city_display                TEXT,
    FOREIGN KEY (listing_id)    REFERENCES listings(listing_id)
);


-----------------------
-- INDEXES
-----------------------
CREATE INDEX IF NOT EXISTS idx_calendar_listing_date
    ON calendar(listing_id,date);

CREATE INDEX IF NOT EXISTS idx_reviews_listing
    ON reviews(listing_id);
 