# 📘 Day 43 Learning Log — City & Property-Type KPI Aggregation  
**Date:** 2025-11-10  
**Phase:** Data Analysis  
**Focus:** KPI Aggregation and Summary Export  
**Dataset:** `str_market_clean_v2.parquet`  
**Tool:** Python (pandas)  
**Author:** JP Malit  

---

## 🧩 Overview  
Today’s session focused on extending our STR dataset into actionable insights through KPI aggregation.  
We computed performance metrics across both **city** and **property_type** dimensions, highlighting how market and accommodation types differ in revenue performance.  

---

## 🔹 Block 1 — City-Level Performance Summary  
Grouped the cleaned dataset by `city_display` to calculate average **ADR**, **RevPAR**, and **Occupancy** across each market.  
Learned how `groupby()` + `agg()` provide a powerful, concise way to summarize data for each unique city.  
- Used `.reset_index()` to flatten the grouped output back into a normal DataFrame for exporting and display.  
- Discovered that `.to_string(index=False)` produces a clean console output, removing extra index clutter.

---

## 🔹 Block 2 — Property-Type RevPAR Analysis  
Aggregated key KPIs by `property_type` to identify category-level profitability.  
Learned that **“aggregate”** refers to combining multiple rows into summary statistics (e.g., mean, count) for each group.  
Also found that RevPAR variations between property types clearly show which listings generate higher revenue potential.

---

## 🔹 Block 3 — Combined City + Property-Type Export  
Built a joined summary by grouping on both `city_display` and `property_type`, producing a city-level comparative table for Power BI integration.  
Saved this as `avg_rates_by_city_and_type.csv`, making it easy to visualize performance distributions per market and property class.  
This block also reinforced how to chain multiple groupings and how `.sort_values()` helps prioritize top-performing property types.

---

## 🧠 Key Learnings  
- `.groupby()` is one of pandas’ most powerful tools for KPI reporting.  
- Aggregation creates instant executive-level summaries from granular data.  
- Formatting outputs with `.to_string()` enhances terminal readability during debugging.  
- Adding both market and property-type grouping provides business context for STR profitability.  

---

## 📂 Output Files  
| File | Description |
|------|--------------|
| `data/interim/city_kpi_summary.csv` | City-level ADR, RevPAR, and Occupancy summary |
| `data/interim/revpar_by_property_type.csv` | Property-type-level KPI summary |
| `data/interim/avg_rates_by_city_and_type.csv` | Combined city + property-type KPI export |

---

## 🔁 Next Steps  
- Integrate the summarized KPI datasets into Power BI for cross-market benchmarking.  
- Visualize revenue concentration by property class and region.  
- Begin designing Power BI model relationships between city, property, and KPI layers.  

---

**End of Day 43 — KPI Aggregation & Export Complete**  
✅ *us_str_pipeline v1.2 — Data Analysis Phase in Progress*
