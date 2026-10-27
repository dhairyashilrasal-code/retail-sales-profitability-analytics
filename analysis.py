
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "retail_sales.csv"
OUT = ROOT / "visuals"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order_Date"])

# 1. Data quality checks
print("\n--- DATA QUALITY ---")
print("Rows and columns:", df.shape)
print("Duplicate rows:", df.duplicated().sum())
print("Missing values:\n", df.isnull().sum())

# 2. Business KPIs
revenue = df["Revenue"].sum()
cost = df["Cost"].sum()
profit = df["Profit"].sum()
margin = profit / revenue * 100 if revenue else 0

print("\n--- BUSINESS KPIs ---")
print(f"Total Revenue:  {revenue:,.2f}")
print(f"Total Cost:     {cost:,.2f}")
print(f"Total Profit:   {profit:,.2f}")
print(f"Profit Margin:  {margin:.2f}%")
print(f"Units Sold:     {df['Quantity'].sum():,}")
print(f"Orders:         {df['Order_ID'].nunique():,}")

# 3. Product profitability
product = (
    df.groupby("Product", as_index=False)
    .agg(Revenue=("Revenue", "sum"),
         Profit=("Profit", "sum"),
         Units=("Quantity", "sum"))
    .sort_values("Profit", ascending=False)
)
product["Profit_Margin_Pct"] = (
    product["Profit"] / product["Revenue"] * 100
).round(2)
product.to_csv(OUT / "product_performance.csv", index=False)
print("\n--- PRODUCT PERFORMANCE ---")
print(product.to_string(index=False))

# 4. Regional performance
region = (
    df.groupby("Region", as_index=False)
    .agg(Revenue=("Revenue", "sum"), Profit=("Profit", "sum"))
    .sort_values("Revenue", ascending=False)
)
region.to_csv(OUT / "regional_performance.csv", index=False)
print("\n--- REGIONAL PERFORMANCE ---")
print(region.to_string(index=False))

# 5. Monthly trends
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly = (
    df.groupby("Month", as_index=False)
    .agg(Revenue=("Revenue", "sum"), Profit=("Profit", "sum"))
)
monthly.to_csv(OUT / "monthly_trends.csv", index=False)

# 6. Dashboard-ready KPI data for Power BI
pd.DataFrame([{
    "Total_Revenue": round(revenue, 2),
    "Total_Cost": round(cost, 2),
    "Total_Profit": round(profit, 2),
    "Profit_Margin_Pct": round(margin, 2),
    "Units_Sold": int(df["Quantity"].sum()),
    "Order_Count": int(df["Order_ID"].nunique())
}]).to_csv(OUT / "kpi_summary.csv", index=False)

# 7. Charts
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.barplot(data=product, x="Profit", y="Product")
plt.title("Profit by Product")
plt.tight_layout()
plt.savefig(OUT / "profit_by_product.png", dpi=150)
plt.close()

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly, x="Month", y="Revenue", marker="o")
plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT / "monthly_revenue.png", dpi=150)
plt.close()

plt.figure(figsize=(9, 5))
sns.barplot(data=region, x="Region", y="Revenue")
plt.title("Revenue by Region")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_region.png", dpi=150)
plt.close()

print("\nAnalysis complete. Results and charts saved in visuals/.")
