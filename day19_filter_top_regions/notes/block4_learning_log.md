# 🧠 Day 19 — Top 2 Regional Sales Dashboard  
**Date:** October 17, 2025  
**Phase:** Pipeline Flow  
**Tools:** SQL • Python (pandas) • Power BI  
**Dataset:** Superstore Sales (Top 2 Regions)  
**Author:** [JP Malit (blakusnaku)](https://github.com/blakusnaku)  

---

## 🧩 Overview  
Today’s study block focused on **multi-stage data filtering and visualization**, showing how insights evolve as data moves from SQL to Python to Power BI.  
Using the Superstore dataset, I identified and compared the **top 2 performing regions (West and East)** across the full data pipeline — from subqueries to pandas Boolean masks to Power BI dashboards.  

---

## ⚙️ Pipeline Summary  

| Block | Tool | Focus | Output |
|:------|:-----|:------|:--------|
| **Block 1** | SQL | Used subquery to isolate top 2 regions by `SUM(sales)` | `top_regions_subquery.sql` |
| **Block 2** | Python (pandas) | Applied Boolean mask using `.isin()` for top regions | `top_regions_filtered.csv` |
| **Block 3** | Power BI | Built **Top 2 Regional Sales Dashboard** with region slicer and comparison view | `top_2_regional_sales.pbix` |
| **Block 4** | Reflection | Summarized learnings and workflow across tools | `block4_learning_log.md` |

---

## 📚 Key Learnings  

### 🧩 SQL  
- Learned to build **subqueries** that filter data dynamically (`WHERE region IN (SELECT … LIMIT 2)`), and understood how `GROUP BY` and `ORDER BY` interact inside subqueries.  
- Realized that **schemas** play a big role in structuring datasets before queries — began using `DROP TABLE IF EXISTS` in schema design.  

### 🐍 Python  
- Discovered that numeric columns can sometimes load as `object` due to commas, and learned to clean them with:  
  ```python
  df['Sales'] = df['Sales'].astype(str).str.replace(',', '').astype(float)
  ```
- Used `.isin()` for **Boolean masking** to replicate SQL subquery logic.  
- Confirmed results matched SQL output (West ₱425K, East ₱367K).  

### 📊 Power BI  
- Designed a **comparative dashboard** for East vs West performance.  
- Used **Region** as a *Legend* for side-by-side comparisons per category.  
- Styled visuals using brand colors (`#F97316` orange for West, `#2563EB` blue for East).  
- Learned how slicer styles (Vertical vs Tile vs Dropdown) affect layout clarity.   

---

## 💭 Reflections  
This block made me appreciate how consistent logic flows across tools — **SQL filters data**, **Python cleans and structures it**, and **Power BI communicates it visually**.  
Each step reinforced the other:  
- SQL taught me *how* to isolate valuable data,  
- Python made me *own* the transformation process, and  
- Power BI helped me *tell the story* behind it.  

I also started noticing my design language solidifying — color harmony, layout rhythm, and balanced white space all come more naturally now.  
It feels like the dashboards are beginning to reflect my workflow personality: clean, structured, and data-driven.  

--- 

## 💡 Insights:  
The West region outperforms East in total sales, driven mainly by Furniture and Technology categories.  
East shows competitive performance in Office Supplies but lags slightly in overall revenue share.  
This comparison highlights strong category leadership and opportunities to balance sales across regions.  

📂 **Dataset:** top_regions_filtered.csv  
📅 **Date Updated:** 2025-10-17  
📊 **Toolchain:** SQL → Python (pandas) → Power BI  
🧭 **Layout Ratio:** Title 15% | Charts 70% | Footer 15%  
🧾 **Version:** day19_filter_top_regions
👤 **Created by JP Malit | #100DaysOfData**
