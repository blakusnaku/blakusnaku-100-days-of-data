# 📊 DAY 34 — US STR Pipeline: Data Acquisition  
**Date:** 2025-11-01  
**Project:** InsideAirbnb STR Pipeline  
**Phase:** Data Acquisition  
**Tools:** Python (pandas, json, os)  
**Dataset:** InsideAirbnb — New York | Austin | Los Angeles  
**Author:** JP Malit  

---

## 🧩 Overview  
Day 34 initiates the **US Short-Term Rental Pipeline** project using open datasets from **InsideAirbnb**.  
The focus was to establish the foundation for an automated ETL pipeline by planning data sourcing, organizing city-level files, and validating schema consistency across multiple US cities.  
By the end of this stage, the raw datasets were successfully downloaded, structured, and validated through a fault-tolerant schema inspection script.

---

## 🔁 Pipeline Flow  

| Block | Tool | Focus | Output |
|:--|:--|:--|:--|
| **1** | Python | Plan STR data acquisition strategy | Selected US cities (New York, Austin, LA) and identified datasets (listings, calendar, neighbourhoods) |
| **2** | Python | Download and organize datasets | Populated `data/raw/<city_name>/` and created `etl_config.json`, `.gitignore`, and `logs/` folder |
| **3** | Python | Inspect schema and validate keys | Built `schema_validation.py`; generated `run_log.json` with row, column, and unique ID metrics |
| **4** | GitHub | Reflection on open-data use & ethics | Documented compliance and sourcing rationale in `block4_learning_log.md` |

---

## 🧮 Key Learnings  
- **InsideAirbnb Structure:** `listings.csv` ( `id` ) → primary key • `calendar.csv` ( `listing_id` ) → daily availability • `neighbourhoods.csv` → geo lookup  
- **ETL Resilience:** Introduced `load_csv_safe()` to gracefully handle bad files and maintain pipeline continuity.  
- **Schema Validation:** Captured core metrics (rows, columns, column samples, unique IDs) for every file.  
- **Data Health:** 1,024 unique listings validated with full 365-day calendar coverage across all cities.  
- **Transparency:** Used only InsideAirbnb open data in accordance with their usage policy (no scraping).  

---

## 💡 Dashboard Preview (Upcoming)  
Future blocks will transform this validated data into a Power BI dashboard featuring occupancy, ADR, and RevPAR metrics by city.  
The clean calendar-based design will enable daily granular analysis and automated refresh tracking.

---

## 🧭 Study Dashboard Hub  
This project contributes to the ongoing **Study Dashboard Series**, documenting progress across multiple data-analytics disciplines.  
View the full learning dashboard here:  
🔗 [blakusnaku-study-dashboard (GitHub)](https://github.com/blakusnaku/blakusnaku-study-dashboard)

---

## 📁 File Structure  
```bash
day34_us_str_pipeline/
├── assets/
│   └── placeholder.txt
├── data/
│   └── raw/
│       ├── new_york/
│       ├── austin/
│       └── los_angeles/
├── logs/
│   └── run_log.json
├── scripts/
│   └── schema_validation.py
├── notes/
│   └── block4_learning_log.md
└── README.md
```

---

### 🏷️ Tags

#100DaysOfData #Python #ETL #DataEngineering #InsideAirbnb #STRAnalytics #PowerBI #DataPipeline #BlakusnakuAnalytics #StudyDashboard