# 📊 Day 19 — Top 2 Regional Sales Dashboard  

**Date:** October 17, 2025  
**Phase:** Pipeline Flow  
**Tools:** SQL • Python (pandas) • Power BI  
**Dataset:** Superstore Sales (Top 2 Regions)  
**Author:** [JP Malit (blakusnaku)](https://github.com/blakusnaku)  

---

## 🧭 Overview  
This project explores **top-performing regional sales** across the Superstore dataset using a full data pipeline approach.  
The goal was to filter the **top 2 regions by total sales** and visualize their category performance comparison between *East* and *West* regions.  

---

## ⚙️ Pipeline Flow  

| Block | Tool | Focus | Output |
|:------|:-----|:------|:--------|
| **Block 1** | SQL | Use subquery to filter top 2 regions by total sales | `top_regions_subquery.sql` |
| **Block 2** | Python (pandas) | Apply Boolean mask using `.isin()` for filtered regions | `top_regions_filtered.csv` |
| **Block 3** | Power BI | Create comparative dashboard with slicer for region filter | `top_2_regional_sales.pbix` |
| **Block 4** | GitHub | Document project learnings and insights | `block4_learning_log.md` |

---

## 🧩 Key Learnings  
- Practiced **nested subqueries** and understood how `GROUP BY` and `ORDER BY` interact inside them.  
- Learned that CSV imports can misread numbers as `object` types — fixed with `.astype(float)` after removing commas.  
- Reinforced Boolean masking in pandas using `.isin()` to replicate SQL subquery behavior.  
- Experimented with Power BI **slicer styles** (Vertical vs Tile vs Dropdown) to find clean layout balance.   

---

## 🧠 Insights  
The **West region** leads in total sales, particularly in *Furniture* and *Technology*, while the **East region** shows strong performance in *Office Supplies*.  
The comparison highlights how product mix and regional dynamics affect overall sales balance, providing potential leads for rebalancing marketing focus and inventory.  

---

## 📊 Dashboard Preview  
**Title:** *Regional Sales Comparison (Top 2 Performing Regions)*  
**Features:**  
- Region-based slicer (East / West)  
- KPI cards (Total Sales, Profit, Total Orders)  
- Side-by-side bar comparison by category  
- Custom footer and color branding (`#F97316` orange / `#2563EB` blue)  

[Dasboard Preview](assets/dashboard_preview.png)

---

## ⛓️ Study Dashboard Hub
This project contributes to the ongoing **Study Dashboard Series**, documenting progress across multiple data analytics disciplines.  
View the full learning dashboard here:  
[blakusnaku-study-dashboard GitHub](https://github.com/blakusnaku/blakusnaku-study-dashboard)
 
---

## 🧾 Footer Info  

💡 **Insights:** The West region outperforms East in total sales, driven mainly by Furniture and Technology categories.  
East shows competitive performance in Office Supplies but lags slightly in overall revenue share.  
This comparison highlights strong category leadership and opportunities to balance sales across regions.  

📂 **Dataset:** top_regions_filtered.csv  
📅 **Date Updated:** 2025-10-17  
📊 **Toolchain:** SQL → Python (pandas) → Power BI  
🧭 **Layout Ratio:** Title 15% | Charts 70% | Footer 15%  
👤 **Created by JP Malit | #100DaysOfData**

---

## 📁 File Structure  
```
day19_filter_top_regions/
├── assets/
│   └── dashboard_preview.png
│   
├── data/
│   ├── superstore.csv
│   ├── superstore.db
│   └── top_regions_filtered.csv
│   
├── notes/
│   └── block4_learning_log.md
│   
├── scripts/
│   ├── block1_sql_action.sql
│   ├── block2_python_action.py
│   └── superstore_schema.py
│   
├── dashboard/
│   └── top_2_regional_sales.pbix
│   
└── README.md
```

---

## #Tags  
#SQL #Python #Pandas #PowerBI #DataVisualization #AnalyticsJourney #100DaysOfData #BlakusnakuAnalytics
