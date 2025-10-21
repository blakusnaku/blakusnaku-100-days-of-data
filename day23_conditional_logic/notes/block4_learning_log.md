# 🧠 Block 4 — Learning Log  
**Day 23 | October 21, 2025**  
**Theme:** Conditional Logic Across the Pipeline  
**Repository:** [blakusnaku-100-days-of-data](https://github.com/blakusnaku-100-days-of-data)  
**Dataset:** superstore_with_category.csv  
**Phase:** SQL Fundamentals → Python Foundations → Power BI Integration  

---

## 🔹 Overview
Today’s session focused on mastering **conditional logic** across all three tools in the analytics pipeline — from `CASE` statements in SQL, to `np.where()` in Python, and logical category filtering in Power BI.  
The core objective was to ensure consistency of logic flow and visual interpretation across different tools.

---

## 🔸 Pipeline Summary

| Block | Tool | Focus | Output |
|:--:|:--|:--|:--|
| 1 | SQL | Used `CASE WHEN` to categorize sales by value | Classified data as High / Medium / Low |
| 2 | Python | Replicated logic using `np.where()` | Exported `superstore_with_category.csv` |
| 3 | Power BI | Added slicer and visuals for category filtering | “Sales Category Breakdown” dashboard |
| 4 | GitHub | Reflection + Documentation | `learning_log.md`, `README.md`, and repo updates |

---

## 🔸 Key Learnings

1. **Conditional Logic Parity:**  
   Translating logic between SQL (`CASE`) and Python (`np.where()`) deepens understanding of vectorized thinking and ensures data classification stays consistent across platforms.

2. **Dimension Tables for Sorting:**  
   Learned how to implement a **Sort Table (DATATABLE)** and use `RELATED()` to properly order categorical slicers — a professional-level Power BI modeling technique.

3. **Clean Relationship Design:**  
   The one-to-many structure between the lookup (`SalesCategoryOrder`) and fact (`superstore_with_category`) table ensures model scalability and clean filtering logic.

4. **Power BI Visual Continuity:**  
   The orange gradient theme and consistent slicer logic reinforce a clear visual identity across dashboards, strengthening portfolio cohesion.

---

## 💬 Reflections
This block tied together a full logic pipeline from data query to visualization — proof that structured conditional logic can maintain accuracy even across different tools.  
The slicer design, combined with the proper sort table relationship, marks an important step toward professional-grade dashboard modeling.  

Future iterations will focus on improving **KPI presentation** and **slicer interactivity** using conditional formatting, dynamic colors, and iconography for a more polished experience.

---

## 🧭 Footer Insights Summary
**Block 4 — Reflection | Day 23**  
**Dataset:** superstore_with_category.csv | **Updated:** 2025-10-21  
**Toolchain:** SQL → Python (pandas) → Power BI  
**Created by:** JP Malit | © blakusnaku analytics  
**Tagline:** *“Our luck is built from the bricks we lay.”*  
**Hashtags:** #100DaysOfData #SQL #Python #PowerBI #AnalyticsJourney #BlakusnakuAnalytics
