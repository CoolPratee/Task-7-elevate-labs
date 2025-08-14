\
# task7_basic_sales_summary.py
# Run: python task7_basic_sales_summary.py
# Requires: Python 3, built-in sqlite3, plus: pip install pandas matplotlib

import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "sales_data.db"
CHART_PATH = "sales_chart.png"

def ensure_db(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(\"\"\"
    CREATE TABLE IF NOT EXISTS sales (
        order_id     INTEGER PRIMARY KEY AUTOINCREMENT,
        order_date   TEXT NOT NULL,
        product      TEXT NOT NULL,
        quantity     INTEGER NOT NULL,
        price        REAL NOT NULL
    );
    \"\"\")
    # Only populate if table is empty
    cur.execute("SELECT COUNT(*) FROM sales;")
    count = cur.fetchone()[0]
    if count == 0:
        rows = [
            ("2025-07-01", "Laptop Sleeve", 3, 14.99),
            ("2025-07-01", "USB-C Cable", 5, 6.50),
            ("2025-07-02", "Wireless Mouse", 2, 19.99),
            ("2025-07-02", "USB-C Cable", 4, 6.50),
            ("2025-07-03", "Laptop Sleeve", 1, 14.99),
            ("2025-07-03", "Keyboard", 2, 24.99),
            ("2025-07-04", "Wireless Mouse", 3, 19.99),
            ("2025-07-05", "Webcam", 1, 39.99),
            ("2025-07-06", "USB-C Cable", 8, 6.50),
            ("2025-07-07", "Keyboard", 1, 24.99),
            ("2025-07-07", "Laptop Stand", 2, 29.99),
            ("2025-07-08", "Laptop Stand", 1, 29.99),
            ("2025-07-08", "USB-C Cable", 3, 6.50),
            ("2025-07-09", "Laptop Sleeve", 4, 14.99),
            ("2025-07-10", "Wireless Mouse", 1, 19.99),
            ("2025-07-10", "Keyboard", 3, 24.99),
            ("2025-07-11", "Webcam", 2, 39.99),
            ("2025-07-12", "USB-C Cable", 6, 6.50),
            ("2025-07-12", "Laptop Sleeve", 2, 14.99),
            ("2025-07-13", "Wireless Mouse", 2, 19.99),
        ]
        cur.executemany(
            "INSERT INTO sales (order_date, product, quantity, price) VALUES (?, ?, ?, ?);",
            rows
        )
        conn.commit()
    return conn

def main():
    conn = ensure_db()
    query_by_product = \"\"\"
    SELECT 
        product, 
        SUM(quantity) AS total_qty, 
        ROUND(SUM(quantity * price), 2) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC;
    \"\"\"
    df_product = pd.read_sql_query(query_by_product, conn)

    query_totals = \"\"\"
    SELECT 
        SUM(quantity) AS grand_total_qty,
        ROUND(SUM(quantity * price), 2) AS grand_total_revenue
    FROM sales;
    \"\"\"
    df_totals = pd.read_sql_query(query_totals, conn)

    print("=== Sales Summary by Product ===")
    print(df_product.to_string(index=False))
    print("\\n=== Overall Totals ===")
    print(df_totals.to_string(index=False))

    plt.figure()
    plt.bar(df_product["product"], df_product["revenue"])
    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_PATH)
    plt.close()

    print(f"\\nSaved chart to {CHART_PATH}")
    print(f"Database at {DB_PATH}")

if __name__ == "__main__":
    main()
