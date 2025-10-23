# 📘 **Day 28 — STR Date Handling & Time Slicer Demo**
**Phase:** STR Analytics (Foundations)  
**Date:** 2025-10-26  
**Toolchain:** SQL → Python → Power BI  
**Dataset:** *Hotel Booking Demand (Kaggle)*  
**Author:** JP Malit  
**Repository:** `blakusnaku-100-days-of-data`

---

## 🧭 **Overview**
Day 28 focused on **date and time handling** within the STR (Short-Term Rental) analytics pipeline.  
The goal was to test extraction and time-based grouping logic across all three layers of the stack — ensuring each stage (SQL, Python, Power BI) handles date fields consistently for downstream visualization and seasonal analysis.  

This study marks the start of a more domain-specific focus on STR performance metrics and booking behavior.

---

## 🔁 **Pipeline Summary**

| Block | Tool | Focus | Output |
|:--|:--|:--|:--|
| 1 | SQL | Tested `YEAR()` and `MONTH()` on `booking_date` | Extracted date parts and validated query syntax |
| 2 | Python | Used `.dt.year` and `.dt.month` on reservation dates | Added derived Year and Month columns |
| 3 | Power BI | Added Year/Month slicers, KPIs, and charts | Built **STR Analytics Dashboard v1 — Date Handling & Time Slicer Demo** |
| 4 | GitHub | Reflection and documentation | This learning log + dashboard deliverable |

---

## 🧠 **Key Learnings**

### 🧩 Data Quality Discoveries
- Found **text placeholders ("NULL")** in `agent` and `company` columns instead of actual null values.  
  → Resolved by replacing `'NULL'` with `np.nan` before applying fill logic.  
- Discovered **"NA"** in `children` column caused type errors in Power BI.  
  → Determined `"NA"` represents zero children → replaced with `0` and cast as integer.  
- Identified one **negative ADR** entry; flagged and excluded it to prevent skewed averages.  

---

### 🔍 Data Handling Insights
- Learned to extract and validate time components using both **SQL (`YEAR()`, `MONTH()`)** and **pandas (`.dt.year`, `.dt.month`)** consistently.  
- Practiced aligning **month sorting** via *Sort by Column* (using numeric month helper).  
- Confirmed the importance of **cross-verifying KPI metrics** (row counts, averages, cancel rates) across SQL, Python, and Power BI for **pipeline integrity**.  
  > *Each stage must reconcile with the previous one — discrepancies reveal weak links in the data chain.*

---

### 🎨 Visualization Insights
- Developed a clear **KPI → Filters → Visuals → Insights** layout hierarchy.  
- Used **clustered bar chart** to compare *City vs Resort* performance — effective for dual-category storytelling.  
- Reinforced Power BI layering workflow using the **Selection Pane** for arranging overlapping visuals.  
- Designed and applied your **standard blakusnaku footer layout**, completing your first STR-branded mock dashboard.

---

## 📊 **Dashboard Preview**
**File:** `dashboard/str_dashboard_mock.pbix`  
**Preview:** `assets/str_dashboard_mock_preview.png`  

![STR Analytics Dashboard v1](assets/str_dashboard_mock_preview.png)

---

## 💡 **Insights Summary**
Seasonality drives distinct ADR patterns across both hotel types.  
Resort Hotels exhibit higher ADR volatility, peaking mid-year due to leisure travel demand.  
City Hotels maintain steadier ADR, reflecting business-oriented consistency.  
Online Travel Agencies dominate bookings overall, though City Hotels sustain stronger Direct and Corporate booking channels.  
This suggests **channel diversification opportunities** and supports future metric development (RevPAR, occupancy rate) for the STR Analytics Phase.

---

## 📘 **Footer Insight Summary**
> Building consistent validation habits at every stage of the pipeline ensures analytical integrity.  
> This session reinforced the mindset that visuals only hold meaning when their upstream data is trusted and verified.

---

## 🏁 **Day 28 Deliverables**
| File | Description |
|:--|:--|
| `scripts/block1_sql_action.sql` | Extracted date parts using `YEAR()` / `MONTH()` |
| `scripts/block2_python_action.py` | Added `.dt.year` and `.dt.month` transformations |
| `dashboard/str_dashboard_mock.pbix` | STR Analytics Dashboard v1 |
| `assets/str_dashboard_mock_preview.png` | Dashboard preview image |
| `notes/block4_learning_log.md` | This learning log |

---

## 🧩 **Next Steps**
- Begin **Day 29** with **extended STR KPI practice** (ADR, RevPAR, Occupancy Rate).  
- Incorporate **date hierarchy visuals** (Year–Month–Day drilldown).  
- Experiment with **Power BI color themes** and custom JSON palettes.

---

### ✳️ Footer
_Block 4 — STR Analytics Foundation | Day 28 | © blakusnaku analytics_  
_Created by JP Malit | #100DaysOfData_
