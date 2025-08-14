Basic Sales Summary from a Tiny SQLite Database using Python
Project Overview

This project connects Python to a small SQLite database, runs basic SQL queries, and visualizes results using Matplotlib.
It generates a basic sales summary showing the total quantity sold and total revenue per product, along with a simple bar chart.

Tools and Technologies

Python 3

SQLite (built into Python)

pandas for data handling

matplotlib for visualization

Dataset

The dataset is stored in a local SQLite database file named sales_data.db with a single table sales containing:

order_id – Auto-incremented order identifier

order_date – Date of the order

product – Product name

quantity – Units sold

price – Unit price in USD

A CSV export of the raw data (sales_data_raw.csv) is also included.

Features

Creates and populates a SQLite database with sample sales data if empty

Runs SQL queries directly from Python to produce:

Per-product summary with total quantity and revenue

Overall totals for all products

Displays results in the console

Generates and saves a bar chart of revenue by product (sales_chart.png)

Example Output

Console Output:

=== Sales Summary by Product ===
       product  total_qty  revenue
   USB-C Cable         26   169.00
Wireless Mouse          8   159.92
      Keyboard          6   149.94
 Laptop Sleeve         10   149.90
        Webcam          3   119.97
  Laptop Stand          3    89.97

=== Overall Totals ===
 grand_total_qty  grand_total_revenue
              56                838.70

How to Run

Clone the repository

Install required packages:

pip install pandas matplotlib


Run the script:

python task7_basic_sales_summary.py


View the console output and check the sales_chart.png file in the folder.

Files in This Project

sales_data.db – SQLite database

sales_data_raw.csv – Original dataset in CSV format

task7_basic_sales_summary.py – Python script to generate the summary and chart

sales_chart.png – Generated revenue bar chart

README.md – Project documentation

Possible Enhancements

Add date-wise trend analysis

Export summaries to Excel

Use Seaborn for enhanced visualizations

Accept user-uploaded CSV files to update the database
