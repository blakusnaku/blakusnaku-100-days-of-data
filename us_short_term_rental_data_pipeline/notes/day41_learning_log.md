# 📘 Day 41 Learning Log — Data Analysis Phase Start
**Date:** 2025-11-08  
**Phase:** Data Analysis — Validation & Prep  
**Project:** US STR Pipeline (InsideAirbnb)  
**Repo:** blakusnaku-100-days-of-data/us_short_term_rental_data_pipeline

---

## ✅ What I did
1) **Loaded & inspected** `str_market_ready.parquet` (12,311 rows × 14 cols).  
   - Key columns: `price`, `adr`, `revpar`, `occupancy_pct`, `los`, `review_scores_rating`, `property_type`, `room_type`, beds/bedrooms/bathrooms.  
   - Missing summary highlighted gaps in `review_scores_rating` (1,663), `price` (1,372), beds/baths (≈1.3k each).

2) **Standardized numerics** (`price`, `adr`, `revpar`, `review_scores_rating`)  
   - Cleaned non-numeric chars via regex and coerced to `float64`.  
   - Verified stable distributions via `describe().T`.

3) **Handled missing values & outliers**  
   - Imputed: `review_scores_rating` with **median**, `bedrooms/beds/bathrooms` with **mode**.  
   - Dropped rows missing **core KPIs** (`price`, `adr`, `revpar`).  
   - Winsorized **1st–99th percentile** for `price`, `adr`, `revpar`, `occupancy_pct`, `los`.  
   - Output: `str_market_clean_v2.parquet` (**10,939 rows**).

---

## 🧠 Key learnings
- **Chained assignment warnings**: `df["col"].fillna(..., inplace=True)` is unsafe; assign back or use `.loc`.  
- Treat **core KPI nulls** strictly (drop) and **auxiliary fields** with sensible imputations.  
- Light winsorization (1–99%) is a clean way to stabilize KPIs before BI without distorting central tendencies.

---

## 📦 Artifacts
- `data/interim/str_market_clean_v1.parquet` — numeric-standardized
- `data/interim/str_market_clean_v2.parquet` — missing/outlier-treated (final for BI prep tests)

---

## 🔭 Next steps (Day 42)
- Add basic **feature engineering** (`price_per_bedroom`, `revenue_per_bed`, `adr_bucket`).
- Produce **city/property-type KPI cuts** for Power BI seed tables.
- Start **Power BI model** using `str_market_clean_v2.parquet`.

---

**Author:** JP Malit  
**Tags:** #100DaysOfData #Python #Pandas #DataPreparation #Winsorization #ETL #STRAnalytics #BlakusnakuAnalytics
