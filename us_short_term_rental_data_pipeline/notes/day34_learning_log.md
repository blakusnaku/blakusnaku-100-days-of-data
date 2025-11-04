# 🧠 BLOCK 4 — Learning Log  
**Day 34 | 2025-11-01**  
**Phase:** Data Acquisition  
**Project:** US STR Pipeline (InsideAirbnb)  
**Toolchain:** Python → GitHub  
**Cities:** New York | Austin | Los Angeles  

---

## 🧩 Overview
Day 34 marked the start of the US-based STR pipeline project using **InsideAirbnb open datasets**.  
The objective was to plan, collect, and validate raw data from three target cities to establish a reliable foundation for an automated ETL and dashboard system.  
By the end of the day, the pipeline could safely load, inspect, and log schema details for each city’s datasets.

---

## ⚙️ Pipeline Summary
| Block | Tool | Focus | Output |
|:--|:--|:--|:--|
| 1 | Python | Plan data acquisition strategy | Finalized US-only InsideAirbnb source (New York, Austin, LA) |
| 2 | Python | Download and organize datasets | Created `etl_config.json`, structured data/raw folders, set up logs |
| 3 | Python | Inspect schema and validate keys | Built `schema_validation.py`, generated `run_log.json` |
| 4 | GitHub | Reflection & ethics | Documented open-data sourcing principles |

---

## 🧮 Key Learnings
- **InsideAirbnb Data Model:**  
  - `listings.csv` → primary listing info (`id`)  
  - `calendar.csv` → daily availability (`listing_id`)  
  - `neighbourhoods.csv` → geo context for visual filters.  
- **ETL Resilience:**  
  Implemented `load_csv_safe()` to prevent crashes on corrupted or missing files.  
- **Schema Validation:**  
  Logged `rows`, `columns`, and `unique_id` to check data integrity and detect duplicates.  
- **Relationship Insight:**  
  Calendar data contains ≈ 365 rows per listing → a daily availability timeline rather than bookings only.  
- **Logging Mechanism:**  
  `run_log.json` serves as a persistent ETL audit trail for future automation and data-health tracking.

---

## 💭 Reflections
Shifting to US cities felt strategic and aligned with future client markets.  
The open-data approach keeps the project transparent and compliant, while the calendar-based design opens doors for deep STR analytics like occupancy and RevPAR.  
Understanding the ETL flow from config loading to run logging provided a clear mental map of how future pipeline blocks will connect.  
This foundation sets the stage for automated cleaning and transformation next.

---

## 🧠 Footer Insights Summary
**Data Integrity:** All 1,024 listings have unique IDs; calendar data covers ~365 days per listing (100% coverage).  
**Audit Trail:** `run_log.json` captures schema snapshots for each ETL run.  
**Ethics:** Data sourced solely from InsideAirbnb’s open datasets — no direct scraping.  
**Next Steps:** Design data cleaning logic and validation scripts for transformation phase.  

---

© 2025 blakusnaku analytics | Day 34 — US STR Pipeline v1.0  
