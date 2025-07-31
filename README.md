# Sales Metrics Forecasting Platform


This project is a complete **ETL + Analytics + Forecasting Pipeline** built using **Python, Pandas, Streamlit, and Prophet**.  

- Monitor real-time sales KPIs  
- Explore category, region, and product-based trends  
- Extract smart business insights  
- Forecast future sales  
- Export custom reports  




##  Project Architecture

```text
           ┌──────────────────────────────┐
           │     Raw Sales Data (CSV)     │
           │                              │
           └────────────┬─────────────────┘
                        │
                        ▼
           ┌──────────────────────────────┐
           │      extract.py (ETL - E)    │
           │  Reads raw CSV → DataFrame   │
           └────────────┬─────────────────┘
                        │
                        ▼
           ┌──────────────────────────────┐
           │    transform.py (ETL - T)    │
           │  Cleans, validates, enriches │
           │  - Parses dates              │
           │  - Handles nulls             │
           │  - Adds TotalPrice           │
           └────────────┬─────────────────┘
                        │
                        ▼
           ┌──────────────────────────────┐
           │      load.py (ETL - L)       │
           │ Saves clean data as CSV      │
           └────────────┬─────────────────┘
                        │
                        ▼
           ┌──────────────────────────────┐
           │ Streamlit Dashboard          │
           │ - KPI Metrics                │
           │ - Interactive Filters        │
           │ - Visual Charts              │
           │ - Top Products Table         │
           │ - Smart Insights Engine      │
           │ - CSV Export                 │
           └────────────┬─────────────────┘
                        │
                        ▼
           ┌──────────────────────────────┐
           │  Prophet Forecast Module     │
           │ Predicts next 6 months sales │
           │   Trend & seasonality aware  │
           └──────────────────────────────┘
