# 🧠 Day 21 — Data Pipeline Integration (SQL → Python → Power BI)

**Date:** October 19, 2025  
**Phase:** Integration Workflow  
**Tools:** SQL • Python (pandas) • Power BI • GitHub  
**Dataset:** Superstore (Cleaned v1.1)  
**Author:** [JP Malit (blakusnaku)](https://github.com/blakusnaku)

---

## 🔹 Overview
Day 21 focused on establishing a **complete data pipeline integration**, connecting the outputs of SQL and Python into Power BI for seamless refresh automation.  
This session marked the transition from isolated block outputs to a unified ecosystem — where updates in SQL directly cascade through Python and Power BI without manual intervention.

---

## ⚙️ Pipeline Summary

| Block | Tool | Focus | Output |
|:------|:-----|:------|:--------|
| **Block 1** | SQL | Create `superstore_cleaned` view | `superstore_cleaned` view in SQLite |
| **Block 2** | Python | Export SQL view results to CSV | `superstore_cleaned.csv` |
| **Block 3** | Power BI | Refresh dataset and redesign visuals | Integrated dashboard update |
| **Block 4** | GitHub | Document full process | `README.md` + `learning_log.md` |

---

## 🧩 Key Learnings

### 🧠 SQL
- Learned how **views** serve as dynamic, reusable layers — acting as virtual tables that simplify future queries.  
- Realized that **SQLite errors** like “no such table” often just mean a table name mismatch.  
- Added `DROP VIEW IF EXISTS` for flexibility when re-running scripts.

### 🐍 Python
- Exported SQL view results using `pandas` and `sqlite3`.  
- Discovered that column headers were case-preserving from the database — fixed this via:
```
  df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

```
- Reinforced the use of date_format='%Y-%m-%d' to preserve ISO consistency.

---

### 📊 Power BI
- Identified how Power BI automatically formats dates to local (MM/DD/YYYY) — resolved via
**Change Type → Using Locale → English (Canada)** to enforce `YYYY-MM-DD`.
- Finalized the blakusnaku Orange Gradient for consistent visual identity:
```
#FF914D | #FFB072 | #FFD3A1 | #FFE0C2
```
- Enhanced visual balance by adjusting the South region bar for better readability.
- Applied standardized footer with full signature layout.

---

## 🧭 Reflections

This session tied together every prior concept from the 100 Days of Data journey.
Building the end-to-end integration pipeline made the process feel tangible — from SQL logic to Power BI visuals.
Small nuances like locale formats and header casing proved how important “invisible details” are in professional workflows.
It’s not just about producing visuals; it’s about building reliable systems that can scale and refresh cleanly.

---

## 🧩 Footer Insights Summary

Data pipeline successfully integrated from SQL → Python → Power BI.
The cleaned dataset ensures consistent date and numeric formatting across the entire workflow, enabling accurate refresh automation for future dashboards.

📂 Dataset: Superstore (Cleaned v1.1)
📅 Date Updated: 2025-10-19
📊 Toolchain: SQL → Python (pandas) → Power BI
🧭 Layout Ratio: Title 15% | KPI/Charts 70% | Footer 15%
📁 Version: day21_data_pipeline_integration v1.0 
