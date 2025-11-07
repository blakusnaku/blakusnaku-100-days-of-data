# 📘 Day 37 — Data Validation & Quality Assurance (2025-11-04)

## 🗂️ Phase
Data Acquisition → Validation Stage

## 🧩 Overview
Today focused on validating the integrity of the consolidated STR dataset before transformation and KPI modeling.  
After merging multiple cities into a unified master file, this stage ensured that data completeness, missing values, and numeric logic were consistent across all records.  

This marks the final step in the Data Acquisition phase — the pipeline now officially produces an analysis-ready dataset.

---

## ⚙️ Pipeline Flow
| Block | Script | Focus | Output |
|:--|:--|:--|:--|
| 1 | `validate_data_completeness.py` | Checked null values and completeness across all columns | `data_quality_report.csv` |
| 2 | `validate_missing_outliers.py` | Treated missing values and capped numeric outliers | `validated_master_v2.parquet` |
| 3 | `validate_numeric_consistency.py` | Verified ADR, occupancy %, and rating logic | `numeric_validation_report.csv` |
| 4 | Reflection | Summarized data quality findings | `validation_reflection.md` |

---

## 🧠 Key Learnings
- **Completeness Auditing:** Generating a column-level null summary helped identify empty or redundant fields like `calendar_updated`.
- **Controlled Cleaning:** Learned to differentiate between *data loss* (dropping rows) and *schema refinement* (dropping empty columns).
- **Capped Extremes:** Implemented IQR-based outlier treatment for price and logical capping for `availability_365`.
- **Schema Alignment Realization:** Detected that the listing ID (`id`) persisted across earlier stages — fixed by standardizing it to `listing_id` during harmonization.
- **Metric Validation:** Derived key metrics (`adr`, `occupancy_pct`) and confirmed their logical range and behavior across all cities.

---

## 📊 Outputs
- `/data/interim/data_quality_report.csv`
- `/data/interim/validated_master_v2.parquet`
- `/data/interim/numeric_validation_report.csv`
- `/notes/validation_reflection.md`

---

## 📈 City-Level Summary (Block 3)
| City | Listings | Avg Price (ADR) | Median Price | Avg Occupancy % | Avg Rating |
|:--|--:|--:|--:|--:|--:|
| New York City, NY | 1,024 | 115.24 | 105.00 | 36.82 | 4.81 |
| Seattle, WA | 6,862 | 197.74 | 164.50 | 45.55 | 4.83 |
| Portland, OR | 4,425 | 140.40 | 123.00 | 41.30 | 4.87 |

---

## 🧩 Reflections
Today’s session brought everything full circle for the acquisition pipeline.  
Detecting the missing `listing_id` and realizing it stemmed from the harmonization branch helped me understand how *schema drift* can quietly propagate downstream.  
The validation step proved that modular checks (nulls → outliers → logic) build confidence in data readiness before even touching visualization or KPIs.  
I can now trust that the dataset reflects reality — not just technically valid, but logically sound.

---

## ✅ Next Steps
- Transition to the **Transformation & KPI Calculation Phase**
- Compute and validate business KPIs (ADR, Occupancy, RevPAR)
- Begin dashboard model design for Power BI integration

---

### 🧭 Summary
> Day 37 concluded the validation loop of the STR Pipeline.  
> The dataset is now harmonized, imputed, bounded, and logically consistent — ready to move into the Transformation phase and start generating true business insights.
