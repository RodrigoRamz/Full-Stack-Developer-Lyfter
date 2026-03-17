
-- Categories Table
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT
);

-- Add category_id column to products table
ALTER TABLE products ADD COLUMN category_id INTEGER;

-- Ensure quantity exists
ALTER TABLE products ADD COLUMN quantity INTEGER DEFAULT 0;

-- Insert Categories
INSERT INTO categories (name, description)
VALUES ('Electronics', 'Electronic Devices');

INSERT INTO categories (name, description)
VALUES ('Accessories', 'Computer accessories');

INSERT INTO categories (name, description)
VALUES ('Home', 'Home appliances');

-- Update products table with category
UPDATE products SET category_id = 1 WHERE id = 1;
UPDATE products SET category_id = 2 WHERE id = 2;
UPDATE products SET category_id = 1 WHERE id = 3;

-- Verify Products
SELECT id, name AS product_name, price, quantity, category_id
FROM products;

-- Insert more products and filters
INSERT INTO products (code, name, price, brand)
VALUES ('P010', 'Apple MacBook', 120000, 'Apple');

INSERT INTO products (code, name, price, brand)
VALUES ('P011''Apple Mouse', 25000, 'Apple');

INSERT INTO products (code, name, price, brand)
VALUES ('P012', 'Samsung TV', 80000, 'Samsung');

INSERT INTO products (code, name, price, brand)
VALUES ('P013', 'LG Monitor', 70000, 'LG');

INSERT INTO products (code, name, price, brand)
VALUES ('P014', 'Sony Headphones', 40000, 'Sony');

INSERT INTO products (code, name, price, brand)
VALUES ('P015', 'Dell Laptop', 90000, 'Dell');

INSERT INTO products (code, name, price, brand)
VALUES ('P016', 'Logitech Mouse', 20000, 'Logitech');

INSERT INTO products (code, name, price, brand)
VALUES ('P017', 'Apple Watch', 60000, 'Apple');

INSERT INTO products (code, name, price, brand)
VALUES ('P018', 'HP Printer', 50000, 'HP');

-- Select All products
SELECT * FROM products;

---Products with a price greater than 50000
SELECT *
FROM products
WHERE price > 50000;

-- Apple Products
SELECT *
FROM products
WHERE name LIKE '%apple%';

--- Top 5 Expensive Products
SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;

-- Add new invoice fields
ALTER TABLE invoices ADD COLUMN phone TEXT;

ALTER TABLE invoices ADD COLUMN cashier_code TEXT DEFAULT 'N/A';

-- Update Invoices
UPDATE invoices SET phone= '8888-8888', cashier_code= 'EMP001' WHERE id= 1;

UPDATE invoices SET phone = '8777-7777', cashier_code = 'EMP002' WHERE id = 2;

-- Invoices with Phone NULL
SELECT * FROM invoices WHERE phone IS NULL OR phone = '';

-- Get an invoice by id
SELECT * FROM invoices WHERE id = 1;

-- Updates to products
UPDATE products SET quantity = 0 WHERE price <= 0;

-- Decrease quantity in a specific product
UPDATE products SET quantity = quantity - 1 WHERE id = 1;

-- Verify Results
SELECT * FROM products ORDER BY id ASC LIMIT 10;

-- Increase price to 100 when quantity < 10
UPDATE products SET price = price + 100 WHERE quantity < 10;

