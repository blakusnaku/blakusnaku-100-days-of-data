# 🧩 Day 22 – Multi-Table Modeling (Orders, Shipping, Returns)

### 📅 Date: October 21, 2025  
**Phase:** SQL → Python → Power BI → Documentation  
**Author:** JP Malit (@blakusnaku)  

---

## 🧭 Overview
Day 22 focused on **multi-table modeling** using the custom **Orders**, **Shipping Cost**, and **Returns** datasets. The goal was to simulate a real relational data pipeline — from SQL creation to Python merging and Power BI relationship modeling — showcasing how clean joins enable deeper business insights.

---

## 🔗 Pipeline Summary

| Block | Tool | Focus | Output |
|:------|:-----|:-------|:--------|
| **Block 1** | SQL | Created schemas and practiced JOINs | `orders`, `shipping_cost`, and `returns` tables generated |
| **Block 2** | Python | Merged three tables and validated relationships | `merged_orders.csv` exported for Power BI |
| **Block 3** | Power BI | Built data model and interactive visuals | Multi-table dashboard with return-rate and cost analysis |
| **Block 4** | GitHub | Documented workflow and insights | `learning_log.md` and updated `README.md` |

---

## 🧠 Key Learnings
- Multi-table setups mirror real database design and encourage thinking in relationships, not flat files.  
- Matching **keys and data types** across all sources prevents join errors and missing data.  
- Power BI’s **relationship view** makes SQL logic visual and intuitive.  
- Calculating **Return Rate = [Returned Orders] / COUNTROWS(Orders)** introduced practical DAX use.  
- Maintaining numeric fields free of formatting symbols ensures smoother merges.

---

## 💭 Reflections
Day 22 connected the dots between your technical phases — SQL logic, Python data prep, and Power BI modeling — into one end-to-end system. Seeing the data link seamlessly across tools reinforced why structured design and data integrity matter for scalable analytics.

---

## 🧩 Footer Insights Summary
💡 **Insights:**  
This dashboard connects **Orders**, **Shipping**, and **Returns** tables to reveal real business relationships. It highlights **return rates**, **shipping cost impact**, and **sales trends** while emphasizing clean joins and consistent data types across SQL, Python, and Power BI.

---

**Block 3 — Multi-Table Modeling Dashboard | Day 22 | © blakusnaku analytics**  
Dataset: Orders + Shipping + Returns | Updated: 2025-10-21  
Figures in ₱ (Philippine Peso) | Toolchain: SQL → Python (pandas) → Power BI  
Created by JP Malit | #100DaysOfData
