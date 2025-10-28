# 📊 Day 30 — STR Debug Series

**by blakusnaku (JP Malit)**  
**Date:** 2025-10-28  
**Phase:** STR Data Debugging  
**Repository:** [blakusnaku-100-days-of-data](https://github.com/blakusnaku/blakusnaku-100-days-of-data)

---

## 🧩 Overview
Day 30 focused on **debugging and validation** across the full STR data pipeline — from SQL joins to Python merges and Power BI field handling.  
Instead of creating new visuals, the goal was to ensure data integrity and type consistency throughout the system.

This session reinforced end-to-end thinking in data workflows, identifying how small inconsistencies (like header omissions or text-type numeric columns) can propagate downstream and impact analytics accuracy.

---

## 🔁 Pipeline Flow

| Block | Tool | Focus | Output |
|:------|:------|:------|:------|
| 1 | SQL | Validate joins and export headers properly | `listings_calendar_joined.csv` |
| 2 | Python | Debug `KeyError` and verify merge consistency | `merged_debugged.csv` |
| 3 | Power BI | Handle missing ADR/occupancy, fix data types | Functional KPI cards |
| 4 | GitHub | Document troubleshooting & lessons | `block4_learning_log.md` |

---

## 🧠 Key Learnings

### SQL
- `.headers on` must be enabled to include headers in exports.  
- Missing headers cause misalignment in downstream imports.

### Python
- `KeyError: 'listing_id'` can stem from mismatched or case-sensitive column names.  
- Always normalize headers via `str.strip().str.lower()` before merging.

### Power BI
- `adr_final` and `occupancy_final` columns were incorrectly typed as **Text**.  
- Manually changing them to **Decimal Number** fixed KPI card errors.  
- Data-type validation is essential before writing DAX formulas.

### Cross-Stage Insight
- **Systemic issues** → Fix upstream (SQL / Python).  
- **Sporadic anomalies** → Fix downstream (Power BI).  
- Power BI is best for presentation logic, not heavy data cleaning.

---

## 📊 Dashboard Focus
> Visual creation was **not** the priority for this day.  
> Focus was on ensuring visuals and DAX formulas worked correctly after debugging ADR and occupancy field issues.

---

## 🧭 Study Dashboard Hub
This project contributes to the ongoing **Study Dashboard Series**, documenting progress across multiple data analytics disciplines.  
View the full learning dashboard here:  
👉 [blakusnaku Study Dashboard](https://github.com/blakusnaku/blakusnaku-study-dashboard)

---

## 📁 File Structure
```
day30_str_debug/
├── data/
│   ├── raw/
│   │   ├── listings_raw.csv
│   │   └── calendar_raw.csv
│   ├── interim/
│   │   ├── listings_calendar_joined.csv
│   │   ├── listings_calendar_joined_missing.csv
│   │   └── merged_debugged.csv
│   └── processed/
│       └── str_model_clean.csv
├── scripts/
│   ├── block1_sql_action.sql
│   └── block2_python_action.py
├── notes/
│   └── block4_learning_log.md
└── README.md
```

---

## 🧾 Footer Info
```
💡 Insights: Debugging is part of design — stable data foundations make strong visuals.

Block 3 — STR Debug Model | Day 30 | © blakusnaku analytics  
Dataset: listings_calendar_joined_missing.csv | Updated: 2025-10-28  
Figures in ₱ (Philippine Peso) | Toolchain: SQL → Python (pandas) → Power BI  
Created by JP Malit | #100DaysOfData
```
