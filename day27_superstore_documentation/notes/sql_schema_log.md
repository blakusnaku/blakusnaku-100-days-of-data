# 🧱 Superstore SQL Schema Log  
**Day:** 26  
**Phase:** BI Mastery — Superstore Capstone  
**Dataset:** `superstore_clean_stage2.csv`  
**Tool:** SQLite via VS Code  
**Author:** JP Malit  
**Repository:** blakusnaku-100-days-of-data  

---

## 🧭 Overview  
This log documents the creation, structure, and validation of the **Superstore SQL schema**, built using the cleaned dataset from Day 25.  
The goal of this stage is to establish a **consistent relational foundation** for analytical queries and Power BI integration.

---

## 🏗️ Schema Creation

### 🧩 Table Definition
```sql
CREATE TABLE superstore (
    row_id INTEGER PRIMARY KEY,
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
```

### 🧰 Import Command
```sql
.mode csv
.import data/superstore_clean_stage2.csv superstore
```

✅ **Note:**  
Before import, the helper column `postal_len` created in Python validation (Day 25) was removed to match the 21-column schema.

---

## 🧪 Schema Validation

| Check | SQL Command | Result | Notes |
|--------|--------------|--------|-------|
| Verify structure | `PRAGMA table_info(superstore);` | ✅ Passed | All 21 columns imported with correct data types |
| Count records | `SELECT COUNT(*) FROM superstore;` | ✅ Passed | Matches Excel & Python record count |
| Detect nulls | `SELECT * FROM superstore WHERE sales IS NULL OR profit IS NULL;` | ✅ Passed | No null values found |
| Validate dates | `SELECT * FROM superstore WHERE ship_date < order_date;` | ✅ Passed | All dates logical |
| Numeric validation | `SELECT * FROM superstore WHERE sales < 0 OR profit < 0 OR quantity <= 0;` | ⚠️ Found 1,871 rows | Negative profit = valid business loss |
| Check duplicates | `SELECT order_id, COUNT(*) FROM superstore GROUP BY order_id HAVING COUNT(*) > 1;` | ⚠️ Found 2,471 rows | Multi-item orders — valid duplicates |
| Row ID uniqueness | `SELECT COUNT(DISTINCT row_id), COUNT(*) FROM superstore;` | ✅ Passed | 1:1 unique mapping |
| State–region pairing | `SELECT DISTINCT region, state FROM superstore;` | ✅ Passed | All regions match valid states |

---

## 🧾 Summary of Findings

| Category | Observation | Status |
|-----------|--------------|---------|
| Schema structure | 21 columns, consistent with Python schema | ✅ Valid |
| Extra column (`postal_len`) | Dropped before import | ✅ Fixed |
| Data consistency | No nulls or date errors found | ✅ Passed |
| Negative profit entries | 1,871 records | ⚠️ Accepted as legitimate loss data |
| Duplicate order IDs | 2,471 rows | ✅ Multi-item orders confirmed valid |
| State / Region mapping | Verified across dataset | ✅ Accurate |

---

## 🧩 Integration Readiness
The Superstore SQL schema now serves as the **central source of truth** for:
- Aggregation and analytical queries  
- Data extraction for Python and Power BI  
- Downstream joins and KPI calculations  

---

## 💾 Outputs

| File | Description |
|------|--------------|
| `data/superstore_clean_stage2.csv` | Clean dataset imported into SQL |
| `scripts/block1_sql_schema.sql` | Schema creation and import script |
| `notes/sql_schema_log.md` | This document — schema definition and validation summary |

---

✅ **Conclusion:**  
The **Superstore SQL Schema** has been successfully created and validated.  
The dataset is now fully structured, relationally consistent, and ready for analytical operations in **Python (Block 2)** and **Power BI (Block 3)** for Day 26.

---
