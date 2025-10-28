# 🧠 Day 29 Learning Log — STR Listings Pipeline

**Date:** October 25, 2025 (Dashboard Date: 10-27-2025)
**Author:** JP Malit @blakusnaku
**Phase:** STR Analytics Transition
**Dataset:** `hotel_bookings` (Kaggle)
**Repository:** `blakusnaku-100-days-of-data`

---

## 📘 **Overview**

Day 29 marked the transition into the **STR Analytics Phase**, where I began structuring real short-term rental data pipelines.
Instead of focusing on visuals, today’s objective was to understand **how clean datasets flow through SQL → Python → Power BI** — and how relationships form the backbone of analytical design.

---

## 🔁 **Pipeline Summary**

| Block | Tool     | Focus                                               | Output                                         |
| :---- | :------- | :-------------------------------------------------- | :--------------------------------------------- |
| **1** | SQL      | Export snapshot using `LIMIT`                       | `hotel_bookings_snapshot.csv`                  |
| **2** | Python   | Save cleaned `bookings` + `listings` CSVs           | `bookings_cleaned.csv`, `listings_cleaned.csv` |
| **3** | Power BI | Build STRT base model (fact–dimension relationship) | `STR_Analytics_BaseModel.pbix`                 |

---

## 🧬 **Block 1 — SQL ACTION**

**Task:** Write export query with `LIMIT` for listings snapshot
**Goal:** Extract a manageable subset for testing downstream.
**Key Learning:**

* `.mode` and `.import` are meta commands — must be used outside SQL blocks.
* Using `LIMIT` helps validate data structure before heavy loads.
* CSV export confirmed proper column headers and encoding.

✅ **Output:** `data/interim/hotel_bookings_snapshot.csv`

---

## 🧬 **Block 2 — PYTHON ACTION**

**Task:** Save cleaned bookings + listings CSVs
**Goal:** Prepare distinct datasets for modeling in Power BI.
**Key Learning:**

* Cleaned and separated files create a modular workflow for future pipelines.
* `drop_duplicates(subset=["hotel"])` reduced listings to 2 rows — correctly representing unique properties.
* Implemented the **data folder hierarchy best practice** (`raw`, `interim`, `processed`, `external`) to improve pipeline traceability and scalability.

✅ **Outputs:**

* `data/processed/bookings_cleaned.csv`
* `data/processed/listings_cleaned.csv`

---

## 🧬 **Block 3 — POWER BI ACTION**

**Task:** Import listings sample, establish relationships, and validate schema.
**Goal:** Create the foundation for STR Analytics templates.
**Key Learning:**

* Built a clean **Many-to-One** relationship between `bookings_cleaned` (fact) and `listings_cleaned` (dimension) using the `hotel` key.
* Realized this phase is about **conceptual modeling**, not dashboard output.

  > *“Not every Power BI exercise needs to be a full dashboard — the goal is to master structure first.”*
* Confirmed model integrity using KPI, bar, and donut charts.

✅ **Output:**
`dashboard/block3_str_analytics_basemodel`

---

## 🟡 **Pipeline Architecture Update**

Today, I finalized and implemented the new folder hierarchy aligned with industry best practices:

```
data/
├── raw/             ← Original unmodified data
├── interim/         ← Temporary exports or SQL snapshots
├── processed/       ← Cleaned datasets ready for modeling
└── external/        ← Reference or 3rd-party data
```

**Takeaway:**
This structure brings clarity and scalability to my future STR projects, improves automation, and keeps version control cleaner for GitHub commits.

---

## 💡 **Reflections**

* The **data model foundation** is more valuable than a polished visual.
* Learned to prioritize data structure, reproducibility, and clarity.
* The new `data/` hierarchy standardizes my workflow for the rest of the STR Analytics phase.
* My first STR model (bookings + listings) now serves as the base for all future dashboards.

---

## 🗮️ **Footer Insights Summary**

| Aspect             | Reflection                                                         |
| :----------------- | :----------------------------------------------------------------- |
| **Focus**          | Pipeline integrity and folder standardization                      |
| **Lesson Learned** | Folder hierarchy = scalable pipelines                              |
| **Next Step**      | Build `block3_str_analytics_basemodel` for Power BI reuse          |
| **Toolchain**      | SQL → Python → Power BI                                            |
| **Status**         | ✅ Block 1–3 complete — model foundation + architecture established |
