-------------------------------------------------------------------
-- 📦 PROJECT METADATA
-------------------------------------------------------------------
-- Day: 44
-- Date: 2025-11-11
-- Process: str_analysis_schema.sql
-- Block: 1 - Create SQL schema for STR database
-- Phase: Data Analysis - Database Integration
-- Dataset: STR Market (InsideAirbnb)
-- Tools: SQL (QLite)
-- Author: JP Malit
-- Repository: blakusnaku-100-days-of-data
-------------------------------------------------------------------

-- Database Schema Definition

-- Drop tables if they already exist
DROP TABLE IF EXISTS listings;
DROP TABLE IF EXISTS calendar;
DROP TABLE IF EXISTS reviews;

-- 🧩 TABLE: listings

CREATE TABLE listings (
    listing_id              TEXT PRIMARY KEY,
    city_display            TEXT,
    property_type           TEXT,
    room_type               TEXT,
    price                   REAL,
    adr                     REAL,
    revpar                  REAL,
    occupancy_pct           REAL,
    los                     INTEGER,    
    review_scores_rating    REAL,
    beds                    REAL,
    bedrooms                REAL,
    bathrooms               REAL,
    latitude                REAL,
    longitude               REAL
);

-- 🧩 TABLE: calendar
-- // placeholder for daily pricing and availability (for future use)

CREATE TABLE calendar (
    calendar_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id              TEXT,
    date                    TEXT,
    availabile              TEXT,
    price                   REAL,
    adjusted_price          REAL,
    minimum_nights          INTEGER,
    maximum_nights          INTEGER,
    FOREIGN KEY (listing_id) REFERENCES listings(listing_id)
);

-- 🧩 TABLE: reviews
-- // placeholder for review-level data (future expansion)

CREATE TABLE reviews (
    review_id               INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id              TEXT, 
    reviewer_id             TEXT,
    reviewer_name           TEXT,
    date                    TEXT,
    comments                TEXT,
    FOREIGN KEY (listing_id) REFERENCES listings(listing_id)
);

-- ⚡ INDEXES 

CREATE INDEX IF NOT EXISTS idx_city_display ON listings(city_display);
CREATE INDEX IF NOT EXISTS idx_property_type ON listings(property_type);
CREATE INDEX IF NOT EXISTS idx_date ON calendar(date);
CREATE INDEX IF NOT EXISTS idx_listing_id_calendar ON calendar(listing_id);
CREATE INDEX IF NOT EXISTS idx_listing_id_reviews ON reviews(listing_id);
