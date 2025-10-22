# 📊 Superstore Dashboard Development Log (Day 26)
**Phase:** BI Mastery — Superstore Capstone  
**Date:** 2025-10-26  
**Dataset:** Superstore Clean Final (Stage 3 → Stage 4)  
**Author:** JP Malit  
**Repository:** blakusnaku-100-days-of-data  

---

## 🧭 Overview
This document records the design, structure, and insights of the **Superstore Performance Dashboard (v1.0)** created in Power BI.  
It represents the culmination of the data preparation and validation work from **Day 25**, translating cleaned data into a clear, insight-driven executive dashboard.

---

## 🔁 Pipeline Flow
| Block | Tool | Focus | Output |
|-------|------|--------|--------|
| 1 | SQL | Schema creation & final export | `superstore_clean_stage3.csv` |
| 2 | Python | Validation & profiling | `python_sql_validation_log.md` |
| 3 | Power BI | Dashboard design & insights | `superstore_dashboard_v1.pbix` |
| 4 | GitHub | Documentation & reflection | `day26_dashboard_log.md` + README update |

---

## 🎯 Dashboard Goal
To present a **nationwide business performance overview** that helps stakeholders identify:
- Top- and bottom-performing regions and states  
- Profitability by product category  
- National sales and profit trends over time  
- Discount and order distribution patterns  

---

## 🧱 Dashboard Structure

| Section | Visual | Metric(s) | Purpose |
|----------|---------|------------|----------|
| **Header KPIs** | Cards | Total Sales, Total Profit, Order Count, Average Discount | Provide immediate snapshot of business performance |
| **Regional Sales** | Horizontal bar | Sales + Profit by Region | Compare regional revenue and profitability |
| **Sales by Category** | Vertical bar | Sales + Profit by Category | Assess product-level performance |
| **Top 5 States** | Horizontal bar (blue) | Sales + Profit | Identify strongest state-level contributors |
| **Bottom 5 States** | Horizontal bar (gray) | Sales + Profit | Highlight underperforming states |
| **Sales Trend** | Line chart | Sales by Year, Quarter, Month, Day | Track historical trends and seasonal behavior |
| **Footer Insights** | Text card | Narrative summary + metadata | Communicate key takeaways and maintain traceability |

---

## 💡 Insights Summary
> Western and Eastern regions drive **60% of total sales**, led by **California** and **New York**.  
> Profit margins are highest in **Technology** and lowest in **Furniture**.  
> Smaller states such as **Wyoming**, **Maine**, and **West Virginia** show consistent losses, but their impact remains minimal.  
> Sales trends reveal stable activity from 2015–2017, with periodic spikes during promotional months.  
> Discounts average **15.6%**, which correlates with higher order volumes but reduced profit per unit.

---

## 🧩 Design & Style Guide
| Element | Standard | Notes |
|----------|-----------|-------|
| **Font** | Segoe UI / Poppins | 10–12pt body, 16pt titles |
| **Color Palette** | #FF914D (main), #FFD3A1, #F9FAFB, #7A7A7A, #333333 | Follows *blakusnaku Orange* standard |
| **Layout Ratio** | Header 15% • KPIs 20% • Visuals 50% • Footer 15% | Clean, balanced composition |
| **Footer Format** | Two-column insight + metadata | Matches BI Mastery visual identity |
| **File Naming** | `superstore_dashboard_v1.pbix` | Version control for design evolution |

---

## 🗂️ File Outputs
| File | Description |
|------|-------------|
| `dashboard/superstore_dashboard_v1.pbix` | Final Power BI file |
| `assets/superstore_dashboard_v1.png` | Screenshot for documentation |
| `data/superstore_clean_stage3.csv` | Validated dataset used for dashboard |
| `notes/sql_schema_log.md` | SQL schema and export documentation |
| `notes/python_sql_validation_log.md` | Python validation results |
| `notes/day26_dashboard_log.md` | This log file (dashboard summary) |

---

## 🧠 Footer — Standardized Layout Reference
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

✅ **Status:**  
`superstore_dashboard_v1` is officially completed and validated as part of **Day 26 — BI Mastery Phase**.  
Next step: Day 27 will focus on documentation, GitHub integration, and publishing reflections.


