-- USAGE GUIDE:
-- 1. Open SQLite:  sqlite3 superstore.db
-- 2. Load schema:  .read scripts/superstore_schema.sql
-- 3. Set CSV mode: .mode csv
-- 4. Import data:  .import --skip 1 data/superstore.csv orders
-- 5. Confirm:      SELECT * FROM orders LIMIT 5;

-- (If your SQLite version doesn’t support --skip 1,
-- manually remove the header row before importing.)

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    Row_ID INTEGER,
    Order_ID TEXT,
    Order_Date TEXT,
    Ship_Date TEXT,
    Ship_Mode TEXT,
    Customer_ID TEXT,
    Customer_Name TEXT,
    Segment TEXT,
    Country TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT,
    Region TEXT,
    Product_ID TEXT,
    Category TEXT,
    Sub_Category TEXT,
    Product_Name TEXT,
    Sales REAL,
    Quantity INTEGER,
    Discount REAL,
    Profit REAL
);
