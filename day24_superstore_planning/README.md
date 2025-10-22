# 📊 Day 24 — Superstore Final Project: Planning & Scope  
> Framing the Superstore dataset as a real-world business intelligence engagement.

🧭 **Phase:** BI Mastery — Superstore Capstone  
📅 **Date:** 2025-10-23  
🛠️ **Tools:** Markdown, SQL, Power BI  
📂 **Dataset:** Superstore Final (Cleaned)  
👤 **Author:** JP Malit  
🔗 **Repository:** blakusnaku-100-days-of-data  

---

## 🎯 Overview
Today marks the beginning of the **Superstore Final Project**, the capstone for the BI Mastery phase of the #100DaysOfData journey.  
This project repositions the Superstore dataset as if it were provided by a real client — focusing not just on technical execution, but on **business understanding, problem framing, and strategic insight design**.

The purpose of this planning phase is to define *what problems the business might be facing*, *what we can offer as analysts*, and *how data analytics can influence better decisions.*

---

## 🧩 Pipeline Flow
| Block | Tool | Focus | Output |
|--------|-------|--------|---------|
| 1 | Discussion / Markdown | Identify business pains and goals | Problem statement |
| 2 | SQL / Python | Map analytical deliverables | KPI and metric plan |
| 3 | Power BI | Draft dashboard layout wireframe | Visual strategy sketch |
| 4 | GitHub / Markdown | Write planning documentation | `superstore_finale_planning.md` |

---

## 💼 Business Context
The **Superstore** dataset represents a multi-category retail business operating across several U.S. regions.  
The company has provided its transaction history — including orders, discounts, and shipping data — to identify patterns that affect profitability and growth.

This mirrors a real-world situation where a retail client engages a BI analyst to **diagnose hidden inefficiencies** and **uncover growth levers** through data.

---

## 🔍 Business Pains — Analyst Reasoning

Through experience working with the Superstore dataset, several patterns often emerge that reflect common operational challenges in retail:

| Pain | Description | Implication |
|------|--------------|-------------|
| Inconsistent Profitability | Sales volume doesn’t always align with profit margins. | Indicates pricing or discount inefficiency. |
| Uncontrolled Discounting | Discount rates vary unpredictably. | Potential revenue loss due to unmanaged promotions. |
| Regional Imbalance | Performance differs greatly between regions. | Poor demand forecasting or supply allocation. |
| Shipping Inefficiency | Shipping costs inconsistent with profit contribution. | Operational cost leakage. |
| Fragmented Segmentation | No clear understanding of customer types. | Missed retention or targeting opportunities. |

---

## 🧠 Analyst’s Role in Context

In real client engagements, analysts rarely start with data alone — they start with **questions**.

### **Business-Driven Projects**
The client defines the problem (“profits are dropping”), and the analyst reframes it into measurable data questions.  
> “Which product lines or regions show declining profit margins despite stable sales?”

### **Data-Driven Projects**
The analyst explores the dataset to surface unspoken or hidden issues.  
> “We noticed high discounts correlate with low profit — this may be an underlying pain.”

### **Real-World Balance**
Most projects blend both: the client sets direction, and the analyst refines focus using data evidence.  
This project simulates a **data-driven discovery** — where the dataset is the starting point, and insights shape the narrative.

---

## 💡 Analytical Deliverables
| Objective | Metric / KPI | Method |
|------------|---------------|--------|
| Identify high/low performing regions | Total Sales, Profit by Region | SQL GROUP BY + Power BI visual |
| Analyze discount impact | Profit Margin vs Discount | Python correlation + Power BI scatter |
| Track customer segment performance | Sales by Segment | DAX measure, filtered view |
| Monitor fulfillment efficiency | Shipping Cost vs Profit | SQL view, Power BI combo chart |

---

## 🧭 Dashboard Strategy
**Title:** “Superstore Performance Overview”  

**Planned Sections:**
1. KPI Summary (Sales, Profit, Orders, Discounts)  
2. Regional Performance (map or bar visual)  
3. Product Category Profitability  
4. Discount and Profit Correlation  
5. Top 10 Customers / Products  
6. Insights Footer — Business Takeaways  

---

## 🧡 Dashboard Footer (Preview)
```
💡 Insights: This dashboard aims to uncover how product mix, regional trends, and discount strategies affect profit performance.

📂 Dataset: Superstore Final (Cleaned)
📅 Date Updated: 2025-10-23
📊 Toolchain: SQL → Python (pandas) → Power BI
🧭 Layout Ratio: Title 15% | KPIs 70% | Footer 15%
📁 Version: superstore_capstone_v1.0
Created by JP Malit | #100DaysOfData
```

---

## 🪞 Reflection
This phase reaffirms the **core of business intelligence work** — translating data into understanding.  
It’s less about queries and charts, and more about diagnosing how a business operates and where it can improve.  
Tomorrow’s focus will shift from framing the problems to verifying them through **data validation and model setup**.

---

📘 **Related File:** [`notes/superstore_finale_planning.md`](../notes/superstore_finale_planning.md)  
© blakusnaku analytics | #100DaysOfData