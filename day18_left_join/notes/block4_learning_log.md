# 🧩 Day 18 — LEFT JOIN Practice: Orders & Returns Integration

**Date:** October 16, 2025  
**Phase:** Pipeline Flow  
**Tools:** SQL • Python (pandas) • Power BI  
**Dataset:** Mock Orders & Returns Data (30 Orders, 8 Returns)  
**Author:** [JP Malit (blakusnaku)](https://github.com/blakusnaku)

---

## 🧭 Overview
This study block focused on understanding and visualizing **LEFT JOIN behavior** across the full analytics pipeline.  
The goal was to simulate a real-world *Orders–Returns* relationship — identifying completed vs returned orders using SQL joins, replicating the same logic in Python, and finally visualizing the breakdown in Power BI.

---

## ⚙️ Pipeline Summary

| Block | Tool | Focus | Output |
|:------|:-----|:------|:--------|
| **Block 1** | SQL | Practiced `LEFT JOIN` between `orders` and `returns` | Combined dataset with `NULL` values representing unreturned orders |
| **Block 2** | Python (pandas) | Recreated join logic using `.merge(how="left")` | DataFrame with new `status` column (`Returned` vs `Completed`) |
| **Block 3** | Power BI | Visualized returns vs completed orders | Donut chart + KPI cards with insights and standardized footer |

---

## 📘 Key Learnings

### 🧩 SQL
- Reinforced understanding that `LEFT JOIN` **retains all records** from the left table, even if there’s no match on the right.  
- Used the condition `WHERE r.order_id IS NULL` to isolate unreturned (completed) orders.  
- Learned that missing the `--skip 1` flag during import includes the header row as data — an important cleanup reminder.  

## 🐍 Python (pandas)
- Successfully replicated the SQL join logic using:
  ```
  merged = pd.merge(orders, returns, how='left', on='order_id')
  ```
- Derived a new categorical column to label results:
  ```
  merged['status'] = merged['return_reason'].apply(lambda x: 'Returned' if pd.notnull(x) else 'Completed')
  ```
- Practiced counting grouped outcomes with `.value_counts()` to mirror SQL `GROUP BY` functionality.

## 📊 Power BI

Created a Returns vs Completed Orders Dashboard with:
Two KPI cards for Completed and Returned orders.
Pie chart displaying the proportion of returns.
Applied visual-level filters to make KPIs independent.
Reframed the “Not Returned” label → “Completed” to shift from a neutral to a positive narrative.

Followed Study Dashboard v1.2 layout standards:

Canvas: 1280×720 (16:9)
Layout ratio: Title 15% | Visuals 70% | Footer 15%
Palette: #6BCB77 (Completed) and #FF6B6B (Returned)

---

## 💡 Reflections
Today’s study block solidified my understanding of data relationships and how they directly shape downstream insights.
By moving from SQL → Python → Power BI, I experienced firsthand how consistent logic across tools ensures reliability in reporting.

Renaming “Not Returned” to “Completed” was a subtle but powerful decision — it reframed the analysis to celebrate fulfillment rather than absence. This reinforced the importance of semantic clarity and storytelling tone in data communication.

---

### 🧠 Insights Summary
22 orders (73%) were successfully delivered and marked as Completed.
8 orders (27%) were Returned due to issues like damage or delay.

Practicing LEFT JOIN across multiple tools built confidence in maintaining consistency between SQL queries, pandas merges, and Power BI transformations.
 