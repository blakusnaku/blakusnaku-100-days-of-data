# 🔗 Day 13 — SQL to Power BI Sales Dashboard (Joins Practice)

**Date:** October 11, 2025  
**Phase:** Pipeline Flow  
**Tools:** SQL • Python (pandas) • Power BI  
**Dataset:** Dummy Orders & Customers Data (Self-Created)  
**Author:** [JP Malit (blakusnaku)](https://github.com/blakusnaku)

---

## 🧩 Overview
This project focuses on learning how to **combine relational data** using SQL joins and replicate the same process in pandas.  
By joining an `orders` table and a `customers` table, the session explored how data relationships form the foundation of analytics pipelines.  
The workflow ends with a **base Power BI dashboard**, visualizing joined results and validating consistency between SQL and Python outputs.

---

## ⚙️ Pipeline Flow

| Block | Tool | Focus | Output |
|:------|:-----|:------|:--------|
| **Block 1** | SQL | Perform `INNER JOIN` between `orders` and `customers` to merge customer info with order details | `orders_customers_joined` result table |
| **Block 2** | Python (pandas) | Replicate the SQL join using `pd.merge()`; verify data integrity and export cleaned dataset | `orders_customers_joined_pandas.csv` |
| **Block 3** | Power BI | Build a base sales dashboard using joined dataset to visualize customer-level metrics | `block3_powerbi_base_dashboard.pbix` |

---

## 🧠 Key Learnings
- Practiced **INNER JOIN** syntax and logic for connecting tables with shared keys.  
- Understood the parallel between **SQL joins** and **pandas merge** — how both can achieve identical relational outcomes.  
- Gained clarity on join types (`INNER`, `LEFT`, `RIGHT`, `OUTER`) and their impact on dataset size.  
- Learned that keeping consistent key names and clean schemas makes cross-tool joins seamless.  
- Built the foundation for relational modeling in Power BI using custom dummy data.

---

## 💬 Reflections
Day 13 was a major “click” moment — I finally saw how data connects across tools.  
Creating two separate tables and successfully merging them in both SQL and pandas made the concept of **relationships** tangible.  
It also reinforced how important column consistency and key matching are for smooth integrations.  
This project served as the bridge between data cleaning and full-fledged analytics modeling.

---

## 📊 Dashboard / Deliverables Preview
**Title:** *SQL to Power BI Sales Dashboard (Joins Practice)*  
**Visuals:**  
![Dashboard_Preview]()
- KPI cards: Total Sales • Total Customers • Average Order Value  
- Table visual showing joined order-customer data  
- Bar chart by Customer Region or Segment  
- Footer with standardized layout  
**Figures in ₱ (Philippine Peso)**  

---

## ⛓️ Study Dashboard Hub
This project journey builds into my **central Study Dashboard**, which you can explore here:  
[blakusnaku-study-dashboard GitHub](https://github.com/blakusnaku/blakusnaku-study-dashboard)

---

## 🧾 Footer Info
**Block 3 — SQL to Power BI Sales Dashboard (Joins Practice) | Day 13 | © blakusnaku analytics**  
Dataset: *Dummy Orders & Customers (Self-Created)*  
Figures in ₱ (Philippine Peso) | Power BI v2025.10  
Created by *JP Malit | Study Project Series*

---

## 🗂️ File Structure
```
day13_joins/
│
├── data/
│ ├── orders.csv
│ ├── customers.csv
│ └── orders_customers_joined_pandas.csv
│
├── scripts/
│ ├── block1_join_orders_custoemrs.sql
│ └── block2_pandas_join.py
│
├── dashboard/
│ └── block3_powerbi_base_dashboard.pbix
│
├── notes/
│ └── block4_learning_log.md
│
├── assets/
│ └── day13_dashboard.md
│
└── README.md
```

---

## 🪶 Tags
`#SQL` `#Python` `#PowerBI` `#DummyDataset` `#SalesDashboard` `#PipelineFlow` `#StudyProjectSeries`

---

**End of Day 13 — JOINS**
