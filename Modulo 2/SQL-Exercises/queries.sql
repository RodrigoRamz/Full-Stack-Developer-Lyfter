PRAGMA foreign_keys = ON;

-- DROP TABLES (to execute the script)

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS invoice_items;
DROP TABLE IF EXISTS shopping_cart;
DROP TABLE IF EXISTS shopping_cart_items;

-- PRODUCTS
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    brand TEXT
);

-- INVOICES
CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT UNIQUE NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    buyer_email TEXT NOT NULL,
    total_amount INTEGER NOT NULL
);

-- INVOICE ITEMS (relate the products with the invoice)
CREATE TABLE invoice_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_amount INTEGER NOT NULL,

    FOREIGN KEY (invoice_id) REFERENCES invoices(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- SHOPPING CART
CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT NOT NULL
);

-- SHOPPING CART ITEMS
CREATE TABLE shopping_cart_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,

    FOREIGN KEY (cart_id) REFERENCES shopping_cart(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

ALTER TABLE invoices
ADD COLUMN buyer_phone TEXT;

ALTER TABLE invoices
ADD COLUMN cashier_code TEXT;

-- INSERT SAMPLE DATA

INSERT INTO products (code, name, price, brand)
VALUES ('P001', 'Laptop', 120000, 'Dell');

INSERT INTO products (code, name, price, brand)
VALUES ('P002', 'Mouse', 15000, 'LogiTech');

INSERT INTO products (code, name, price, brand)
VALUES ('P003', 'Monitor', 70000, 'Samsung');

INSERT INTO invoices (invoice_number, buyer_email, total_amount, buyer_phone, cashier_code)
VALUES ('F001', 'cliente@email.com', 135000, '8888-8888', 'EMP001');

INSERT INTO invoice_items (invoice_id, product_id, quantity, total_amount)
VALUES (1, 1, 1, 120000);

INSERT INTO invoice_items (invoice_id, product_id, quantity, total_amount)
VALUES (1, 2, 1, 150000);

-- Exercise Queries

-- 1. Get all the stored products
SELECT *
FROM products;

-- 2. Get the product with the price greater than 50000
SELECT *
FROM products
WHERE price > 50000;

-- 3. Get the purchases from a product id
SELECT *
FROM invoice_items
WHERE product_id = 1;

-- 4. Join purchases by product
SELECT
    product_id,
    SUM(quantity) AS total_purchased
FROM invoice_items
GROUP BY product_id;

-- 5. Invoices from the same buyer
SELECT *
FROM invoices
WHERE buyer_email = 'cliente@email.com';

-- 6. Order invoices by descent total amount
SELECT *
FROM invoices
ORDER BY total_amount DESC;

-- 7. Get an invoice by number
SELECT *
FROM invoices
WHERE invoice_number = 'F001';