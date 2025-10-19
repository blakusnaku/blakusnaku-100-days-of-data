-- USAGE GUIDE:
-- 1. Open SQLite:      sqlite3
-- 2. Open database:    .open data/superstore.db
-- 3. Load schema:      .read scripts/superstore_schema.sql
-- 4. Set CSV mode:     .mode csv
-- 5. Import data:      .import --skip 1 data/superstore.csv orders
-- 6. Confirm:          SELECT * FROM orders LIMIT 5;

-- (If your SQLite version doesn’t support --skip 1,
-- manually remove the header row before importing.)

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    row_id INTEGER,
    order_id TEXT,
    order_date TEXT,
    ship_date TEXT,
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
