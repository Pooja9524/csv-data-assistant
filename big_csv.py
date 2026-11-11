import csv
import random

random.seed(1)  # same data every time

regions = ["South", "North", "East", "West"]
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [500, 1200, 12000, 55000]

with open("big.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "region", "product", "quantity", "unit_price", "order_date"])

    for i in range(1, 100001):
        quantity = random.randint(1, 20)
        if i % 10 == 0:
            quantity = ""  # leave every 10th quantity blank

        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date = f"2026-{month:02d}-{day:02d}"

        writer.writerow([i, random.choice(regions), random.choice(products), quantity, random.choice(prices), date])

print("big.csv created")