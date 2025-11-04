# 📊 US Short-Term Rental (STR) Data Pipeline  
**Author:** JP Malit • [@blakusnaku](https://github.com/blakusnaku)  
**Project:** InsideAirbnb STR Pipeline  
**Phase:** Automated ETL → Power BI Dashboard  
**Duration:** Days 34–40 of #100DaysOfData  

---

## 🧠 Overview  
The **US STR Pipeline** is a multi-city ETL system built using **InsideAirbnb** datasets to automate the process of cleaning, validating, merging, and transforming short-term rental data for KPI tracking.  

This project simulates a real-world **analytics engineering workflow**, focusing on configuration-driven architecture, efficient file handling, and scalable data preparation for Power BI visualization.

---

## ⚙️ Architecture  

```
flowchart TD
A[Raw Data (InsideAirbnb)] --> B[Schema Validation (Python)]
B --> C[Cleaning Stage (Numeric + Text Fields)]
C --> D[Standardization + Deduplication]
D --> E[Merging Stage (Listings + Calendar)]
E --> F[Processed Output (Parquet)]
F --> G[Power BI Dashboard (ADR, RevPAR, Occupancy KPIs)]
```

---

## 🧩 Pipeline Flow

| Stage                    | Script                        | Description                                                          | Output                                          |
| :----------------------- | :---------------------------- | :------------------------------------------------------------------- | :---------------------------------------------- |
| **1. Schema Validation** | `schema_validation.py`        | Validates columns, datatypes, and unique IDs across all city files   | `logs/run_log.json`                             |
| **2. Cleaning Stage**    | `cleaning_stage.py`           | Cleans numeric & text fields (`price`, `availability_365`, `rating`) | `data/interim/clean_numeric_text_[city].csv`    |
| **3. Standardization**   | `cleaning_stage.py` (Block 2) | Converts headers to `snake_case` and removes duplicates              | `data/interim/standardized_[city]_listings.csv` |
| **4. Merging Stage**     | `cleaning_stage.py` (Block 3) | Merges listings + calendar per city with chunked processing          | `data/processed/clean_merged_[city].parquet`    |
| **5. Reflection & Logs** | `block4_learning_log.md`      | Daily learnings, design decisions, and pipeline notes                | Markdown summaries                              |

---

## 🧱 Features

✅ Config-Driven Architecture — All paths, cities, and formats controlled through etl_config.json.  
⚙️ Dynamic Output Formats — Switch between .csv.gz and .parquet directly via config.  
🧩 Chunk-Based Merging — Handles millions of rows efficiently without RAM overload.  
⏱️ Performance Tracking — Built-in timers log merge vs. compression time.  
💾 Structured Logging — Every stage writes summary metrics to run_log.json.  
🔁 Modular & Scalable — Each block can run standalone or as a full pipeline.   

---

## 🧮 Key Learnings

• The merge process itself is fast — the main bottleneck was file compression (.csv.gz).  
• Migrating to Parquet (Snappy) made saves 5–10× faster and smaller in size.  
• The ETL config system made city and format switching frictionless.   
• Validation before processing avoids wasted runs and ensures reliability.  
• Data engineering is not just about speed — it’s about building systems that adapt and scale.  

---

## 📅 Project Update Log
> Progress journal for the InsideAirbnb STR Pipeline (Days 34 → 40 of #100DaysOfData)

| 🗓️ Day | 📍 Focus                                 | 🔑 Key Takeaways                                                                                                                                                                                                          |
| :------ | :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **34**  | Data Acquisition                         | Established pipeline foundation, validated schemas, and organized city datasets (NY, Austin, LA). Built `schema_validation.py` for automated schema checks.                                                               |
| **35**  | Cleaning Stage                           | Implemented numeric/text cleaning, header standardization, and chunked merging. Learned about compression bottlenecks and switched output to Parquet. Replaced Austin → Seattle and LA → Portland for smoother iteration. |
| **36**  | Validation & Transformation *(Upcoming)* | Schema alignment checks, lightweight data validation, and Power BI integration prep.                                                                                                                                      |


## 🧮 Study Dashboard Hub  
> This project contributes to the ongoing **Study Dashboard Series**, documenting progress across multiple data analytics disciplines.  
> View the full learning dashboard here:  
> [🔗 blakusnaku-study-dashboard (GitHub)](https://github.com/blakusnaku/blakusnaku-study-dashboard)

## 📁 File Structure
```
us_short_term_rental_data_pipeline/
├── data/
│   ├── raw/
│   │   ├── new_york/
│   │   ├── seattle/
│   │   └── portland/
│   ├── interim/
│   └── processed/
├── logs/
│   └── run_log.json
├── scripts/
│   ├── schema_validation.py
│   └── cleaning_stage.py
├── notes/
│   ├── day34_learning_log.md
│   └── day35_learning_log.md
├── etl_config.json
└── README.md
```
---

## 💡 Dashboard Preview (Upcoming)

The upcoming Power BI dashboard will visualize:
Occupancy Rate
ADR (Average Daily Rate)
RevPAR (Revenue per Available Room)
City comparisons & time-based performance trends

---

## 🧭 Version
`us_str_pipeline v1.0 — Cleaning Stage Complete`
Last Updated: 2025-11-04

---

## 🏷️ Tags
#100DaysOfData #Python #ETL #DataEngineering #Parquet #InsideAirbnb #STRAnalytics #PowerBI #BlakusnakuAnalytics #StudyDashboard
