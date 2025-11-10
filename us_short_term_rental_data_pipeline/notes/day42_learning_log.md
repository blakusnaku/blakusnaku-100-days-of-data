# 🧠 Day 42 Learning Log — Feature Extraction & Amenity Insights  
**Date:** 2025-11-09  
**Phase:** Data Analysis — Feature Exploration  
**Project:** US Short-Term Rental (STR) Data Pipeline  
**Author:** JP Malit  

---

## 📦 Overview  
Today's focus was on enriching the dataset with **amenity-based features** and analyzing their relationship with **ADR (Average Daily Rate)**.  
The goal was to extract text-based insights from listing descriptions, quantify amenity presence, and visualize how these features correlate with revenue performance.

---

## 🔹 Block 1 — Extract Amenity Keywords  
- Combined `description` and `amenities` columns from each city’s harmonized listings into a single **text blob** for keyword detection.  
- Used a predefined keyword list (wifi, pool, gym, kitchen, balcony, etc.) and searched within the text blob using regex.  
- Each detected amenity became a new Boolean column (`amenity_<keyword>`).  
- Created an `amenity_count` column to quantify the total amenities per listing.  

✅ **Output:** `data/interim/str_market_with_amenities_v1.parquet`  
✅ **Result:** 27 amenity flags created, with an average of **10.26 amenities per listing**.  

🧠 *Key Insight:* Many amenity mentions appear in descriptions, not titles — combining text sources significantly improved detection accuracy.

---

## 🔹 Block 2 — Compute Amenity Impact  
- Counted how many listings mentioned each amenity.  
- Calculated the **average ADR** of listings containing each amenity using:  
```
  df.loc[df[col] == True, "adr"].mean()
```
(this filtered rows where the amenity was True and computed ADR averages).

Saved results as amenity_impact_summary.csv for later visualization.

✅ Output: data/interim/amenity_impact_summary.csv
✅ Key Metrics: Each record includes amenity name, number of listings mentioning it, and mean ADR.

---

## 🔹 Block 3 — Visualize Amenity Frequency vs ADR
• Created a horizontal bar chart showing Average ADR per Amenity.
• Highlighted the top 15 amenities by frequency.
• Exported visualization as a static PNG for review.
✅ Output: `data/interim/amenity_vs_adr_chart.png`
✅ Visualization Goal: Identify high-ADR amenities (e.g., pool, view, balcony) that contribute most to revenue lift.

---

## 💡 Key Learnings
• Text parsing is a powerful tool for feature engineering — you can derive structured variables from unstructured text.
• .loc[] is essential for targeted row-column filtering when computing conditional metrics.
• Small regex details (\b boundaries, re.escape) make extraction more accurate and reduce false positives.
• Combining amenities and ADR gives actionable business insights: “Which amenities justify premium pricing?”
• Learned that cleaning and preprocessing textual features is just as critical as numeric cleaning for robust models.

---

## 🧩 Next Steps
• Extend amenity analysis to include sentiment keywords (e.g., “cozy”, “luxury”, “spacious”).
• Integrate this enriched dataset into Power BI for visual comparisons across cities.
• Add dual-axis charts (ADR vs. listing count) to explore trade-offs between popularity and profitability.

---

**Output Files:**
```
data/interim/str_market_with_amenities_v1.parquet  
data/interim/amenity_impact_summary.csv  
data/interim/amenity_vs_adr_chart.png
```

---

**✅ Day 42 Complete — Feature Extraction Phase Concluded**
*The pipeline now produces structured amenity-based metrics ready for BI analysis.*