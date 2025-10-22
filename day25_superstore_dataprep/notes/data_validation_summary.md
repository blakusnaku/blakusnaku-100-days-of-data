# 🧾 Superstore Data Validation Summary  
**Day:** 25  
**Phase:** BI Mastery — Superstore Capstone  
**Dataset:** `superstore_clean_stage1.csv`  
**Author:** JP Malit  
**Repository:** blakusnaku-100-days-of-data  

---

## 🧭 Overview  
This document records the validation process performed after cleaning the Superstore dataset.  
The goal of this stage is to ensure that all cleaned data imported into SQL, Python, and Power BI maintains structural and logical integrity, and that field relationships remain consistent across all platforms.

---

## 🔹 Block 1 — SQL Validation  
**Tool:** SQLite via VS Code  

### ✅ Goals  
- Import the cleaned dataset into SQL schema.  
- Validate column data types and structure.  
- Check for logical integrity, duplicates, and profit anomalies.  

### 🧩 Actions  
| Check | SQL Command / Query | Result | Notes |
|--------|---------------------|---------|-------|
| Validate schema creation | `PRAGMA table_info(superstore);` | ✅ | All column types correct |
| Check record count | `SELECT COUNT(*) FROM superstore;` | ✅ | Matches Excel record count |
| Detect null values | `SELECT * FROM superstore WHERE sales IS NULL OR profit IS NULL;` | ✅ | No nulls found |
| Validate date logic | `SELECT * FROM superstore WHERE ship_date < order_date;` | ✅ | None returned |
| Verify numeric columns | `SELECT * FROM superstore WHERE sales < 0 OR profit < 0 OR quantity <= 0;` | ⚠️ Returned rows | Some transactions show **negative profit**, confirmed as legitimate loss transactions (discounts / shipping costs) |
| Validate state–region pairs | `SELECT DISTINCT region, state FROM superstore;` | ✅ | All U.S. states valid |
| Detect duplicate orders | `SELECT order_id, COUNT(*) FROM superstore GROUP BY order_id HAVING COUNT(*) > 1;` | ⚠️ Returned rows | **Valid behavior** — multi-item purchases under one order |
| Check row ID uniqueness | `SELECT COUNT(DISTINCT row_id), COUNT(*) FROM superstore;` | ✅ | All unique |
| Review summary stats | Aggregate query (SUM, AVG) | ✅ | Totals consistent with Excel |

### 📘 Findings  
- **Negative Profit Records:** Legitimate business losses; kept intentionally for financial realism.  
- **Duplicate Order IDs:** Represent multiple items purchased in a single order; valid data structure.  
- No structural or type errors found; all state and regional data verified as accurate.  

---

## 🔹 Block 2 — Python Cleaning & Validation  
**Tool:** pandas via VS Code  

### ✅ Goals  
- Validate results from SQL stage programmatically.  
- Confirm data type consistency, postal code formats, and date logic.  
- Standardize column formatting and export clean version for Power BI.  

### 🧩 Cleaning & Validation Steps  
| Check | Code Snippet | Result | Notes |
|--------|---------------|---------|-------|
| Load dataset as UTF-8 | `pd.read_csv(..., dtype={'postal_code': str})` | ✅ | Loaded successfully |
| Convert date columns | `pd.to_datetime(order_date, ship_date)` | ✅ | Converted to datetime64[ns] |
| Standardize postal codes | `.astype(str).str.strip().str.zfill(5)` | ✅ | 449 entries corrected with restored leading zeros |
| Normalize state names | `.str.title().str.strip()` | ✅ | Validated across all 50 U.S. states + D.C. |
| Check nulls and blanks | `df.isnull().sum()` | ✅ | No null values found |
| Verify ship date logic | `ship_date >= order_date` | ✅ | All valid |
| Detect negative profit | `df[df['profit'] < 0]` | ⚙️ 1,871 | Retained as legitimate losses |
| Detect duplicate orders | `df.duplicated(subset='order_id')` | ⚙️ 2,471 | Valid multi-item orders |
| Verify postal length | `df['postal_code'].str.len().unique()` | ✅ | All standardized to 5 |
| Check numeric summary | `df[['sales','profit']].describe()` | ✅ | Ranges verified |
| Export clean dataset | `df.to_csv('superstore_clean_stage2.csv')` | ✅ | Exported successfully |

---

### 📘 Key Findings  
- **Postal Code:** Fixed 449 truncated ZIPs with missing leading zeros.  
- **State Validation:** All 50 states + D.C. confirmed valid after normalization.  
- **Date Logic:** No invalid shipping or order date relationships found.  
- **Profit & Orders:** 1,871 loss transactions retained; 2,471 multi-item orders confirmed.  
- **Clean Export:** Dataset exported as `superstore_clean_stage2.csv` — now standard for Power BI integration.

---

### 📊 Python Validation Summary Output  
```
✅ Validation Summary:
- No nulls or blanks found.
- Ship dates validated: 0 invalid entries.
- 1871 transactions with negative profit (valid losses).
- 2471 multi-item orders confirmed.
- Postal and state fields verified for consistency.
- Dataset integrity confirmed for Power BI integration.
```

---

## 🔹 Block 3 — Power BI Validation  
**Tool:** Power BI Desktop  

### ✅ Goals  
- Verify correct data types and relationships.  
- Test categorical and date-based visuals.  
- Check measure accuracy after import.  

### 🧩 Checks  
| Test | Result | Notes |
|------|---------|-------|
| Data type detection | ✅ Passed | All numeric/date fields recognized |
| Relationships | ✅ Passed | Orders ↔ Shipping_Cost linked properly |
| Aggregations (Sales, Profit) | ✅ Passed | Totals match SQL & Python outputs |
| Date hierarchy visuals | ✅ Passed | Year/Month slicers functional |
| State/Region visuals | ✅ Passed | All states categorized correctly |

### 📘 Notes  
Visual tests confirmed accurate import and data relationships.  
Measures and totals aligned across tools.  

---

## 🔹 Block 4 — GitHub Documentation  
**Tool:** Markdown  

### ✅ Goals  
- Summarize validation findings.  
- Maintain reproducibility and traceability.  

### 📘 Summary  
- All validation steps across SQL, Python, and Power BI passed.  
- **Negative profit** and **duplicate order ID** findings recorded as valid business outcomes.  
- Dataset confirmed clean, logical, and ready for integration into Day 26 pipeline.  

---

✅ **Conclusion:**  
`superstore_clean_stage2.csv` has been fully validated across all tools and officially designated the **Superstore Clean Final Dataset** for the BI Mastery Phase.  
Ready for integration and dashboard development in **Day 26**.