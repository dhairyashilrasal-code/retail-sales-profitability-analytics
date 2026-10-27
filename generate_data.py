
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

products = {
    "Laptop": (55000, 42000, "Computers"),
    "Smartphone": (25000, 18000, "Electronics"),
    "Headphones": (2500, 1200, "Accessories"),
    "Monitor": (12000, 8500, "Computers"),
    "Keyboard": (1500, 700, "Accessories"),
    "Mouse": (800, 300, "Accessories"),
    "Tablet": (18000, 13000, "Electronics"),
    "Printer": (9000, 6500, "Office Equipment"),
}

regions = ["North", "South", "East", "West", "Central"]
channels = ["Online", "Retail Store", "Marketplace"]
start_date = date(2025, 1, 1)
date_range = (date(2025, 12, 31) - start_date).days

output = DATA_DIR / "retail_sales.csv"

with output.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Order_ID", "Order_Date", "Region", "Product", "Category",
        "Sales_Channel", "Quantity", "Unit_Price", "Unit_Cost",
        "Revenue", "Cost", "Profit"
    ])

    for i in range(1, 2001):
        product = random.choice(list(products))
        price, cost, category = products[product]
        quantity = random.randint(1, 8)
        order_date = start_date + timedelta(
            days=random.randint(0, date_range)
        )

        unit_price = round(price * random.uniform(0.90, 1.10), 2)
        unit_cost = round(cost * random.uniform(0.95, 1.05), 2)
        revenue = round(unit_price * quantity, 2)
        total_cost = round(unit_cost * quantity, 2)

        writer.writerow([
            f"ORD{i:05d}", order_date.isoformat(),
            random.choice(regions), product, category,
            random.choice(channels), quantity, unit_price,
            unit_cost, revenue, total_cost,
            round(revenue - total_cost, 2)
        ])

print(f"Dataset created: {output}")
print("Total records: 2000")
