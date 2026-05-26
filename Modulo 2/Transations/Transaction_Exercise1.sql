DROP TABLE IF EXISTS bill_items;
DROP TABLE IF EXISTS bills;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    stock INTEGER NOT NULL CHECK (stock >= 0),
    price DECIMAL (10, 2) NOT NULL CHECK (price >= 0)
);

CREATE TABLE bills (
    bill_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL REFERENCES users(user_id),
    total DECIMAL (10, 2) NOT NULL CHECK (total >= 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Paid', 'Returned')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bill_items (
    bill_item_id SERIAL PRIMARY KEY,
    bill_id VARCHAR(50) NOT NULL REFERENCES bills(bill_id),
    product_id VARCHAR(50) NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    subtotal DECIMAL(10, 2) NOT NULL CHECK (subtotal >= 0)
);

INSERT INTO users (user_id, name, email)
VALUES ('U001', 'Rodrigo', 'rodri@gmail.com');

INSERT INTO products (product_id, name, stock, price)
VALUES
('P001', 'Mouse', 10, 25.00),
('P002', 'Keyboard', 5, 50.00),
('P003', 'Monitor', 3, 150.00);

