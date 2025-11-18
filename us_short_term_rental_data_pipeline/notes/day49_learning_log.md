# Day 49 — BI Mastery (Power BI Dashboard Expansion)
**Date:** 2025-11-16  
**Block:** Full-Day BI Visual Development  
**Project:** US STR Pipeline — Power BI Dashboard  
**Author:** JP Malit  
**Repo:** blakusnaku-100-days-of-data

---

## 🧩 Overview
Today’s session focused on enhancing the Power BI dashboard by adding KPI cards, comparison visuals, interactive slicers, and ensuring the model behaves cleanly when filtering. This was the first day where the visual layer started forming into a usable analytics experience.

---

## 📌 Block 1 — KPI Cards (ADR, RevPAR, Occupancy %)
- Added core KPI cards for:
  - **ADR (Average Daily Rate)**
  - **RevPAR (Revenue per Available Room)**
  - **Occupancy %**
- Verified that all cards reflect the DAX measures created in Day 47.
- Confirmed they respond correctly to city-level and category filters.

**Key Learning:**  
Clean, validated measures immediately translate to clean visuals. The metric layer we built earlier makes the KPI zone reliable.

---

## 📌 Block 2 — Comparison Charts (City vs Property Type)
- Built:
  - **Top 10 Property Types by ADR**
  - **Top 10 Property Types by RevPAR**
- Implemented ranking using:
  ```
  ADR Rank =
  RANKX(
      ALL(listings[property_type]),
      [Avg ADR],
      ,
      DESC
  )
  ```
  - Filtered charts to show only Top 10.
  - Both visuals now react smoothly to city and room type filters.

**Key Learning:**
Top N visuals paired with dynamic measures create strong storytelling for performance comparison.

---

## 📌 Block 3 — Slicers (City, Property Type, Season)
- Added slicers for:
    - City
    - Property Type
    - Room Type
    - Season (future-ready for simulated seasonal pricing)
- Encountered a repeating issue: slicers showing (Blank).
- Root cause discovered:
    calendar_raw contained unmatched listing_id rows, causing Power BI to auto-generate a virtual blank category through relationship propagation.
- Temporary fix: Disconnected the calendar table to prevent unwanted blank values.
We will reconnect this table after nightly pricing is simulated.

**Key Learning:**
A slicer showing (Blank) does not always mean the column has blanks—often it comes from incomplete or mismatched relationships.

---

## 📌 Block 4 — Reflection & Insights

Today advanced the STR dashboard’s interactivity and structure. Debugging the slicer blanks reinforced how crucial model relationships are in shaping Power BI behavior.

**Next steps:**
- Build dimension tables (CityDim, PropertyTypeDim, RoomTypeDim).
- Reconnect calendar after simulated dynamic nightly pricing.
- Start sculpting the dashboard layout with finalized components.
The dashboard is evolving from raw output into a structured analytical tool.

--- 

## 📂 Files Updated
- str_dashboard.pbix
- day49_learning_log.md

---

## 🧠 Key Takeaways
- Relationship mismatches can create phantom (Blank) categories.
- Top N measures + filtering = clean comparison visuals.
- Metric integrity drives visual accuracy.
- Simplifying relationships improves the user experience.
- Seasonal/dynamic pricing simulation will complete the STR time-series analysis.