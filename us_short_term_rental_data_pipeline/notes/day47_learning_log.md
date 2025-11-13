# 📘 day47_learning_log.md
**Date:** 2025-11-14  
**Phase:** BI Mastery  
**Focus:** DAX Metrics • Segmentation Columns • KPI Validation  

---

## 🧩 What I Worked On Today
Today focused on strengthening the Power BI metric layer by building validated DAX measures and adding segmentation fields for deeper STR analysis. I created DAX measures for ADR, RevPAR, Occupancy %, and LOS — and verified that all of them match the outputs from my Python + SQL pipeline, confirming full model consistency.

I also added calculated columns like `city_group`, `price_band`, `review_score_band`, and `property_category`, which set up the dashboard for richer slicing and business-focused insights.

---

## 🧠 Key Learnings

### **1. Difference Between DAX Measures vs Columns**
I confirmed that the KPI cards I built earlier were already functioning as true DAX measures.  
- Measures recalculate dynamically depending on report filters  
- Calculated columns are static and stored in the table  
This clarified why KPIs must always be measures, not columns.

---

### **2. Understanding SWITCH(TRUE())**
I learned how `SWITCH(TRUE())` works as a cleaner alternative to nested IF statements.  
It allows me to define range-based logic in an organized way — perfect for segmentation like:
- price bands  
- review score tiers  
- occupancy buckets  
This structure is more readable and easier to maintain.

---

### **3. Creating Analytical Segmentation Columns**
I added several segmentation fields to enrich the STR dashboard:
- **city_group** → East vs West  
- **price_band** → Low / Mid / High / Luxury  
- **review_score_band** → Poor / Average / Good / Excellent  
- **property_category** → Home, Private Room, Shared Room, Hotel/Hospitality, Unique Stay, Apartment  

These fields are essential for storytelling, comparisons, and slicing KPIs meaningfully.

---

### **4. Validating DAX vs Python/SQL**
All my DAX measures matched the Python + SQL results exactly:
- ADR  
- RevPAR  
- Occupancy %  
- LOS  

This confirms:  
✔ My ETL pipeline is correct  
✔ SQLite import is clean  
✔ Power BI relationships are correct  
✔ My DAX logic is accurate  

This was a big confidence boost and validates the end-to-end system.

---

## 🚧 Challenges / Improvements
- Learning when to use DAX columns vs Power Query  
- Structuring categories in a scalable, business-minded way  
- Building intuition for segmentation and data modeling  

---

## 🚀 Next Steps
- Build comparison visuals using the new segmentation columns  
- Create KPI cards and slicers using the new bands  
- Start designing the STR Market Overview layout and theme  
- Prepare the dashboard for insights storytelling  

---

## 📝 Reflection
Today felt like everything finally clicked — Python, SQLite, and Power BI are now talking to each other cleanly. The segmentation work made me realize how much dashboards depend on thoughtful business logic, not just raw numbers.

This block solidified my understanding of how DAX fits into the overall STR pipeline, and it sets the stage for more advanced visuals and insights in the next BI blocks.

