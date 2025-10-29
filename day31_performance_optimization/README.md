# 📊 Day 31 — STR Performance Optimization  
**Date:** 2025-10-29  
**Project:** 100 Days of Data  
**Phase:** STR Dataset — Efficiency & Performance  
**Tools:** SQL • Python (pandas) • Power BI • GitHub  
**Dataset:** Short-Term Rental (STR) Calendar  
**Author:** JP Malit  

---

## 🧩 Overview  
This session focused on **end-to-end performance optimization** across the STR dataset pipeline.  
From indexing in SQL to memory-efficient loading in Python and faster refreshes in Power BI, each block demonstrated how small structural and type-level improvements compound into measurable downstream efficiency gains.

---

## ⚙️ Pipeline Flow  

| Block | Tool | Focus | Output |
|:--|:--|:--|:--|
| 1 | SQL | Optimize STR queries with indexes on `listing_id` and `date` | Verified plan shift from `SCAN` → `SEARCH USING INDEX` |
| 2 | Python | Benchmark `pandas.read_csv()` performance | Measured memory reduction and timing differences |
| 3 | Power BI | Evaluate dashboard refresh speed | Tested baseline vs optimized CSV refresh time |
| 4 | GitHub | Summarize learnings | Documented results and reflections |

---

## 🧠 Key Learnings  

- **SQL:** Indexes drastically improve query performance by reducing full table scans.  
- **Python:** Specifying `dtype`, `usecols`, and `parse_dates` reduces memory usage up to **76%**, improving scalability.  
- **Power BI:** Lighter, typed CSVs refresh ~40% faster, reducing model latency.  
- **Pipeline Insight:**  
  Upstream optimizations in SQL and Python directly influence downstream Power BI responsiveness and refresh performance.

---

## 🪞 Reflections  

The experiment illustrated how **data engineering best practices**—like indexing, data type management, and pruning unnecessary columns—are critical for analytical scalability.  
Even though the dataset was small (~2K rows), the effects were already visible, showing that **performance tuning matters at every layer** of the data pipeline.

---

## 📊 Dashboard Preview  
*(Placeholder: Power BI Performance Analyzer visual comparing baseline vs optimized refresh time)*  

---

## 🧮 Study Dashboard Hub  
> This project contributes to the ongoing **Study Dashboard Series**, documenting progress across multiple data analytics disciplines.  
> View the full learning dashboard here:  
> [🔗 blakusnaku-study-dashboard (GitHub)](https://github.com/blakusnaku/blakusnaku-study-dashboard)

---

## 🗂️ File Structure  
```
day31_performance_optimization/ 
├── data/
│ ├── calendar.csv
│ └── calendar_optimized.csv
├── scripts/
│ ├── build_calendar_table.sql
│ ├── block1_sql_action.sql
│ └── block2_python_action.py  
├── notes/
│ └── block4_learning_log.md 
└── README.md
```

---

## 🏷️ Tags  
#100DaysOfData #SQL #Python #Pandas #PowerBI #PerformanceOptimization #DataPipeline #AnalyticsJourney #BlakusnakuAnalytics  

