# 📊 Day 29 — STR Listings Pipeline
**Project:** STR Analytics Transition  
**Dataset:** `hotel_bookings` (Kaggle)  
**Date (Dashboard):** 10-27-2025  
**Actual Date:** 10-25-2025  
**Author:** JP Malit @blakusnaku  
**Repository:** `blakusnaku-100-days-of-data`  

---

## 🧭 Overview

Day 29 focuses on building the **STR Listings Pipeline**, marking the start of the STR Analytics Phase.
The goal was to design a modular data flow across SQL → Python → Power BI, emphasizing structure and integrity rather than visuals.
This phase introduces the hotel_bookings dataset as a training model for STR data logic.

---

## 🔁 Pipeline Flow

| Block | Tool     | Focus                                               | Output                                                                       |
| :---- | :------- | :-------------------------------------------------- | :--------------------------------------------------------------------------- |
| **1** | SQL      | Export snapshot using `LIMIT`                       | `data/interim/hotel_bookings_snapshot.csv`                                   |
| **2** | Python   | Save cleaned `bookings` + `listings` CSVs           | `data/processed/bookings_cleaned.csv`, `data/processed/listings_cleaned.csv` |
| **3** | Power BI | Build STRT base model (fact–dimension relationship) | `dashboard/STR_Analytics_BaseModel.pbix`                                     |

---

## 🧩 Key Learnings

* Practiced proper **CSV export and import** flow between SQL and Python.
* Understood the importance of **fact vs. dimension** design in Power BI.
* Implemented the **data folder hierarchy** best practice for scalability:

  ```
  data/
  ├── raw/             ← Original unmodified data
  ├── interim/         ← Temporary exports or SQL snapshots
  ├── processed/       ← Cleaned datasets ready for modeling
  └── external/        ← Reference or 3rd-party data
  ```
* Learned that not every Power BI activity must end in a dashboard — some blocks focus purely on **conceptual modeling**.

---

## 🧠 Insights

> “Not every Power BI exercise needs to be a full dashboard — the goal is to master structure first.”

This day’s work laid the foundation for future STR dashboards by focusing on data relationships, integrity, and standardized pipeline organization.

--- 

## 🧭 Study Dashboard Hub
This project contributes to the ongoing Study Dashboard Series, documenting progress across multiple data analytics disciplines.
View the full learning dashboard here:  
[🔗 View Study Dashboard v1.2](https://docs.google.com/spreadsheets/d/1TLP4skR9L8p8keZBImYdIXdy1Gyl0mBcUqyHPyfwIXE/edit?usp=sharing)

---

## 🧾 File Structure

```
day29_str_listingspipeline/
├── assets/
│
├── data/
│   ├── raw/
│       └── hotel_bookings_cleaned.csv
│   └── interim/
│       └── hotel_bookings_snapshot.csv
│   └── processed/
│       ├── bookings_cleaned.csv
│       └── listings_cleaned.csv
│   └── external/
│
├── dashboard/
│   └── STR_Analytics_BaseModel.pbix
│
├── scripts/
│   ├── block1_sql_action.sql
│   ├── hotel_bookings_schema.sql
│   └── block2_python_action.py
│
├── notes/
│   └── block4_learning_log.md
│
└── README.md
```

---

## 🏷️ Tags

#100DaysOfData #SQL #Python #PowerBI #DataModeling #DataCleaning #BlakusnakuAnalytics #STRAnalytics
