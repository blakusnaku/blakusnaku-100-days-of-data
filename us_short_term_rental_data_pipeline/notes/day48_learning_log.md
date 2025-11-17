# Day 48 — BI Mastery: Time Intelligence & Data Model Validation  
**Date:** 2025-11-15  
**Project:** US STR Data Pipeline  
**Block:** BI Mastery (Power BI Time Intelligence)  
**Author:** JP Malit  

---

## 📝 Overview  
Today’s focus was on expanding the STR BI model with proper **time intelligence foundations**, building a Date table, linking it with the model, and validating Month-to-Date (MTD) and Year-to-Date (YTD) DAX calculations. This block also surfaced an important insight about the InsideAirbnb dataset that will affect future work.

---

## 📌 Block Summary

### **Block 1 — Created the Date Table with DAX**  
- Built a complete Date table using `CALENDAR()`  
- Added time features (Year, Quarter, Month, Week, etc.)  
- Positioned it at the top of the model as the time backbone for STR analysis  

### **Block 2 — Established Proper Relationships**  
- Connected `Date[Date]` to `calendar_raw[date]`  
- Ensured one-way filtering from Date → Calendar → Listings  
- Confirmed Power BI now recognizes time hierarchy and supports time intelligence

### **Block 3 — Implemented YTD / MTD Measures**  
- Created MTD and YTD versions of ADR and Occupancy  
- Organized all metrics inside a **STR_Measures** table  
- Validated formulas against Python + SQL outputs  
- Verified consistency across tools  

### **Block 4 — Learning Log & Reflection Commit**  
- Documented workflow, discoveries, and next steps  

---

## 🔍 Key Learning  
### **InsideAirbnb Does *Not* Provide Daily Price Values in `calendar.csv`**  
During testing, we found that for all cities examined (New York, Seattle, Portland, Austin, London, Paris, etc.), the `calendar.csv` files **do not contain daily price or adjusted_price values**.

This means:

- No daily ADR  
- No seasonality patterns  
- No event-driven price shifts  
- No dynamic price curves over time  

This limits true STR analysis because base prices alone cannot represent market behavior.

---

## 💡 Strategic Decision  
Once the STR Dashboard is complete, we will:

### **Build a simulated dynamic pricing engine**  
This pricing layer will:  
- Generate daily prices for each listing  
- Apply seasonality patterns  
- Use occupancy-based adjustments  
- Add property-type multipliers  
- Feed realistic time-series pricing into Power BI  

This simulation will unlock:  
- ADR seasonality  
- Revenue curves  
- YTD/M YTD trend visuals  
- Forecasting opportunities  
- More realistic STR insights  

---

## 📘 What I Learned Today  
- Time intelligence requires a clean Date table + correct relationships  
- Measures should live inside a dedicated Metrics table  
- Always validate DAX calculations against Python/SQL  
- Dataset limitations can be opportunities for engineered solutions  
- Real analytics often require augmenting missing reality with simulation  

---

## 🧭 Next Steps  
- Finish STR Dashboard KPI visuals  
- Begin designing the Dynamic Pricing Simulation Engine  
- Add a config toggle (`simulate_pricing: true/false`)  
- Reconnect Power BI to the simulated calendar once ready  

---
