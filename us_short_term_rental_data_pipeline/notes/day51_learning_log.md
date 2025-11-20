# 📘 Day 51 — KPI Modeling (Stage 4)
**Date:** 2025-11-18  
**Project:** US STR Pipeline (InsideAirbnb)  
**Phase:** Stage 4 — KPI Modeling  
**Author:** JP Malit (@blakusnaku)  

---

## 🧠 Overview  
After completing the *original* STR pipeline a few days ago, I realized something important — while the outputs were correct, the structure itself wasn’t scalable. There were redundancies, repeated logic, and too many hardcoded sections. It worked, but it wasn’t the kind of pipeline I could easily maintain, extend, or automate long-term.

So before moving on to the visualization and automation stages, I made the decision to **rework the processing phase** from the ground up. The goal was clear:

> Make the STR pipeline *modular, configurable, and efficient.*

Today, I completed **Stage 4: KPI Modeling** using this new modular architecture. The transformations, KPI formulas, ADR/RevPAR simulation, and aggregation steps now run cleanly across all cities using consistent, reusable modules. The pipeline finally feels like something that can scale.

---

## 🔁 Pipeline Flow Today  
1. Loaded transformed dataset per city  
2. Computed listing-level KPIs through a dedicated module  
3. Concatenated all listing KPIs across cities  
4. Computed city-level metrics  
5. Saved all outputs under `data/kpi/`  
6. Confirmed BI-readiness of the KPI layer  

---

## 🧩 Key Learnings  

### **1. Refactoring the old pipeline was absolutely worth it**  
By modularizing the entire processing chain:
- cleaner → harmonizer → transformer → kpi  
the system became significantly easier to debug and reuse.  
One config change now updates the whole pipeline.

### **2. KPI modeling depends heavily on proper feature engineering**  
Fields such as:
- `listing_age_days`  
- `reviews_per_month_calc`  
- normalized categories  

are essential for stable KPI calculations. Missing any of these breaks the model.

### **3. ADR Simulation (Option C) is a strong first iteration**  
The hybrid approach (room-type baseline + bedroom/bathroom scaling) keeps ADR realistic without needing nightly rate data.

### **4. Treating each city independently but structuring them with shared modules feels “enterprise-grade”**  
Once harmonized and transformed, all cities can flow through identical KPI logic without special cases.

### **5. Config-driven KPI modeling = future-proofing**  
Pricing multipliers and weights are now adjustable via `etl_config.json`, not code. This makes tuning and iteration much easier.

---

## 🛠 What I Implemented  

### **Listing-level KPIs:**
- `reviews_per_month_calc`
- `engagement_score`
- `occupancy_score`
- `simulated_adr`
- `simulated_revpar`
- safe numeric handling

### **City-level KPIs:**
- market size  
- average ADR (simulated)  
- average RevPAR  
- average engagement  
- average review rating  
- room-type distribution  

Outputs stored in:
```
data/kpi/
```


---

## 🚧 Challenges & Fixes  

### **1. Old pipeline assumptions no longer apply**  
Many earlier bugs came from relying on inconsistent city schemas.  
The new harmonization layer fixed this cleanly.

### **2. Series vs scalar conflicts**  
Several KPI formulas had to be rewritten to use vectorized operations.

### **3. ADR simulation edge cases**  
Handled `NA`, missing bedrooms, and ambiguous values safely.

### **4. Runtime warnings from fillna**  
Updated to modern pandas-safe patterns.

---

## 🎯 Next Steps  
**Stage 5 — Visualization Prep (Power BI)**  
- Build the star schema  
- Finalize fact/dimension tables  
- Sync listing and KPI outputs  
- Prepare the dashboard’s metrics layer  
- Begin layout design (KPI grid, ADR/RevPAR visuals, maps)

This is where the pipeline finally becomes something that users can interact with visually.

---

## 🧡 Reflection  
Refactoring this pipeline was one of the best decisions I made. The old STR workflow *worked*, but it wasn’t something I’d trust in a real Data Engineering environment. Today, the structure feels clean, modular, and scalable — the kind of system I can extend, automate, and improve over time.

KPI modeling made everything “click.”  
Before, I was processing data.  
Now, I’m generating **insights**.

That shift in mindset is what today was really about.

---

