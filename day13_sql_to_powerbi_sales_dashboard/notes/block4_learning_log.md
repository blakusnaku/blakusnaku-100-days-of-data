## 🧩 Block 4 – Learning Reflection  
**Day 13 | Base Sales Dashboard (SQL → Python → Power BI)**  
**Date:** October 10, 2025  

---

### 🧠 What I Learned
Today’s session tied together the full data analysis pipeline — from database creation to visualization.  
It was my first time seeing how SQL, Python (pandas), and Power BI complement each other in a real-world workflow.  

1. **SQL (Block 1):**  
   - Created and joined tables (`orders` and `customers`) using `INNER JOIN`.  
   - Practiced translating queries into English one-liners to build intuitive muscle memory.  
   - Understood how relationships between datasets form the foundation of all analysis.

2. **Python (Block 2):**  
   - Re-created the same join in `pandas` using `pd.merge()`.  
   - Learned how data integrity and file paths affect reproducibility.  
   - Experienced the importance of debugging errors (e.g., missing CSV paths, virtual environments, and module imports).

3. **Power BI (Block 3):**  
   - Imported the merged dataset to visualize insights.  
   - Built KPI cards for **Total Orders**, **Total Sales**, and **Average Order Value**.  
   - Created supporting visuals:
     - **Sales by Region** (horizontal bar)
     - **Sales by Customer (₱)** (vertical bar)
   - Added contextual insights and a clean footer signature to transform the dashboard into a mini case study.

---

### 💡 Insights
- **Luzon** leads with ₱2,200 in sales — about **40% of total revenue**.  
- **Anna Santos** is the top customer, contributing **₱1,800** worth of orders.  
- The **“Unknown”** region highlights missing or incomplete data — a potential data cleanup task.  

This process made me realize that dashboards aren’t just about visuals — they’re about *clarity and story*.  

---

### 🎨 Design Takeaways
- Prioritized visual hierarchy: numbers first, explanations second.  
- Used a consistent color palette:  
  - Luzon → 🟧 `#F6A623`  
  - Visayas → 🟦 `#1976D2`  
  - Unknown → ⚪ `#9E9E9E`  
- Added an “💡 Insights” text box for immediate interpretation.  
- Signed the footer:  
  `Block 3 – Base Sales Dashboard | Day 13 | © blakusnaku analytics`

These subtle design decisions made the dashboard feel polished and intentional.

---

### 🧭 Next Steps
- Experiment with DAX measures to compute KPIs directly in Power BI.  
- Add interactivity (filters/slicers for date or region).  
- Apply similar storytelling structure to future datasets — SQL → Python → Power BI → Insights.  

---

**Reflection Summary:**  
> Today, I didn’t just build visuals — I learned how to connect data logic with design clarity.  
> It’s not about showing *everything*, but about showing *what matters most*.

---