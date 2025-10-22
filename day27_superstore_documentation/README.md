# 🏪 Superstore Sales Analytics — Final Capstone  
**Phase:** BI Mastery (Days 24–27)  
**Author:** JP Malit  
**Repository:** blakusnaku-100-days-of-data  
**Dataset:** Superstore (Clean Final)  

---

## 🧭 Overview  
The **Superstore Capstone Project** represents the culmination of the BI Mastery phase — integrating SQL, Python, and Power BI into a complete end-to-end analytics pipeline.  
This project demonstrates the workflow of a real-world data analyst: transforming raw transactional data into business insights that address performance and profitability questions.

---

## 🧩 Objectives  

1. Identify key **business pains** using client-style framing.  
2. Build a **validated and traceable dataset** through Excel → SQL → Python.  
3. Develop a **Power BI dashboard** that visualizes actionable insights for regional, product, and discount performance.  
4. Deliver **documentation and reproducibility** across all stages.

---

## 🔁 Pipeline Flow  

| Step | Tool | Output |
|------|------|---------|
| 1️⃣ | Excel | `superstore_clean_stage1.csv` — Cleaned and formatted dataset |
| 2️⃣ | SQL (SQLite via VS Code) | Schema creation + data validation (`superstore.db`) |
| 3️⃣ | Python (pandas) | Data profiling and integrity checks |
| 4️⃣ | Power BI | Final interactive dashboard (`superstore_dashboard_v1.pbix`) |
| 5️⃣ | GitHub | Documentation, logs, and portfolio publishing |

---

## 💡 Key Insights  

| Category | Highlight |
|-----------|------------|
| **Top-Performing Regions** | Western & Eastern regions generate ~60 % of total sales. |
| **Low-Performing Regions** | Central & South show lower profit margins — high discount impact. |
| **Top States** | California, New York, and Washington drive highest sales. |
| **Bottom States** | Wyoming, Maine, and West Virginia consistently record losses. |
| **Category Profitability** | Technology leads profit margins; Furniture lags despite sales volume. |
| **Discount Behavior** | Avg. discount ≈ 15.6 %; heavy discounting correlates with reduced profitability. |

---

## 📊 Dashboard Overview  

**Core KPIs**
- Total Sales  
- Total Profit  
- Total Quantity Sold  
- Average Discount  

**Visual Highlights**
- Regional Performance Bar Chart  
- Category-Level Profit Comparison  
- Top 5 & Bottom 5 States by Profit  
- Yearly Sales Trend Line  

---

## 🎨 Design Standards  

| Element | Style |
|----------|-------|
| **Color Palette** | blakusnaku Orange (#FF914D → #FFF2E9) |
| **Font** | Segoe UI / Poppins |
| **Layout Ratio** | Title 15 %  |  Charts 70 %  |  Footer 15 % |
| **Footer Format** | Left: Insights summary  •  Right: Metadata (Block #, Day #, Dataset, Author) |

---

## 🧠 Business Impact  
This dashboard provides a data-driven lens for managerial decision-making:
- Prioritize profitable categories and high-performing regions.  
- Reassess discount strategy to preserve margins.  
- Identify underperforming states for targeted sales or shipping strategy improvements.  

---

## 🗂️ File Structure  
```
day27_superstore_documentation/
├── assets/
│ └── superstore_dashboard_v1.png
├── dashboard/
│ └── superstore_dashboard_v1.pbix
├── data/
│ ├── superstore_clean_stage3.csv
│ ├── superstore_clean_stage4.csv
│ └── superstore.db
├── notes/
│ ├── data_cleaning_log.md
│ ├── sql_schema_log.md
│ ├── python_sql_validation_log.md
│ ├── day26_dashboard_log.md
│ └── day27_reflection.md
└── README.md
```

---

## 🧾 Documentation Links  

| File | Description |
|------|--------------|
| [`data_cleaning_log.md`](notes/data_cleaning_log.md) | Excel cleaning and formatting protocol |
| [`sql_schema_log.md`](notes/sql_schema_log.md) | Schema creation + SQL validation |
| [`python_sql_validation_log.md`](notes/python_sql_validation_log.md) | Python verification and profiling |
| [`day26_dashboard_log.md`](notes/day26_dashboard_log.md) | Power BI layout and design process |
| [`day27_reflection.md`](notes/day27_reflection.md) | Final project reflection summary |

---

## 🚀 Next Phase  
The Superstore Capstone concludes the **BI Mastery Phase**.  
Next up: **Short-Term Rental (STR) Analytics Phase**, applying automation, pricing, and forecasting to real-world datasets for portfolio expansion.

---

**Created by JP Malit | #100DaysOfData | blakusnaku analytics**

