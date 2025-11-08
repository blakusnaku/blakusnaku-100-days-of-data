# 📘 Day 40 Learning Log — Data Acquisition Phase Wrap-Up  
**Date:** 2025-11-07  
**Phase:** Data Acquisition — BI Preparation  
**Project:** US Short-Term Rental (STR) Data Pipeline  
**Repository:** `blakusnaku-100-days-of-data/us_short_term_rental_data_pipeline`  
**Block Focus:** Export final BI-ready dataset and confirm end-to-end reproducibility  

---

## 🧠 Key Learnings  

### 1. End-to-End Pipeline Verification  
Running the full `automation_pipeline.py` with the pipeline mode set to **production** completed successfully — confirming that the pipeline can now execute **from raw ingestion to BI-ready output** without manual intervention.  
All major stages (`schema_validation → cleaning → harmonization → KPI calculation → SQLite import → verification → export`) are now reproducible and properly logged.

### 2. Merging Behavior and Column Conflicts  
While building `export_bi_dataset.py`, I learned that **pandas drops or overwrites duplicate columns during merges** if no suffixes are defined.  
Initially, both the listings and KPI datasets shared columns like `price` and `beds`, causing pandas to overwrite or drop columns silently — leaving only KPI columns visible in the export.

**Fix Applied:**  
- Added `suffixes=("", "_kpi")` in the merge step to preserve both column sets.  
- Normalized join keys (`listing_id`) to string on both sides.  
- Explicitly selected the final columns for BI export.  

This clarified how **column name collisions** behave in joins and why explicit suffix handling is a critical best practice for modular pipelines.

### 3. Debugging Confirmation Output  
Added key checkpoints and print statements in the export step to verify:  
- Dataset load counts  
- Listing ID key overlap  
- Final columns in the merged dataset  
These debug prints helped verify that the merge worked as intended:
```
Key overlap: 12,311 / 12,311
Columns: ['listing_id', 'city_display', 'price', 'adr', 'revpar', 'occupancy_pct', 'los', 'review_scores_rating', 'property_type', 'room_type', 'beds', 'bedrooms', 'bathrooms', 'latitude']
Rows exported: 12,311
```

---

## 🧩 Final Outputs  
- ✅ **`str_market_ready.parquet`** — BI-ready dataset for Power BI integration  
- ✅ **`str_market_ready.csv`** — lightweight preview file for data inspection  
- ✅ Full pipeline runs reproducibly via `automation_pipeline.py`  

---

## 💡 Reflection  
Today’s debugging reinforced how **data reproducibility and merge precision** directly affect reliability in automated pipelines.  
Learning how pandas resolves column conflicts at merge time clarified a subtle but crucial detail in ETL logic — ensuring that future pipelines remain modular, traceable, and schema-consistent.  

This marks the successful conclusion of the **Data Acquisition Phase** — setting the stage for the upcoming **Transformation and BI Integration Phase**.

---

**Next Steps:**  
- Start Day 41 — Begin Power BI integration tests  
- Design Power BI KPI dashboard using `str_market_ready.parquet`  
- Document schema mapping for BI layer  

---
**Author:** JP Malit  
**#100DaysOfData #Python #Pandas #DataEngineering #ETLPipeline #PowerBI #BlakusnakuAnalytics**
