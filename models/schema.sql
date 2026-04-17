CREATE DATABASE sales_db;

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    category TEXT
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name TEXT,
    segment TEXT,
    location TEXT
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    date DATE,
    product_id INT REFERENCES products(product_id),
    customer_id INT REFERENCES customers(customer_id),
    quantity INT,
    price FLOAT,
    total_amount FLOAT,
    region TEXT
);