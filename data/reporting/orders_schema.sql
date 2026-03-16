DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    order_status TEXT NOT NULL,
    amount REAL NOT NULL,
    region TEXT NOT NULL,
    order_date TEXT NOT NULL
);