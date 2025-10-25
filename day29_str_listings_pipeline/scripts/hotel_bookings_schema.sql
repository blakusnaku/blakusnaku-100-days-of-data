-- USAGE GUIDE:
-- 1. Open SQLite:      sqlite3 
-- 2. Open Database:    .open data/hotel_bookings.db
-- 3. Load schema:      .read scripts/hotel_bookings_shema.sql
-- 4. Set CSV mode:     .mode csv
-- 5. Import data:      .import --skip 1 data/hotel_bookings_cleaned.csv hotel_bookings
-- 6. Confirm rows:     SELECT COUNT(*) AS total_rows FROM hotel_bookings;
-- 6. Confirm:          SELECT * FROM hotel_bookings LIMIT 5;

DROP TABLE IF EXISTS hotel_bookings;

CREATE TABLE hotel_bookings (
    hotel                       TEXT,
    is_canceled                 INTEGER,
    lead_time                   INTEGER,
    arrival_date_year           INTEGER,
    arrival_date_month          TEXT,
    arrival_date_week_number    INTEGER,
    arrival_date_day_of_month   INTEGER,
    stays_in_weekend_nights     INTEGER,
    stays_in_week_nights        INTEGER,
    adults                      INTEGER,
    children                    INTEGER,
    babies                      INTEGER,
    meal                        TEXT,
    country                     TEXT,
    market_segment              TEXT,
    distribution_channel        TEXT,
    is_repeated_guest           INTEGER,
    previous_cancellations      INTEGER,
    previous_bookings_not_canceled INTEGER,
    reserved_room_type          TEXT,
    assigned_room_type          TEXT,
    booking_changes             INTEGER,
    deposit_type                TEXT,
    agent                       TEXT,
    company                     TEXT,
    days_in_waiting_list        INTEGER,
    customer_type               TEXT,
    adr                         REAL,
    required_car_parking_spaces INTEGER,
    total_of_special_requests   INTEGER,
    reservation_status          TEXT,
    reservation_status_date     TEXT
);