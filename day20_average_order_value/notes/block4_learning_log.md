# 🧠 Day 20 — Learning Log  
**Project:** Average Order Value Dashboard (Superstore Dataset)  
**Date:** October 19, 2025  
**Phase:** Integration & Dashboard Design  
**Tools:** SQL • Python (pandas) • Power BI  
**Dataset:** Superstore (Cleaned)  
**Author:** JP Malit (blakusnaku)

---

## 🧩 Overview  
Today’s focus was on computing and visualizing the **Average Order Value (AOV)** — a key business metric showing how much a customer spends per order.  
The process connected multiple tools: SQL for querying totals, Python for verification and data export, and Power BI for final visualization and storytelling.

---

## ⚙️ Pipeline Summary  

| Block | Tool | Focus | Output |
|:------|:-----|:------|:--------|
| **Block 1** | SQL | Calculated total sales, total orders, and derived AOV (`total_sales / total_orders`) | Verified AOV = ₱458.61 |
| **Block 2** | Python | Recalculated AOV using pandas for cross-validation | Confirmed same ₱458.61 after cleaning numeric fields |
| **Block 3** | Power BI | Created AOV KPI card and regional comparison chart | Built 4 KPI cards + “AOV by Region” visual |
| **Block 4** | GitHub | Documentation and reflection | Updated README, footer, and color identity |

---

## 🔑 Key Learnings  

- Some numeric fields (e.g., `sales`, `profit`) weren’t being read properly due to commas.  
  → Learned that **best practice is to remove commas and formatting symbols** before processing numeric data.  
- Updated the Superstore dataset by converting `order_date` and `ship_date` to the standard `YYYY-MM-DD` format for consistency.  
- Reinforced the importance of consistent **lower_snake_case** column naming to avoid mismatches across SQL, Python, and Power BI.  
- Learned how to **create relationships** in Power BI (Many-to-One using `customer_id`) to connect the main dataset (`superstore_clean`) with the summary dataset (`aov_per_customer`).  
- Observed how Power BI’s default aggregations can differ (average of averages vs. weighted average) and learned when to use DAX for more accurate measures.  
- Decided to **pause DAX** for now and focus on building portfolio visuals, with plans to integrate DAX-based AOV in a future version.  
- Finalized the **blakusnaku Orange** color palette — an orange gradient with soft neutrals — as the **official visual identity** for all dashboards moving forward.  

---

## 💬 Reflections  

This dashboard marks a major milestone: the first version built under my **consistent design system and brand color identity**.  
It not only consolidates SQL and Python workflows into Power BI visuals but also strengthens my ability to build dynamic relationships and organize metric logic cleanly.  

The dataset cleaning process revealed subtle issues with numeric and date formatting — a reminder that reliable analytics always begins with clean data.  
Power BI’s visual structure is now aligned with the Study Dashboard standard, and today’s orange theme truly gives it a professional, cohesive feel.  

Next step: explore **DAX for weighted AOV and time-based trends**, then integrate additional segmentation visuals for deeper analysis.

---

## 🧾 Footer Insights Summary  

**💡 Insights:**  
Customers spend an average of ₱460 per order, showing minimal variance across regions.  
This indicates stable purchasing patterns and consistent pricing strategies across territories.  

**📁 Version:** superstore_aov_dashboard_v1.0  
**📅 Updated:** 2025-10-19  
**🔗 Toolchain:** SQL → Python (pandas) → Power BI  
**🎨 Theme:** blakusnaku Orange (Signature Palette)  
**🧭 Layout:** KPI Row 30% | Chart 55% | Footer 15%  
**© blakusnaku analytics | #100DaysOfData**
