# 🧠 Day 15 — Profit Margin Analysis  
**Date:** October 13, 2025  
**Phase:** Pipeline Flow
**Tools:** SQL • Python (pandas) • Power BI  
**Blocks Covered:** 1–3  

---

## 🧩 Block 1 — SQL: Create Calculated Profit Column
**Objective:** Add a calculated profit column (`profit_calc`) to simulate a 40% profit margin assumption.  
**Key Steps:**
- Queried the `orders` table from `superstore.db`
- Created a new column `profit_calc = sales * 0.4`
- Compared against the real `Profit` column using a temporary calculated field `diff = profit_calc - profit`

**Learning Points:**
- Discovered that *computed (temporary)* columns using aliases are cleaner than permanently altering a table.
- Realized that temporary calculations let analysts test logic without bloating the database.
- The `diff` column became a powerful moment of insight — showing the difference between “data storage” vs “data expression”.

**Result:**  
First working SQL comparison of simulated vs. actual profit margins.  

---

## 🐍 Block 2 — Python (pandas): Replicating the Calculation
**Objective:** Recreate the same transformation flow using pandas for data cleaning and validation.  
**Key Steps:**
- Loaded `superstore.csv` into pandas  
- Cleaned `sales` and `profit` columns using `.astype(str)`, `.str.replace()`, and `pd.to_numeric()`  
- Added `profit_calc` and `diff` columns  
- Exported the cleaned dataset as `superstore_with_profit.csv`  

**Learning Points:**
- Understood how `errors="coerce"` replaces bad rows with `NaN` to avoid crashes.
- Gained clarity on how `isna().sum()` works — each `True` (NaN) counts as 1 and is summed for a quick data-quality snapshot.
- Realized the `int()` wrapper converts NumPy integers to native Python integers for cleaner printing and logging.
- Reinforced how pandas mirrors SQL logic (`ALTER`, `UPDATE`, `SELECT`, `AS`) in a Pythonic way.

**Result:**  
Successfully exported a clean, analysis-ready dataset for Power BI.  

---

## 📊 Block 3 — Power BI: Profit Margin Dashboard
**Objective:** Visualize the simulated vs. actual profit comparison.  
**Key Steps:**
- Imported `superstore_with_profit.csv`
- Built 4 KPI cards: **Total Sales**, **Total Profit**, **Simulated Profit (40%)**, **Average Difference**
- Designed a clustered column chart comparing `Profit` vs `Profit_Calc` by `Category`
- Added concise insights and a standardized footer for visual consistency  

**Learning Points:**
- Refined understanding of dashboard hierarchy (Title → KPI → Chart → Insights → Footer).
- Experimented with layout proportions (Title 10% | KPI 20% | Chart 55% | Footer 15%) for balanced design.
- Learned when chart titles are optional when a strong page title already sets context.
- Strengthened visual storytelling through consistent footer branding (`© blakusnaku analytics | Study Project Series`).

**Result:**  
A clean, cohesive Power BI dashboard showcasing simulated vs actual profitability — ready for portfolio presentation.

---

## 💡 Reflections
- This session deepened my *self-discovery learning approach*: guided exploration > passive instruction.  
- Found that structured experimentation (Block 1–4) builds momentum and retention far better than theory-heavy lessons.  
- Realized that consistency, reflection, and curiosity matter more than speed — each “aha” (like discovering the diff column) compounds over time.  
- Noticed that the SQL → Python → Power BI flow mirrors real-world analytics pipelines: **query → clean → visualize**.  

---

**End of Day 15 Log**  
*Block 1–3 Complete • Block 4 (Reflection) Logged*  