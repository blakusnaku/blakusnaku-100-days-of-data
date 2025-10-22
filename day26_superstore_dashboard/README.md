# 📊 Day 26 — Superstore Performance Dashboard  
**Phase:** BI Mastery — Superstore Capstone  
**Date:** 2025-10-26  
**Dataset:** Superstore Clean Final (Stage 3 → Stage 4)  
**Author:** JP Malit  
**Repository:** blakusnaku-100-days-of-data  

---

## 🧭 Overview  
Day 26 marks the completion of the **Superstore Capstone Dashboard (v1.0)** — the first fully validated, end-to-end business intelligence project in the 100 Days of Data journey.  
This dashboard consolidates SQL, Python, and Power BI workflows into a single analytical pipeline, turning raw transactional data into actionable business insights.

---

## 🔁 Pipeline Flow  

| Block | Tool | Focus | Output |
|--------|------|--------|--------|
| 1 | SQL | Schema creation & data export | `superstore_clean_stage3.csv` |
| 2 | Python | Validation & profiling | `python_sql_validation_log.md` |
| 3 | Power BI | Dashboard design & insight generation | `superstore_dashboard_v1.pbix` |
| 4 | GitHub | Documentation & publishing | `day26_dashboard_log.md` + README |

---

## 🎯 Objective  
To create an **executive-level performance dashboard** summarizing national sales, profitability, and discount trends across regions, states, and categories.  
The focus is to align data clarity with business context — translating cleaned Superstore data into **storytelling visuals** that highlight performance patterns and improvement areas.

---

## 📊 Dashboard Overview  

![Superstore Dashboard v1](assets/superstore_dashboard_v1.png)

| Section | Visual | Metrics | Purpose |
|----------|---------|----------|----------|
| **Header KPIs** | Cards | Total Sales, Total Profit, Order Count, Avg. Discount | Snapshot of business health |
| **Regional Sales** | Horizontal bar | Sales + Profit by Region | Compare performance across regions |
| **Sales by Category** | Vertical bar | Sales + Profit by Category | Evaluate product profitability |
| **Top 5 States** | Horizontal bar (blue) | Sales + Profit | Identify leading contributors |
| **Bottom 5 States** | Horizontal bar (gray) | Sales + Profit | Highlight underperforming regions |
| **Sales Trend** | Line chart | Sales over time | Track historical patterns (2014–2017) |
| **Insights Footer** | Text field | Business summary + metadata | Communicate findings clearly |

---

## 💡 Key Insights  

> 🧠 Western and Eastern regions account for nearly **60% of total sales**, led by **California** and **New York**.  
> Technology remains the most profitable category, while Furniture shows thinner margins.  
> **Wyoming, Maine, and West Virginia** reflect localized losses, but with limited business impact.  
> Discounts average **15.6%**, indicating strong promotion-driven sales with slight profit compression.  
> The dashboard demonstrates consistent data flow and metric alignment across **SQL → Python → Power BI**.

---

## 🧩 Design Standards  

| Element | Standard | Notes |
|----------|-----------|-------|
| **Font** | Segoe UI / Poppins | 10–12pt body, 16pt titles |
| **Color Palette** | #FF914D (main), #FFD3A1, #F9FAFB, #7A7A7A, #333333 | blakusnaku Orange |
| **Footer Format** | Two-column layout | Left: insights • Right: metadata |
| **Layout Ratio** | Title 15% | KPI/Charts 70% | Footer 15% |
| **Dashboard File** | `superstore_dashboard_v1.pbix` | Version-controlled |
| **Export File** | `superstore_clean_stage4.csv` | Validated input dataset |

---

## 🗂️ File Structure  
```
day26_superstore_dashboard/
├── assets/
│ └── superstore_dashboard_v1.png
│
├── dashboard/
│ └── superstore_dashboard_v1.pbix
│
├── data/
│ ├── superstore_clean_stage2.csv
│ ├── superstore_clean_stage3.csv
│ ├── superstore_clean_final.csv
│ └── superstore.db
│
├── notes/
│ ├── python_sql_validation_log.md
│ ├── sql_schema_log.md
│ └── day26_dashboard_log.md
│
├── scripts/
│ ├── block1_superstore_schema.sql
│ └── block2_python_sql_import.py
│
└── README.md
```
---

## 🧠 Footer (Standardized Layout)
```
💡 Insights:
Western and Eastern regions drive 60% of total sales, led by California and New York.
Losses remain low and localized to smaller states, suggesting stable profitability.

📂 Dataset: Superstore
📅 Date Updated: 2025-10-26
📊 Toolchain: SQL → Python → Power BI
🧭 Layout Ratio: Title 15% | KPI/Charts 70% | Footer 15%
📁 Version: superstore_dashboard_v1
```

---

## 💬 Reflections  
Completing this dashboard marks a key transition point — from learning tools individually to **synthesizing them into a cohesive analytical pipeline**.  
It reinforced that:
- Data cleaning is only as valuable as the business clarity it enables.  
- Design discipline (layout, color, typography) enhances interpretability.  
- Every dataset should end with a story — not just a table.

---

✅ **Status:**  
`superstore_dashboard_v1` successfully completed and validated.  
Next → **Day 27:** Documentation, GitHub push, and capstone reflection.