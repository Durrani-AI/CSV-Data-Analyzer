# Sales Data Analysis

A Python application for analyzing sales data from CSV files, calculating total revenue and revenue breakdown by product.

## Overview

This project reads sales data from a CSV file and provides financial insights including:
- Total revenue across all sales
- Revenue breakdown by individual products

## Features

- **CSV Data Loading**: Safely loads and validates sales data from `sales.csv`
- **Error Handling**: Gracefully handles missing files and invalid data entries
- **Revenue Calculation**: Computes total revenue across all transactions
- **Product Analysis**: Breaks down revenue by product for detailed insights
- **Data Validation**: Automatically filters out rows with invalid quantity or price values

## Requirements

- Python 3.6 or higher
- No external dependencies (uses Python standard library)

## File Structure

```
python Project 2/
├── Project2.py    # Main application script
├── sales.csv      # Sales data file (CSV format)
└── README.md      # This file
```

## Data Format

The `sales.csv` file should contain the following columns:

| Column   | Type   | Description                    |
|----------|--------|--------------------------------|
| Date     | String | Date of the sale               |
| Product  | String | Product name                   |
| Quantity | Integer| Number of units sold           |
| Price    | Float  | Price per unit (in £)          |

### Example CSV Format

```csv
Date,Product,Quantity,Price
2026-01-15,Laptop,2,899.99
2026-01-16,Mouse,5,25.50
2026-01-17,Keyboard,3,75.00
```

## Usage

1. Ensure `sales.csv` is in the same directory as `Project2.py`
2. Run the script:

```bash
python Project2.py
```

### Expected Output

```
Total Revenue: £2,627.48

Revenue by Product:
- Laptop: £1,799.98
- Mouse: £127.50
- Keyboard: £225.00
```

## Functions

### `load_sales_data()`
Loads sales data from the CSV file and converts quantity/price to appropriate numeric types.

**Returns**: List of dictionaries containing validated sales records

### `calculate_total_revenue(sales_data)`
Calculates the total revenue across all sales transactions.

**Parameters**:
- `sales_data`: List of sales records

**Returns**: Total revenue as a float

### `revenue_by_product(sales_data)`
Calculates revenue breakdown by product.

**Parameters**:
- `sales_data`: List of sales records

**Returns**: Dictionary mapping product names to their total revenue

### `main()`
Main execution function that orchestrates data loading and revenue reporting.

## Error Handling

- If `sales.csv` doesn't exist, the program displays "CSV file not found."
- Rows with invalid quantity or price values are automatically skipped
- If no valid data is found, displays "No valid sales data available."

## License

This project is provided as-is for educational and analytical purposes.
