DO $$
DECLARE
    -- Variable to validate user existence 
    v_user_exists INTEGER;

    -- Variable to iterate through products
    item RECORD;

    -- Variable to calculate bill total
    v_bill_total DECIMAL (10, 2);

BEGIN
    -- Validate if the user exists
    SELECT COUNT (*)
    INTO v_user_exists
    FROM users
    WHERE user_id = 'U001';

    IF v_user_exists = 0 THEN
        RAISE EXCEPTION 'User does not exist';
    END IF;

    -- Temporary table to simulate multiple purchased products
    CREATE TEMP TABLE temp_purchase_items (
        product_id VARCHAR(50),
        quantity INTEGER
    ) ON COMMIT DROP;

    -- Products included in the purchase
    INSERT INTO temp_purchase_items (product_id, quantity)
    VALUES
    ('P001', 2),
    ('P002', 1);

    -- Validate stock for all products    
    FOR item IN
        SELECT 
            t.product_id, 
            t.quantity, 
            t.stock, 
            p.price
        FROM temp_purchase_items t 
        JOIN products p 
            ON p.product_id = t.product_id
    LOOP
        IF items.stock < items.quantity THEN
            RAISE EXCEPTION
            'Insufficient stock product %', 
            item.product_id;
        END IF;

    END LOOP;

    -- Calculate total bill amount
    SELECT SUM(t.quanity * p.price)
    INTO v_bill_total
    FROM temp_purchase_items t
    JOIN products p 
        ON p.product_id = t.product_id;

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
        v_bill_total,
        'Paid'
    );

    -- Create bill items for all products
    INSERT INTO bill_items (
        bill_id, 
        product_id, 
        quantity, 
        subtotal
    )
    SELECT 
        'B001',
        t.product_id,
        t.quantity,
        t.quantity * p.price
    FROM temp_purchase_items t
    JOIN products p 
        ON p.product_id = t.product_id;

    -- Reduce stock for all purchased products
    UPDATE products p
    SET stock = p.stock - t.quantity
    FROM temp_purchase_items t
    WHERE p.product_id = t.product_id;

    -- Purchase Confirmation
    RAISE NOTICE 'Purchase Completed Successfully';

END $$;