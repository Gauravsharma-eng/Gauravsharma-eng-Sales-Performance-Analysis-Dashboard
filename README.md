# Sales Performance Analysis Dashboard

An end-to-end analysis of retail sales data using **SQL** and **Power BI**. The goal was to understand revenue and profit trends, find the best-performing products and categories, and see how demand changes by season.

## Dataset
- 10,500 retail orders from Jan 2023 to Dec 2024
- Columns: order_id, order_date, segment, region, category, sub_category, product, quantity, discount, sales, profit
- This is a **sample dataset generated for practice** (see `generate_data.py`), not real company data

## Tools
SQL (SQLite), Power BI (DAX, Power Query), Python (data generation only)

## What I did
1. Loaded and cleaned the data (date formats, duplicates, missing values)
2. Wrote SQL queries for KPIs, monthly growth, category and product performance, and seasonal demand (`analysis_queries.sql`)
3. Built an interactive Power BI dashboard with revenue, profit margin and monthly growth rate (steps in `POWER_BI_STEPS.md`)

## Key findings
- Total revenue is about 16.4 Cr with a profit margin of 11.9%
- Technology brings the most revenue (about 9.2 Cr), but Office Supplies has the best margin (24.7%)
- Smartphone X is the top-selling product by revenue
- Average monthly sales in Oct to Dec are about 16% higher than the rest of the year, so inventory and pricing should be planned before Q4

## Dashboard
![Dashboard](screenshots/dashboard.png)

A quick web preview of the main charts is also in `Sales_Dashboard.html`.

## Files
| File | Description |
|---|---|
| `sales_data.csv` | Dataset |
| `analysis_queries.sql` | SQL analysis |
| `generate_data.py` | Script used to create the sample data |
| `Sales_Dashboard.html` | Web version of the dashboard |
| `POWER_BI_STEPS.md` | Power BI build steps and DAX measures |

## Author
Gaurav Sharma | [LinkedIn](https://linkedin.com/in/gaurav-sharma-aa584a257)
