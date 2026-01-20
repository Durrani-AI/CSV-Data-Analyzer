import csv
from pathlib import Path

FILE = Path("sales.csv")
HEADERS = ["Date", "Product", "Quantity", "Price"]


def load_sales_data():
    sales_data = []

    if not FILE.exists():
        print("CSV file not found.")
        return sales_data

    with FILE.open(mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                row["Quantity"] = int(row["Quantity"])
                row["Price"] = float(row["Price"])
            except (ValueError, TypeError):
                continue 

            sales_data.append(row)

    return sales_data


def calculate_total_revenue(sales_data):
    total = 0.0

    for row in sales_data:
        total += row["Quantity"] * row["Price"]

    return total


def revenue_by_product(sales_data):
    revenue = {}

    for row in sales_data:
        product = row["Product"]
        revenue[product] = revenue.get(product, 0.0) + (
            row["Quantity"] * row["Price"]
        )

    return revenue


def main():
    sales_data = load_sales_data()

    if not sales_data:
        print("No valid sales data available.")
        return

    total_revenue = calculate_total_revenue(sales_data)
    print(f"\nTotal Revenue: £{total_revenue:.2f}")

    print("\nRevenue by Product:")
    product_revenue = revenue_by_product(sales_data)
    for product, amount in product_revenue.items():
        print(f"- {product}: £{amount:.2f}")


if __name__ == "__main__":
    main()
