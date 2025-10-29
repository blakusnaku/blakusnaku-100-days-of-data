# 🧠 Block 4 — Learning Log  
**Day 31 — STR Performance Optimization**  
**Date:** 2025-10-29  
**Phase:** STR Dataset — Efficiency & Performance  
**Author:** JP Malit  

---

## 🧩 Overview
Today’s focus was on understanding **query and load performance optimization** across all stages of the STR dataset pipeline — from SQL indexing, to Python data loading, and Power BI refresh efficiency.  
The goal was to quantify how small structural or type-level changes can significantly improve speed and reduce resource usage downstream.

---

## 🔁 Pipeline Summary

| Block | Tool | Focus | Key Output |
|:--|:--|:--|:--|
| 1 | SQL | Add indexes on `listing_id` & `date` | Verified plan improvement from `SCAN` → `SEARCH USING INDEX` |
| 2 | Python | Benchmark `pandas.read_csv()` performance | Achieved 76% memory reduction via dtype & column optimization |
| 3 | Power BI | Test refresh time differences | Observed faster refresh and lighter visual load with optimized CSV |
| 4 | GitHub | Document findings | Summarized timing and performance results for reproducibility |

---

## ⚙️ Block 1 — SQL Performance Benchmark

| Query Type | Index Used | Plan | Runtime (s) | Speedup |
|:--|:--|:--|:--|:--|
| Baseline | None | SCAN calendar | 0.045 | — |
| Optimized | `idx_calendar_listing_date` | SEARCH calendar USING INDEX | 0.030 | ~33% faster |

🧠 **Insight:**  
Creating a composite index (`listing_id`, `date`) reduced query time by roughly a third.  
For larger STR tables, indexing key filter columns will drastically accelerate range queries and improve Power BI data source refresh speed.

---

## 🐍 Block 2 — Python Load Benchmark

| Test | Description | Load Time (s) | Memory (MB) | Δ vs Baseline |
|:--|:--|:--|:--|:--|
| Baseline | Default `read_csv()` | 0.0051 | 0.217 | — |
| Optimized | `dtype`, `usecols`, `parse_dates` | 0.0287 | 0.053 | 🧠 –76% memory |

💡 **Insight:**  
While the optimized load was slightly slower on small data, memory usage dropped dramatically.  
In real-world STR datasets (100k+ rows), these dtype optimizations scale exponentially — improving load times and stability.

---

## 📊 Block 3 — Power BI Refresh Speed Test

| Version | Dataset | Rows | Refresh Time (s) | Δ vs Baseline |
|:--|:--|:--|:--|:--|
| Baseline | `calendar.csv` | 2,193 | 0.41 | — |
| Optimized | `calendar_optimized.csv` | 2,193 | 0.23 | ~44% faster |

💡 **Insight:**  
The optimized dataset loaded faster due to smaller file size and explicit data typing.  
These upstream optimizations reduce Power BI’s type-inference workload, leading to smoother refreshes and more responsive visuals.

---

## 💬 Reflections
- **Conceptual:** I learned how indexes act like a shortcut map — letting SQL “jump” to rows instead of scanning all of them.  
- **Practical:** Explicit typing in Python and lean CSVs dramatically reduce memory load.  
- **Analytical:** Small technical adjustments upstream compound into large performance gains downstream.  
- **Future application:** Apply the same performance testing framework when scaling STR dashboards or integrating larger datasets.
 
---

**© blakusnaku analytics — #100DaysOfData**
