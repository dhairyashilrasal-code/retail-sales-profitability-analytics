
import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent
csv_path = ROOT / "data" / "retail_sales.csv"
db_path = ROOT / "data" / "retail_sales.db"
sql_path = ROOT / "sql" / "retail_analysis.sql"

df = pd.read_csv(csv_path)

with sqlite3.connect(db_path) as conn:
    df.to_sql("retail_sales", conn, if_exists="replace", index=False)

    queries = [
        ("Overall KPIs", """
            SELECT ROUND(SUM(Revenue), 2) AS revenue,
                   ROUND(SUM(Profit), 2) AS profit,
                   ROUND(100.0 * SUM(Profit) / SUM(Revenue), 2)
                       AS margin_pct
            FROM retail_sales
        """),
        ("Product Profitability", """
            SELECT Product, ROUND(SUM(Revenue), 2) AS revenue,
                   ROUND(SUM(Profit), 2) AS profit
            FROM retail_sales
            GROUP BY Product ORDER BY profit DESC
        """),
        ("Regional Performance", """
            SELECT Region, ROUND(SUM(Revenue), 2) AS revenue,
                   ROUND(SUM(Profit), 2) AS profit
            FROM retail_sales
            GROUP BY Region ORDER BY revenue DESC
        """),
        ("Monthly Trends", """
            SELECT SUBSTR(Order_Date, 1, 7) AS month,
                   ROUND(SUM(Revenue), 2) AS revenue,
                   ROUND(SUM(Profit), 2) AS profit
            FROM retail_sales
            GROUP BY month ORDER BY month
        """),
        ("Channel Performance", """
            SELECT Sales_Channel, COUNT(*) AS order_lines,
                   ROUND(SUM(Revenue), 2) AS revenue,
                   ROUND(SUM(Profit), 2) AS profit
            FROM retail_sales
            GROUP BY Sales_Channel ORDER BY revenue DESC
        """),
    ]

    for title, query in queries:
        print(f"\n--- {title} ---")
        print(pd.read_sql_query(query, conn).to_string(index=False))

    # Verify that the saved SQL file is present.
    assert sql_path.exists(), f"Missing SQL file: {sql_path}"

print(f"\nSQLite database created: {db_path}")
print(f"Rows loaded: {len(df)}")
