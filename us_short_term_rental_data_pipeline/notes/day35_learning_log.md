# 🧩 Day 35 — STR Pipeline: Cleaning Stage

**Date:** 2025-11-02  
**Phase:** Data Acquisition → Cleaning Stage  
**Tools:** Python (pandas, json, os, time)  
**Dataset:** InsideAirbnb (New York, Seattle, Portland)  

---

## 🧠 Overview
Today marked the completion of the cleaning phase of the **US STR Pipeline**.  
We focused on refining numeric and text cleaning logic, standardizing headers, merging multi-city datasets, and optimizing performance for future scalability.

---

## 🔁 Pipeline Summary

| Block | Focus | Output |
|:--|:--|:--|
| **Block 1** | Clean text and numeric fields (`price`, `rating`, `availability_365`) | `clean_numeric_text_[city].csv` |
| **Block 2** | Standardize headers and remove duplicates | `standardized_[city]_listings.csv` |
| **Block 3** | Merge listings + calendar datasets | `clean_merged_[city].parquet` |
| **Block 4** | Reflection and documentation | `day35_learning_log.md` |

---

## 🧩 Key Learnings

- Implemented **chunk-based merging** to efficiently process large datasets without exceeding memory limits.  
- Successfully merged the **Los Angeles** dataset (~16 million rows), confirming that the pipeline can handle heavy data volumes.  
- Learned that even a small compressed file (e.g., 38 MB `.gz`) can decompress into hundreds of MB in RAM, highlighting why chunk streaming is essential for scalable ETL.  
- Later discovered that the **Los Angeles calendar dataset** was too large for daily study blocks (final file ≈ 381 MB).  
  Switched to **Portland, OR** for a more manageable dataset, while keeping Los Angeles archived for **future stress testing**.  
- Recognized the **importance of validating dataset integrity** before running production pipelines to avoid wasted compute time.  
- Added a **time counter** to measure block performance — revealing that merges were extremely fast and the true bottleneck was **file compression** during `.to_csv(compression="gzip")`.  
- Understood that **compression is I/O-bound and single-threaded**, while merges are CPU-optimized and efficient in memory.  
- Migrated final outputs to **Parquet (Snappy compression)** for faster write speeds, smaller files, and native Power BI compatibility.  
- Updated `etl_config.json` to include configurable output settings (`"format"` and `"compression"`), making the pipeline flexible without code changes.  
- Reinforced a key principle: *data engineering is as much about designing scalable, adaptable systems as it is about processing data.*

---

## 🧭 Reflections
This session bridged the gap between analytics and data engineering thinking.  
What began as a simple cleaning task evolved into an exploration of optimization, scalability, and architectural design.  
The pipeline now supports multi-dataset processing, configurable outputs, logging, timing, and chunked execution — all driven by a single `etl_config.json`.  
Most importantly, today’s work established the foundation for an automated, production-ready ELT system.

---

## 🚀 Next Steps
- Begin the **Validation & Transformation Stage** (Day 36).  
- Implement lightweight schema alignment checks for merged outputs.  
- Prepare Parquet datasets for Power BI integration tests.

---

## 📁 Output Files
- `/data/interim/clean_numeric_text_[city].csv`  
- `/data/interim/standardized_[city]_listings.csv`  
- `/data/processed/clean_merged_[city].parquet`  
- `/logs/run_log.json`  

---

## 🧠 Footer Insight

> Efficiency in ETL isn’t just about handling big data — it’s about **designing pipelines that think ahead**.  
> With configuration-driven logic, scalable compression, and structured logging, the STR Pipeline has officially moved from experimental to **production-ready design thinking**.

---

🧠 **Insights:** Cleaning Stage optimization and Parquet migration  
📂 **Dataset:** InsideAirbnb (NY · Seattle · Portland)  
📅 **Date Updated:** 2025-11-02  
📊 **Toolchain:** Python (pandas) → JSON Configs → Parquet Output  
🧭 **Version:** `us_str_pipeline v1.0 — Cleaning Stage Complete`
