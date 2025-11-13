# 📘 Day 45 — Learning Log  
**Date:** 2025-11-12  
**Focus:** SQL KPI Computation & Export  
**Phase:** Data Analysis (SQL Validation + BI Output Prep)  
**Project:** US STR Pipeline — KPI Aggregation via SQL  

---

## 🧠 Overview  
Today shifted the analysis engine **fully inside SQL**.  
Instead of relying on pandas for KPI calculations, I validated that SQL—on its own—can compute ADR, RevPAR, and Occupancy using GROUP BY logic. This confirms that our BI-ready dataset is structurally correct and that SQL is a viable alternative for computing metrics directly from the database.

---

## 🔍 What I Built Today

### 🧩 Block 1 — SQL KPI by City  
I wrote SQL queries to compute:  
- Average ADR  
- Average RevPAR  
- Average Occupancy  
- Listings per city  

This validated that the Python-generated KPIs match SQL-calculated values.  
The numbers aligned, which confirms consistent logic across the pipeline.

---

### 🏗 Block 2 — SQL KPI by Property Type  
I extended the SQL logic to compare performance at a deeper level:  
- `city_display` + `property_type`  
- Aggregated average performance metrics  
- Identified high-performing property categories inside each city  

This created a richer view of STR profitability patterns.

---

### 📤 Block 3 — Export SQL KPI Results  
I wrote a Python script that:  
1. Connects to `str_market.db`  
2. Runs both SQL queries  
3. Combines the results  
4. Labels the rows (`city_summary` / `property_type_summary`)  
5. Saves everything into **sql_output_kpi.csv**

This file will be used for BI exploration and dashboard prototyping.

---

## 📌 Key Learnings  
- SQL can replicate all KPI logic previously computed in Python.  
- GROUP BY aggregations make KPI logic more transparent and scalable.  
- Exporting SQL outputs into CSV improves interoperability with BI tools.  
- Splitting city-level vs property-type summaries improves analytical clarity.  
- Keeping SQL and Python KPI logic aligned is a strong validation practice.

---

## 📁 Outputs Today  
- `sql_output_kpi.csv` — consolidated KPI summary  
- `export_sql_kpi_results.py` — SQL → CSV exporter  
- Full SQL-based KPI validation using SQLite  

---

## 🎯 Next Steps  
- Use SQL summaries as inputs for Power BI visuals  
- Visualize city vs property-type performance  
- Begin shaping the multi-page STR BI dashboard  

---

## 🧭 Day Summary  
Today strengthened the analytical foundation of the STR pipeline by validating metrics at the SQL layer and exporting clean KPI summaries ready for BI integration.  
The dataset is now confirmed reliable across both Python and SQL, which is essential as we move into the visualization phase.

