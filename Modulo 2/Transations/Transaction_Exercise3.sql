DO $$
DECLARE

    -- Variable to store bill status
    v_bill_status VARCHAR(20);

    -- Variable to iterate through bill items
    item RECORD;

BEGIN

    -- Verify bill exists and obtain status
    SELECT status
    INTO v_bill_status
    FROM bills
    WHERE bill_id = 'B001';

    -- Validate bill existence
    IF v_bill_status IS NULL THEN
        RAISE EXCEPTION 'Bill does not exist';
    END IF;

    -- Validate if bill was already returned
    IF v_bill_status = 'Returned' THEN
        RAISE EXCEPTION 'Bill already returned';
    END IF

    -- Iterate through all products from the bill
    FOR item IN
        SELECT product_id, 
        quantity
        FROM bill_items 
        WHERE bill_id = 'B001'
    LOOP

    -- Restore stock for each product
        UPDATE products
        SET stock = stock + item.quantity
        WHERE product_id = item.product_id;
    
    END LOOP;

    -- Mark bill as returned
    UPDATE bills
    SET status = 'Returned'
    WHERE bill_id = 'B001';

    -- Return confirmation  
    RAISE NOTICE 'Product return completed successfully';   

END $$;


