# 🧠 Day 17 — Monthly Trends
**Date:** October 15, 2025  
**Phase:** Pipeline Flow  
**Tools:** SQL • Python (pandas) • Power BI  
**Blocks Covered:** 1–3  

---

## 🧩 Block 1 — SQL: Extract Monthly Totals  
**Objective:** Aggregate monthly sales, profit, and order counts from the Superstore dataset.  
**Key Steps:**
- Loaded `superstore.csv` into SQLite and created a structured table schema.  
- Used `STRFTIME('%Y-%m', order_date)` to group transactions by month and calculate totals for sales, profit, and quantity.  
- Detected a `NULL` group caused by the **header row being imported as data**, and resolved it by deleting the rogue `order_id = 'order_id'` record.  
- Re-exported a clean result as `monthly_totals_raw.csv`.  

**Learning Points:**
- Realized that even properly formatted datasets can include phantom rows if headers are not skipped during import.  
- Strengthened understanding of how SQL reads date formats and how `STRFTIME()` depends on ISO (`YYYY-MM-DD`) formatting.  
- Gained confidence in verifying data integrity through targeted queries like `WHERE STRFTIME('%Y-%m', order_date) IS NULL`.  
- Reinforced that every aggregation query should start with clean, verified data to prevent silent misreads.  

**Result:**  
Successfully produced `monthly_totals_raw.csv`, containing accurate monthly totals with no phantom groups or NULL aggregates.  

---

## 🐍 Block 2 — Python (pandas): Create Month Columns  
**Objective:** Enrich the SQL output with additional columns for month and year context.  
**Key Steps:**
- Loaded the exported `monthly_totals_raw.csv` into pandas.  
- Converted the `month` column into a proper datetime object using `pd.to_datetime(df['month'], format='%Y-%m')`.  
- Created `month_name` and `year` columns for human-readable labels and trend grouping.  
- Reordered columns for clarity and saved the cleaned file as `monthly_totals_clean.csv`.  

**Learning Points:**
- Reinforced confidence with pandas datetime operations (`.dt.year`, `.dt.strftime('%b')`).  
- Learned how pandas automatically handles formatting inconsistencies when using `errors='coerce'`.  
- Understood how intermediate cleaning steps bridge SQL and Power BI by ensuring predictable datatypes.  
- Confirmed that clear column order and naming conventions simplify visualization steps later on.  

**Result:**  
A fully prepared `monthly_totals_clean.csv` — properly formatted, type-validated, and ready for Power BI import.  

---

## 📊 Block 3 — Power BI: Visualize Monthly Trends  
**Objective:** Build a clear time-series line chart showing sales trends per month and year.  
**Key Steps:**
- Imported `monthly_totals_clean.csv` into Power BI.  
- Set **X-axis** to `month` (continuous) and **Legend** to `year` for multi-year trend comparison.  
- Resolved the issue where the chart showed *dots instead of lines* by switching the X-axis to a continuous date field.  
- Applied the **15 | 70 | 15 layout ratio** (Title 108 px | Chart 504 px | Footer 108 px) with standardized footer styling (#F9FAFB background, #DADADA divider).  
- Added insight paragraph summarizing sales seasonality and metadata aligned to the right column.  

**Learning Points:**
- Gained a deeper understanding of how Power BI’s *continuous vs categorical axes* affect chart rendering.  
- Learned the importance of using date-type fields when visualizing time-based data.  
- Strengthened design discipline by maintaining consistent footer layout, typography, and color scheme.  
- Recognized that Power BI visualization is both a technical and aesthetic discipline — clarity is as important as correctness.  

**Result:**  
A completed `Superstore Monthly Sales Trend` dashboard with year-over-year comparison lines and polished footer alignment.  

---

## 💡 Reflections  
Today tied together the full data pipeline — from raw SQL aggregation to pandas enrichment to Power BI visualization.  
The debugging experience with the phantom header row underscored the **critical role of clean imports** in ensuring reliable outputs downstream.  
It also reinforced how structured cleaning and modular design (Block 1–3 handoff) keeps your workflow transparent and reproducible.  
Visually, applying the consistent footer format gave the dashboard a sense of professionalism and identity — a reminder that design cohesion reflects analytical maturity.  

This session deepened the habit of treating **data, visuals, and documentation** as one unified storytelling process rather than separate tasks.  

---

**End of Day 17 Log**  
*Block 1–3 Complete • Block 4 (Reflection) Logged*
