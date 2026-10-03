# E-Commerce Customer Segmentation Dashboard - RFM Analysis

## Project Overview
* This project performs customer segmentation for an e-commerce business using RFM Analysis to differentiate between Regular and Lost customers.

## Dataset Used
Originally 4 tables were available, but only 2 tables were used for final analysis as they were sufficient:

1.  **Orders Table** - Used for Recency & Frequency calculation (Customer ID, Order Date)
2.  **Payments Table** - Used for Monetary calculation & Total Revenue (Customer ID, Payment Value)

Remaining 2 unused tables were removed from the Power BI model to optimize performance and keep the dashboard clean.

## Key Insights from Dashboard
- Total Customers: 99.44K
- Total Revenue: $16.01M
- Lost Customers: 90K (90.48% of base) - Main contributor to historical revenue
- Regular Customers: Only 1K (1.14%) - Generating $182.28K
- Major Churn Identified - Business needs to focus on re-engagement.

## RFM Logic
- **Recency:** Calculated from Orders table (Last Order Date)
- **Frequency:** Count of Orders per Customer
- **Monetary:** Sum of Payment Value from Payments table

## Dashboard Features
- KPI Card 1: Count of customer_id
- KPI Card 2: Sum of Monetary (Total Revenue)
- Bar Chart: Customer Count by Segment
- Donut Chart: Revenue by Segment

## Tech Stack
- Power BI Desktop
- Data Modeling (Relationship between Orders & Payments)
- DAX

## How to Run
1. Download .pbix file
2. Open in Power BI Desktop
3. Data model contains only Orders & Payments tables.

