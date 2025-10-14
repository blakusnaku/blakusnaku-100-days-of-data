# 🧠 Day 16 — Top 10 Customers Dashboard  
**Date:** October 14, 2025  
**Phase:** Pipeline Flow  
**Tools:** SQL • Python (pandas) • Power BI  
**Blocks Covered:** 1–3  

---

## 🧩 Block 1 — SQL: Filter Top 10 Customers  
**Objective:** Query and export the top 10 customers by total sales using the Superstore dataset.  
**Key Steps:**
- Opened `superstore.db` and re-imported the cleaned CSV to ensure column alignment.  
- Used SQL aggregation to group sales by `customer_id` and `customer_name`.  
- Sorted by `SUM(sales)` in descending order and limited to the top 10.  
- Exported the results as `top10_customers.csv` for downstream analysis.  

**Learning Points:**
- Confirmed how SQLite handles imports and why column mismatch (`profit_calc`) can cause NULL padding.  
- Strengthened understanding of transient vs persistent databases (`.open` vs in-memory).  
- Realized that consistent table structure is essential before aggregation and export.  
- Reinforced best practice of using `.headers on` and `.mode csv` before outputting results.  

**Result:**  
Successfully exported a clean `top10_customers.csv` dataset — forming the foundation for Python validation and Power BI visualization.  

---

## 🐍 Block 2 — Python (pandas): Create Top 10 Subset  
**Objective:** Load, verify, and sort the top 10 customer dataset in pandas.  
**Key Steps:**
- Loaded `top10_customers.csv` into a DataFrame for validation.  
- Verified data types, ensured correct decimal formatting, and re-sorted by `total_sales`.  
- Rounded all totals to 2 decimal places for consistency.  
- Saved a verified version as `top10_customers_verified.csv` for Power BI import.  

**Learning Points:**
- Strengthened comfort with pandas’ `.sort_values()` and `.round()` functions for quick quality checks.  
- Understood how minor formatting differences (float precision, NaN handling) affect downstream visualization.  
- Reinforced confidence in pandas as a tool for quick validation between SQL and Power BI pipelines.  

**Result:**  
Produced a verified dataset (`top10_customers_verified.csv`) — ensuring clean and ready input for visualization in Power BI.  

---

## 📊 Block 3 — Power BI: Display Top 10 Customer Cards  
**Objective:** Visualize the top 10 customers and explore design balance within Power BI’s layout system.  
**Key Steps:**
- Imported `top10_customers_verified.csv` into Power BI.  
- Created 10 card visuals to display customer names and sales values.  
- Experimented with the Multi-row Card visual and discovered its vertical stacking limitation.  
- Manually aligned visuals into a **2×5 grid layout**, balancing readability and design uniformity.  
- Added the new standardized footer layout for insights, dataset info, and metadata.  

**Learning Points:**
- Gained first-hand experience with Power BI’s **layout constraints** (no spacing or column control in Multi-row Cards).  
- Recognized how visual composition (alignment, spacing, typography) affects perception of clarity.  
- Strengthened awareness of dashboard structure — **Title 15% | KPI/Charts 70% | Footer 15%**.  
- Learned to differentiate between *functional clarity* and *design polish*.  

**Result:**  
A functional 2×5 Top 10 Customer Dashboard with consistent footer branding and clean visual hierarchy.  

---

## 💡 Reflections  
- Today revealed Power BI’s design limits, but also sharpened my sense for layout rhythm and spacing.  
- The manual alignment process emphasized **composition awareness** — I’m starting to think more like a data designer.  
- I now see that dissatisfaction with layout isn’t failure — it’s growth in visual sensitivity.  
- Moving forward, I plan to explore **hybrid layouts (Power BI → Canva/Figma)** to gain precise spacing control and stylistic freedom.  
- This block reaffirmed the balance between data accuracy and design precision — the two halves of great storytelling.  

---

**End of Day 16 Log**  
*Block 1–3 Complete • Block 4 (Reflection) Logged*  
