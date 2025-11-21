# 📊 US Short-Term Rental (STR) Data Pipeline  
**Author:** JP Malit • [@blakusnaku](https://github.com/blakusnaku)  
**Project:** InsideAirbnb STR Pipeline  
**Phase:** Automated ETL → Power BI Dashboard  
**Duration:** Days 34–40 of #100DaysOfData  

---

## 📊 Dashboard Preview

![Short Term Rental Dashboard](https://github.com/blakusnaku/blakusnaku-100-days-of-data/blob/main/us_short_term_rental_data_pipeline/assets/us_short_term_rental_dashboard_screenshot.PNG)

---

## 🧠 Overview  
The **US STR Pipeline** is a multi-city ETL system built using **InsideAirbnb** datasets to automate the process of cleaning, validating, merging, and transforming short-term rental data for KPI tracking.  

This project simulates a real-world **analytics engineering workflow**, focusing on configuration-driven architecture, efficient file handling, and scalable data preparation for Power BI visualization.

---

## ⚙️ Architecture  
```
A[Raw Data (InsideAirbnb)] --> B[Schema Validation (Python)]
B --> C[Cleaning Stage (Numeric + Text Fields)]
C --> D[Standardization + Deduplication]
D --> E[Merging Stage (Listings + Calendar)]
E --> F[Validation & KPI Calculation]
F --> G[Database Integration (SQLite)]
G --> H[Processed Output (Parquet)]
H --> I[Power BI Dashboard (ADR, RevPAR, Occupancy KPIs)]
```

---

## 🧩 Pipeline Flow

| Stage                        | Script                            | Description                                                                                 | Output                                          |
| :---------------------------- | :-------------------------------- | :------------------------------------------------------------------------------------------ | :---------------------------------------------- |
| **1. Schema Validation**     | `schema_validation.py`            | Validates columns, datatypes, and unique IDs across all city files                         | `logs/run_log.json`                             |
| **2. Cleaning Stage**        | `cleaning_stage.py`               | Cleans numeric/text fields (`price`, `availability_365`, `rating`)                          | `data/interim/clean_numeric_text_[city].csv`    |
| **3. Standardization**       | `cleaning_stage.py` (Block 2)     | Converts headers to `snake_case` and removes duplicates                                    | `data/interim/standardized_[city]_listings.csv` |
| **4. Merge Listings + Cal**  | `cleaning_stage.py` (Block 3)     | Merges listings + calendar with chunked mode for large datasets                             | `data/interim/clean_merged_[city].parquet`      |
| **5. Schema Harmonization**  | `harmonize_schemas.py`            | Aligns schemas and adds city metadata columns                                               | `data/interim/harmonized_[city]_listings.csv`   |
| **6. KPI Calculation**       | `calculate_kpis.py`               | Computes `ADR`, `RevPAR`, `Occupancy`, `LOS` metrics                                        | `data/interim/kpi_dataset_v1.parquet`           |
| **7. Database Integration**  | `import_to_sqlite.py`             | Imports harmonized & calendar data into SQLite                                              | `data/str_market.db`                            |
| **8. Verification**          | `verify_sql_import.py`            | Confirms database row counts vs. file counts                                                | `logs/run_log.json`                             |
| **9. BI Export**             | `export_bi_dataset.py`            | Merges KPI + listings into final BI-ready dataset                                           | `data/processed/str_market_ready.parquet`       |

---

## 🧱 Features  

✅ **Config-Driven Architecture** — Centralized `etl_config.json` controls all paths, cities, and formats  
⚙️ **Dynamic Output Formats** — Switch between `.csv.gz` and `.parquet` directly from config  
🧩 **Chunk-Based Merging** — Handles millions of rows efficiently without RAM overload  
💾 **Structured Logging** — Every stage writes summary metrics to `run_log.json`  
⏱️ **Performance Tracking** — Built-in timers for merge and compression speed  
🔁 **Reproducible Pipeline** — Entire process runs end-to-end via `automation_pipeline.py`  
📈 **BI-Ready Outputs** — Final dataset exported for Power BI integration  

---

## 🧮 Key Learnings  

- Switching from `.csv.gz` to **Parquet (Snappy)** drastically improved I/O speed and compression efficiency.  
- Column name conflicts in merges can silently drop fields — fixed using `suffixes=("", "_kpi")`.  
- End-to-end reproducibility validated by running the **entire ETL-to-SQL pipeline** in production mode.  
- Validation before processing ensures reliable downstream BI performance.  
- Debugging merge behavior clarified how pandas handles overlapping columns, key types, and suffixes.  

---

## 📅 Project Update Log  
> Progress journal for the InsideAirbnb STR Pipeline (Days 34 → 40 of #100DaysOfData)

| 🗓️ Day | 📍 Focus                                   | 🔑 Key Takeaways                                                                                                                                                                                                 |
| :------ | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **34**  | Data Acquisition Setup                    | Established pipeline foundation, validated schemas, and organized city datasets (NY, Seattle, Portland). Built `schema_validation.py` for automated schema checks.                                              |
| **35**  | Cleaning Stage                             | Implemented numeric/text cleaning, header standardization, and chunked merging. Switched to Parquet for better performance and compression.                                                                     |
| **36**  | Harmonization                              | Added city columns and schema alignment across all datasets. Established modular design where each script serves as a reusable block.                                                                          |
| **37**  | Validation                                 | Checked nulls, missing values, and numeric consistency. Built validation scripts for data completeness and logical integrity.                                             |
| **38**  | KPI Calculation                            | Computed ADR, RevPAR, Occupancy, and LOS metrics. Modularized KPI functions for future datasets and created per-city KPI summaries.                                      |
| **39**  | Database Integration                       | Created SQLite schema, imported harmonized and merged datasets, and verified row counts. Confirmed full ETL→SQL pipeline reproducibility.                                |
| **40**  | BI Export + Debugging                      | Exported final BI-ready dataset (`str_market_ready.parquet`). Fixed merge conflicts with suffix handling. Verified end-to-end production run without errors. 🚀           |

---

## 🧮 Study Dashboard Hub  
> This project contributes to the ongoing **Study Dashboard Series**, documenting progress across multiple data analytics disciplines.  
> View the full learning dashboard here:  
> [🔗 blakusnaku-study-dashboard (GitHub)](https://github.com/blakusnaku/blakusnaku-study-dashboard)

---

## 📁 File Structure  
```
us_short_term_rental_data_pipeline/
├── data/
│ ├── raw/
│ │ ├── new_york/
│ │ ├── seattle/
│ │ └── portland/
│ ├── interim/
│ └── processed/
├── logs/
│ └── run_log.json
├── scripts/
│ ├── schema_validation.py
│ ├── cleaning_stage.py
│ ├── harmonize_schemas.py
│ ├── calculate_kpis.py
│ ├── import_to_sqlite.py
│ ├── verify_sql_import.py
│ └── export_bi_dataset.py
├── notes/
│ ├── day34_learning_log.md
│ ├── day35_learning_log.md
│ ├── day36_learning_log.md
│ ├── day37_learning_log.md
│ ├── day38_learning_log.md
│ ├── day39_learning_log.md
│ └── day40_learning_log.md
├── etl_config.json
└── README.md
```

---

## 💡 Dashboard Preview (Upcoming)  

The upcoming Power BI dashboard will visualize:  
- Occupancy Rate (%)  
- ADR (Average Daily Rate)  
- RevPAR (Revenue per Available Room)  
- City-level and property-type performance trends  
- Interactive metrics with dynamic filters for hosts and regions  

---

## 🧭 Version  
`us_str_pipeline v1.1 — Data Acquisition Complete`  
**Last Updated:** 2025-11-07  

---

## 🏷️ Tags  
#100DaysOfData #Python #ETL #DataEngineering #Parquet #InsideAirbnb #STRAnalytics #PowerBI #BlakusnakuAnalytics #StudyDashboard

