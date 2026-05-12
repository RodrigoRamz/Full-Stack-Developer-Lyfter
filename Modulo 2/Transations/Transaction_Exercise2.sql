DO $$
DECLARE
    -- Variable ro validate user existence 
    v_user_exists INTEGER;

    --- Variable to store product stock
    v_stock INTEGER;

BEGIN
    -- Validate if the user exists
    SELECT COUNT (*)
    INTO v_user_exists
    FROM users
    WHERE user_id = 'U001';

    IF v_user_exists = 0 THEN
        RAISE EXCEPTION 'User does not exist';
    END IF;

    -- Validate product stock
    SELECT stock
    INTO v_stock
    FROM products
    WHERE product_id = 'P001';
    
    IF v_stock < 2 THEN
        RAISE EXCEPTION 'Insufficient stock';
    END IF;

-- Create Bill
INSERT INTO bills (
    bill_id,
    user_id,
    total,
    status
)
VALUES (    
    'B001',
    'U001',
    50.00,
    'Paid'
);

-- Create bill items
INSERT INTO bill_items (
    bill_id,
    product_id,
    quantity,
    subtotal
)
VALUES (
    'B001',
    'P001',
    2,
    50.00
);

-- Reduce product stock
UPDATE products
SET stock = stock - 2
WHERE product_id = 'P001';

-- Purchase confirmation
RAISE NOTICE 'Purchase Completed Successfully';

END $$;