DO $$
DECLARE

    v_bill_exists INTEGER;
    v_bill_status VARCHAR(20);
    v_quantity INTEGER;

BEGIN

    -- Verify that the bill exists
    SELECT COUNT(*)
    INTO v_bill_exists
    FROM bills
    WHERE bill_id = 'B001';

    IF v_bill_exists = 0 THEN
        RAISE EXCEPTION 'Bill does not exist';
    END IF;

    -- Verify bill status
    SELECT status
    INTO v_bill_status
    FROM bills
    WHERE bill_id = 'B001';

    IF v_bill_status = 'Returned' THEN
        RAISE EXCEPTION 'Bill already returned';
    END IF;

    -- Obtain purchased quantity
    SELECT quantity
    INTO v_quantity
    FROM bill_items
    WHERE bill_id = 'B001'
    AND product_id = 'P001';

    -- Increase Stock
    UPDATE products
    SET stock = stock + v_quantity
    WHERE product_id = 'P001';

    -- Mark Bill as returned
    UPDATE bills
    SET status = 'Returned'
    WHERE bill_id = 'B001';

    -- Confirmation message
    RAISE NOTICE 'Product return completed successfully';

END $$;