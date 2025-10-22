/*===========================================================
📦 PROJECT METADATA
-----------------------------------------------------------
Day: 26
Date: 2025-10-26
Block: 1 — SQL SCHEMA CREATION
Task: Create Superstore schema and import cleaned dataset
Phase: BI Mastery — Superstore Capstone
Dataset: superstore_clean_stage2.csv
Tool: SQLite (VS Code)
Author: JP Malit
Repository: blakusnaku-100-days-of-data
File: scripts/superstore_schema.sql
===========================================================*/

DROP TABLE IF EXISTS superstore;
CREATE TABLE superstore (
    row_id INTEGER PRIMARY KEY,
    order_id TEXT,
    order_date DATE,
    ship_date DATE,
    ship_mode TEXT,
    customer_id TEXT,
    customer_name TEXT,
    segment TEXT,
    country TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    region TEXT,
    product_id TEXT,
    category TEXT,
    sub_category TEXT,
    product_name TEXT,
    sales REAL,
    quantity INTEGER,
    discount REAL,
    profit REAL
);
