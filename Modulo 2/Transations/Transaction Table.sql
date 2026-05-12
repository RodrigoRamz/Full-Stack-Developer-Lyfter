Ejercicio #1

Users Table

| User_id | Name  | Email         |
|---------|-------|---------------|
|U001   |Rodrigo|rodri@gmail.com 

Products Table

| Product_id | Name | Stock | Price |
|------------|------|-------|-------|
|P001        |Mouse |10     |25     |

Bills Table 

|Bill_id | User_id | Total | Status |
|--------|---------|-------|--------|
|B001    |U001     |100    |Paid    |


Bill_items Table

|Bill_item_id | Bill_id | Product_id | quantity | subtotal |
|-------------|---------|------------|----------|----------|
|1            |B001     |P001        |2         |50        |

Ejercicio #2

1. Validate User

SELECT * FROM Users
WHERE User_id = 'U001';
RAISE EXCEPTION

2. Validate Stock

SELECT stock
FROM Products
WHERE Product_id = 'P001';
IF stock < quantity THEN
    error
END IF;

3. Create Bill

INSERT bills

4. Create bill items

INSERT Bill_items

5. Reduce Inventory

UPDATE products
SET stock = stock - quantity 

6. Purchase Confirmation

Ejercicio 3

1. Verify Bill
2. Verify Bill Not Returned
3. Obtain Purchased Products
4. Increase Stock
5. Bill marked as Returned


