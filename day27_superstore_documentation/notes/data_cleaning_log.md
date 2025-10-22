# 🧹 Superstore Cleaning Protocol v1  
**Dataset:** `superstore_raw.csv`  
**Prepared by:** JP Malit  
**Phase:** BI Mastery — Superstore Capstone  
**Goal:** Standardize and validate the Superstore dataset for integration across SQL → Python → Power BI.  

---

## 🔧 Cleaning & Formatting Steps  

| Step | Columns | Action | Notes |
|------|----------|--------|-------|
| **1. Standardize Headers** | All columns | Renamed to `lowercase_snake_case` | Ensures compatibility across SQL, Python, and Power BI environments |
| **2. Clean Numeric Fields** | `sales`, `profit` | Removed commas and formatting symbols | Enables proper numeric operations and aggregation |
| **3. Set Data Types** | `quantity` (int), `discount` (float, 2 decimals) | Converted for accurate calculations | Discount values standardized to two decimal places |
| **4. Standardize Dates** | `order_date`, `ship_date` | Converted to `YYYY-MM-DD` format | ✅ **Validated:** All `ship_date` ≥ `order_date` |
| **5. Clean Text Fields (Trim + Proper Case)** | `ship_mode`, `customer_name`, `segment`, `country`, `city`, `state`, `region`, `category`, `sub_category`, `product_name` | Removed extra spaces and normalized capitalization | Prevents inconsistent grouping or filtering in visuals |
| **6. Clean ID Fields (Trim + Uppercase)** | `order_id`, `customer_id`, `product_id` | Trimmed and converted to uppercase | Avoids mismatch in joins or case-sensitive lookups |
| **7. Format Postal Code** | `postal_code` | Set data type to **Text** | ✅ Preserves leading zeros for ZIP code consistency |
| **8. Remove Phantom or Blank Rows** | All columns | Dropped header rows mistakenly imported as data | Prevents `NULL` row grouping in queries |
| **9. Handle Duplicates** | `order_id` | Kept multiple entries per order | ✅ **Validated:** Multiple `order_id` = multi-item purchases |
| **10. Use `row_id` as Unique Identifier** | `row_id` | Retained as unique key for each record | Ensures each product line within an order remains distinct |

---

## 🧪 Validation Summary  

| Check | Method | Result |
|--------|--------|--------|
| Missing values | Excel filters + conditional formatting | ✅ None found in key columns |
| Blank cells | Conditional highlight | ✅ No blanks in primary fields |
| Null values | Verified visually and via filters | ✅ No nulls present |
| Ship date validation | `ship_date ≥ order_date` | ✅ Passed |
| Duplicate order IDs | `COUNTIFS(order_id)` | ✅ Expected (multi-item orders confirmed) |
| Row ID uniqueness | `COUNTIF(row_id)` | ✅ All unique |
| Numeric integrity | Filter text in numeric fields | ✅ Clean — all numeric values valid |
| Date format consistency | Power BI import preview | ✅ Recognized correctly as `date` type |
| State validation | Cross-checked against official U.S. state list | ✅ All valid U.S. states confirmed |
| Postal code validation | Column formatted as text | ✅ Leading zeros preserved during export |

---

## 💾 Outputs  

| File | Description |
|------|--------------|
| `superstore_raw.csv` | Original unprocessed dataset |
| `superstore_clean_stage1.csv` | Cleaned and validated version ready for SQL import |
| `superstore_clean_stage2.csv` | Python-validated version with standardized postal codes |
| `superstore_final_clean.csv` | Final verified dataset post-SQL + Python validation |

---

## 🧠 Observations & Key Notes  
- Dataset confirmed free of nulls, blanks, and structural inconsistencies.  
- Postal codes standardized to 5 digits using text formatting — ensures proper mapping and join performance.  
- All U.S. states validated and matched against official reference list.  
- Verified that **multiple order_id entries represent legitimate multi-item orders**, not duplicates.  
- **`row_id` remains the unique row-level key** for tracking individual transactions.  

---

✅ **Summary:**  
All cleaning tasks have been completed and verified.  
The dataset is now standardized, validated, and ready for ingestion into SQL and Python for further analytical processing in the **Superstore Final Project (Day 25)** under the **BI Mastery** phase.  
