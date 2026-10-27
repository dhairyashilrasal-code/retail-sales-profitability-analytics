# Retail Sales & Profitability Analytics

## Overview
An end-to-end retail sales analytics project using Python, SQL, Pandas, and data visualization to analyze revenue, costs, profit margins, product performance, regional sales, monthly trends, and sales channels.

## Objectives
- Evaluate overall sales and profitability KPIs.
- Identify top-performing products and regions.
- Analyze monthly revenue and profit trends.
- Compare sales channels using SQL queries.
- Generate charts and dashboard-ready CSV summaries.

## Tech Stack
- **Python:** Data processing and exploratory data analysis
- **Pandas & NumPy:** Data manipulation and calculations
- **Matplotlib & Seaborn:** Visualizations
- **SQLite & SQL:** Business KPI queries and aggregations
- **Power BI:** Planned interactive dashboard

## Project Structure
- `generate_data.py` — Generates the sample retail sales dataset.
- `analysis.py` — Performs data-quality checks, KPI calculations, and visualizations.
- `run_sql.py` — Loads CSV data into SQLite and executes SQL analyses.
- `sql/retail_analysis.sql` — Contains reusable business analysis queries.
- `data/` — Generated CSV dataset and local SQLite database.
- `visuals/` — Charts and analysis summary files.

## How to Run
1. Create and activate a Python virtual environment.
2. Install dependencies using `pip install -r requirements.txt`.
3. Generate the dataset with `python generate_data.py`.
4. Run Python analysis with `python analysis.py`.
5. Execute SQL analysis with `python run_sql.py`.

## Dataset
The project uses **synthetic sample data** generated with Python for demonstration and portfolio purposes. It does not represent actual company sales.

## Key Analyses
- Overall revenue, cost, profit, and profit margin
- Product-level profitability
- Regional sales performance
- Monthly revenue and profit trends
- Sales channel comparisons

## Future Enhancement
Build an interactive Power BI dashboard with KPI cards, product and regional comparisons, monthly trends, and sales channel filters.