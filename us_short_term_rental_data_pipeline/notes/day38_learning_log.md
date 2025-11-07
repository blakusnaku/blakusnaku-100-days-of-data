# 📘 Day 38 — KPI Computation & City Performance Summary (2025-11-05)

## 🗂️ Phase
Data Acquisition → KPI Transformation

## 🧩 Overview
Today I transformed the validated multi-city dataset into a metrics-ready layer and produced city-level performance KPIs. Core metrics include ADR, Occupancy %, RevPAR, and a LOS proxy. All computations are now modularized for reuse on future InsideAirbnb drops.

---

## ⚙️ Pipeline Flow
| Block | Script | Focus | Output |
|:--|:--|:--|:--|
| 1 | `calculate_kpis.py` | Compute ADR, Occupancy%, RevPAR, LOS | `data/interim/kpi_dataset_v1.parquet` |
| 2 | `metrics_utils.py` | Reusable KPI functions & city summary helper | (functions) |
| 3 | `generate_kpi_summary.py` | Aggregate KPIs at city level | `data/interim/city_kpi_summary.csv` |
| 4 | Reflection | Document insights & next steps | `notes/kpi_learning_log.md` |

Dataset used: `data/interim/validated_master_v2.parquet` → **12,311 rows, 80 cols**  
KPI layer produced: `data/interim/kpi_dataset_v1.parquet` → **12,311 rows, 84 cols**

---

## 📈 City KPI Summary
_Source: `data/interim/city_kpi_summary.csv`_

| City | Listings | Avg ADR | Avg Occupancy % | Avg RevPAR | Avg LOS |
|:--|--:|--:|--:|--:|--:|
| New York City, NY | 1,024 | 115.24 | 36.82 | 44.28 | 11.01 |
| Portland, OR | 4,425 | 140.40 | 41.30 | 53.86 | 14.03 |
| Seattle, WA | 6,862 | 197.74 | 45.55 | 84.48 | 11.47 |

**Notes:**
- Seattle leads ADR and RevPAR; Portland shows the highest LOS proxy among the three.
- Occupancy proxies (derived from `availability_365`) stay within 0–100% bounds as expected.
- Medians and means are reasonably close, indicating outlier capping worked.

---

## 🧠 Key Learnings
- Centralizing formulas in `metrics_utils.py` prevents logic drift and makes upgrades trivial.
- RevPAR responds predictably to both ADR and occupancy — quick health check for each city.
- Maintaining a **validated base** vs **metrics layer** keeps lineage clear and audits simple.

---

## ✅ Next Steps
- Add rolling (30/90/365) variants for ADR/RevPAR.
- Introduce revenue proxy per listing: `revpar * 365`.
- Prepare the Power BI model (fact table from `kpi_dataset_v1.parquet`, city dim).
- Consider percentile cuts for ADR and occupancy to profile listing tiers.
