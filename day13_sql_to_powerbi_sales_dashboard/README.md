# 🧾 Day 13 — SQL to Power BI Sales Dashboard

**Date:** October 11, 2025  
**Phase:** Pipeline Flow  
**Tools:** SQL • Python (pandas) • Power BI  
**Dataset:** Custom Dummy Sales Data (Created for Practice)  
**Author:** [JP Malit (blakusnaku)](https://github.com/blakusnaku)

---

## 🧩 Overview
This project was designed to simulate a **real-world sales pipeline** using a custom-built dataset.  
I created a dummy dataset from scratch in SQL to better understand how data structure, column relationships, and table definitions affect downstream analytics.  
The goal was to connect raw table creation and querying directly to visualization — reinforcing end-to-end pipeline thinking.

---

## ⚙️ Pipeline Flow

| Block | Tool | Focus | Output |
|:------|:-----|:------|:--------|
| **Block 1** | SQL | Create dummy `orders` table, insert sample records, and perform basic SELECT, WHERE, and aggregation queries | SQLite database (`sales.db`) |
| **Block 2** | Python (pandas) | Load SQL data, clean column names, validate types, and export a ready-for-BI CSV | `dummy_sales_cleaned.csv` |
| **Block 3** | Power BI | Import CSV, create KPI cards, sales breakdown charts, and a simple regional dashboard | `Block3_Sales_Dashboard.pbix` |

---

## 🧠 Key Learnings
- Learned to design and populate a **custom dataset** — improving understanding of schema design and data types.  
- Practiced **query construction from scratch**, instead of relying on pre-existing data.  
- Reinforced cleaning discipline: column naming conventions, numeric conversion, and data validation.  
- Understood how data accuracy at the SQL level simplifies later Power BI modeling.  
- Built confidence in handling the **full pipeline**: create → query → clean → visualize.  

---

## 💬 Reflections
This project felt special because it was 100 % self-built — every value and column was intentional.  
It made me realize that building even a small dataset teaches more about structure and logic than passively using ready-made ones.  
It also reminded me that understanding *how data is born* helps me design better analytics flows downstream.  
The process felt like the first true rehearsal of what a real analytics workflow looks like end-to-end.  

---

## 📊 Dashboard / Deliverables Preview
**Title:** *SQL to Power BI Sales Dashboard (Day 13)*  
**Visuals:**  
- KPI Cards: Total Sales • Total Profit • Average Order Value  
- Bar Chart: Sales by Region  
- Column Chart: Profit by Product Category  
- Footer with insights and standardized format  
**Figures in ₱ (Philippine Peso)**  

---

## ⛓️ Study Dashboard Hub
This project journey builds into my **central Study Dashboard**, which you can explore here:  
[blakusnaku-study-dashboard GitHub](https://github.com/blakusnaku/blakusnaku-study-dashboard)

---

## 🧾 Footer Info
**Block 3 — SQL to Power BI Sales Dashboard | Day 13 | © blakusnaku analytics**  
Dataset: *Custom Dummy Sales Data (Created for Practice)*  
Figures in ₱ (Philippine Peso) | Power BI v2025.10  
Created by *JP Malit | Study Project Series*

---

## 🗂️ File Structure
```
day13_sql_to_powerbi_sales_dashboard/
│
├── data/
│ ├── dummy_sales_raw.sql
│ ├── dummy_sales_cleaned.csv
│
├── scripts/
│ ├── block1_create_and_query.sql
│ ├── block2_clean_in_pandas.py
│
├── dashboard/
│ ├── Block3_Sales_Dashboard.pbix
│
├── notes/
│ ├── block4_learning_log.md
│
└── README.md
```

---

## 🪶 Tags
`#SQL` `#Python` `#PowerBI` `#DummyDataset` `#SalesDashboard` `#PipelineFlow` `#StudyProjectSeries`

---

**End of Day 13 — SQL to Power BI Sales Dashboard**
