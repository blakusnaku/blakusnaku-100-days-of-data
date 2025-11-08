# 📦 Data Acquisition Workflow — US Short-Term Rental (STR) Pipeline

**Project:** US STR Data Pipeline  
**Phase:** Data Acquisition  
**Date:** 2025-11-07  
**Author:** JP Malit  
**Repository:** [blakusnaku-100-days-of-data](#)  
**Datasets:** InsideAirbnb (New York | Seattle | Portland)  
**Tools:** Python (pandas, json, os, sqlite3), SQL  

---

## 🧩 Overview
The **Data Acquisition Phase** establishes the foundation of the STR Pipeline, ensuring every dataset—listings, calendar, and reviews—is validated, cleaned, harmonized, and stored in a structured database.  

This phase converts messy raw CSVs into **query-ready, BI-ready datasets** while maintaining schema consistency and logging at each step.  
All processing steps are modular and reproducible through a single command:

```
python automation_pipeline.py
```

---

## ⚙️ Pipeline Flow
| Stage | Script                                          | Description                                                                     | Output                                           |
| :---- | :---------------------------------------------- | :------------------------------------------------------------------------------ | :----------------------------------------------- |
| 1     | `schema_validation.py`                          | Checks structure and column integrity of all raw InsideAirbnb files             | `run_log.json` (validation summary)              |
| 2     | `cleaning_stage.py`                             | Cleans numeric/text fields, standardizes headers, merges listings + calendar    | `clean_merged_<city>.parquet`                    |
| 3     | `harmonize_schemas.py`                          | Aligns schemas across all cities and adds `city_key` and `city_display` columns | `harmonized_<city>_listings.csv`                 |
| 4     | `merge_listings_calendar.py`                    | Consolidates listings + calendar per city into merged datasets                  | `clean_merged_<city>.parquet`                    |
| 5     | `validate_missing_outliers.py`                  | Detects missing values, nulls, and extreme outliers                             | `validated_master_v2.parquet`                    |
| 6     | `validate_numeric_consistency.py`               | Confirms logical consistency (ADR, occupancy %, ratings)                        | `numeric_validation_report.csv`                  |
| 7     | `calculate_kpis.py` + `generate_kpi_summary.py` | Builds STR performance metrics (ADR, RevPAR, LOS, occupancy)                    | `kpi_dataset_v1.parquet`, `city_kpi_summary.csv` |
| 8     | `import_to_sqlite.py`                           | Loads cleaned datasets into SQLite (`str_market.db`)                            | Database ready for BI queries                    |
| 9     | `verify_sql_import.py`                          | Cross-checks database vs CSV/Parquet row counts                                 | Integrity verified                               |

---

## 🧠 Key Highlights
• Config-Driven Architecture: etl_config.json controls directories, compression, and pipeline mode (test vs production).
• Reproducible Workflows: Every script can run independently or via automation_pipeline.py.
• End-to-End Logging: run_log.json records results of each stage for traceability.
• Scalable Design: Modular structure mirrors enterprise ETL patterns (clean → validate → store → analyze).
• BI Readiness: All datasets standardized to Power BI-compatible formats (Parquet and SQLite).

---

## 📊 Final Outputs

| Output                                     | Description                                            |
| :----------------------------------------- | :----------------------------------------------------- |
| `data/interim/validated_master_v2.parquet` | Cleaned and validated dataset ready for transformation |
| `data/interim/kpi_dataset_v1.parquet`      | KPI-enriched dataset with ADR, RevPAR, Occupancy, LOS  |
| `data/str_market.db`                       | SQLite database with listings + calendar tables        |
| `data/interim/city_kpi_summary.csv`        | City-level performance overview                        |
| `logs/run_log.json`                        | Comprehensive execution and validation log             |

---

## 🚀 Next Phase — Transformation & Visualization

With the Data Acquisition Phase complete, the next steps are to:
1. Build transformation scripts for aggregations and city-level trend calculations.
2. Connect Power BI directly to str_market.db and str_market_ready.parquet.
3. Automate nightly refreshes for continuous KPI tracking.

**Version:** v1.0 — Data Acquisition Complete
**© blakusnaku analytics**