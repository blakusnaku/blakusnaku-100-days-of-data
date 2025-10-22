# 📊 Day 25 — Superstore Data Preparation & Validation  
**Phase:** BI Mastery — Superstore Capstone  
**Date:** 2025-10-25  
**Dataset:** Superstore (Raw → Clean Stage 1 → Stage 2)  
**Author:** JP Malit  
**Repository:** blakusnaku-100-days-of-data  

---

## 🧭 Overview  
Day 25 focuses on the **cleaning, standardization, and validation** of the Superstore dataset — preparing it for reliable integration across SQL, Python, and Power BI.  
This process transforms the raw `.csv` file into a clean, analytics-ready dataset through systematic checks for accuracy, consistency, and data integrity.  

By the end of this session, the dataset serves as a **single source of truth**, ensuring that all transformations and visuals built in future blocks are grounded on verified data.

---

## 🔁 Pipeline Flow  

| Block | Tool | Focus | Output |
|--------|------|--------|--------|
| 1 | Excel → CSV | Data Cleaning & Formatting | `superstore_clean_stage1.csv` |
| 2 | SQL | Schema Validation & Logic Checks | SQL validation queries |
| 3 | Python | Programmatic Verification & Export | `superstore_clean_stage2.csv` |
| 4 | GitHub | Documentation & Version Logging | Updated README + Logs |

---

## 🧹 Data Preparation Steps Summary  

1. **Standardized headers** to `lowercase_snake_case` for toolchain compatibility.  
2. **Cleaned numeric columns** (`sales`, `profit`) by removing commas and formatting symbols.  
3. **Validated data types:**  
   - `quantity` → integer  
   - `discount` → float (2 decimals)  
4. **Standardized date fields** (`order_date`, `ship_date`) to `YYYY-MM-DD` format.  
   - ✅ Verified: all `ship_date ≥ order_date`  
5. **Trimmed and normalized text fields** (`ship_mode`, `segment`, `region`, `category`, etc.).  
6. **Formatted ID fields** (`order_id`, `customer_id`, `product_id`) to uppercase and trimmed spaces.  
7. **Set `postal_code` as text** to preserve leading zeros across all tools.  
8. **Checked for nulls, blanks, and phantom rows:** none found in key columns.  
9. **Verified duplicate orders:** multi-item orders confirmed as valid transaction behavior.  
10. **Validated state entries:** all entries match valid U.S. states after normalization.  

---

## 🧪 Validation Summary  

| Validation Check | Status | Notes |
|------------------|--------|-------|
| Missing / Blank Values | ✅ Passed | No null or blank fields detected |
| Numeric Field Consistency | ✅ Passed | All values cleaned and formatted |
| Date Format & Logic | ✅ Passed | All valid and consistent |
| Postal Code Format | ✅ Passed | All ZIPs standardized to 5 digits |
| Duplicate Handling | ✅ Passed | Multi-item orders verified |
| Row ID Uniqueness | ✅ Passed | All unique identifiers retained |
| U.S. State Validity | ✅ Passed | Confirmed across 50 states + D.C. |

---

## 💾 File Outputs  

| File | Description |
|------|--------------|
| `data/superstore_raw.csv` | Original uncleaned dataset |
| `data/superstore_clean_stage1.csv` | Cleaned and formatted Excel output |
| `data/superstore_clean_stage2.csv` | Python-validated version with postal fixes |
| `notes/data_cleaning_log.md` | Detailed record of Excel cleaning steps |
| `notes/data_validation_summary.md` | Consolidated validation across SQL + Python |

---

## 📄 Related Documentation  
- 🧹 **[Data Cleaning Log → `notes/data_cleaning_log.md`](notes/data_cleaning_log.md)**  
- 🧾 **[Data Validation Summary → `notes/data_validation_summary.md`](notes/data_validation_summary.md)**  
- 🗂️ **Next:** SQL schema creation and Power BI validation (`block1_sql_cleaning.sql`)  

---

## 💬 Reflections  
Day 25 reinforced that **data cleaning is not cosmetic — it’s structural quality control.**  
Through step-by-step cleaning, type validation, and logic checks, the dataset now upholds integrity across all tools in the pipeline.  

Consistency in postal codes, date formats, and state values ensures the data can flow seamlessly into SQL, Python, and Power BI without further manual intervention.  

---

**Next Up → Day 26:**  
Begin the **SQL integration phase**, defining schemas, validating imports, and preparing the dataset for Power BI modeling and KPI dashboards.  
