-- INSERT INTO lyfter_car_rental.users
-- (full_name, email, username, password, birth_date, account_status)
-- VALUES
-- ('Rodrigo Ramirez', 'rodrigo@email.com', 'rodrigo', 'pass3325', '1987-10-30', 'active');

-- SELECT *
-- FROM lyfter_car_rental.users
-- WHERE username = 'rodrigo';

-- INSERT INTO lyfter_car_rental.cars
-- (brand, model, manufacturing_year, car_status)
-- VALUES
-- ('Ford', 'Escape', 2021, 'available');

SELECT *
FROM lyfter_car_rental.cars
WHERE brand = 'Ford'
AND model = 'Escape';

UPDATE lyfter_car_rental.users
SET account_status = 'inactive'
WHERE username = 'rodrigo';

SELECT *
FROM lyfter_car_rental.users
WHERE username = 'rodrigo';

UPDATE lyfter_car_rental.users
SET account_status = 'inactive',
    password = 'newpass'
WHERE username = 'rodrigo';

SELECT *
FROM lyfter_car_rental.users
WHERE username = 'rodrigo';

UPDATE lyfter_car_rental.cars
SET car_status = 'disabled'
WHERE id = 11;

SELECT *
FROM lyfter_car_rental.cars
WHERE id = 11;

-- INSERT INTO lyfter_car_rental.rentals
-- (user_id, car_id, returning_date, rental_status)
-- VALUES
-- (51, 12, '2026-07-01', 'active');

-- UPDATE lyfter_car_rental.cars
-- SET car_status = 'rented'
-- WHERE id = 12;

SELECT *
FROM lyfter_car_rental.rentals
WHERE user_id = 51
AND car_id = 12;

SELECT *
FROM lyfter_car_rental.cars
WHERE id = 12;

UPDATE lyfter_car_rental.rentals
SET rental_status = 'completed'
WHERE id = 3;

UPDATE lyfter_car_rental.cars
SET car_status = 'available'
WHERE id = 12;

SELECT *
FROM lyfter_car_rental.rentals
WHERE id = 3;

SELECT *
FROM lyfter_car_rental.cars
WHERE id = 12;

UPDATE lyfter_car_rental.rentals
SET rental_status = 'completed'
WHERE id = 4;

UPDATE lyfter_car_rental.cars
SET car_status = 'available'
WHERE id = 12;

UPDATE lyfter_car_rental.cars
SET car_status = 'disabled'
WHERE id = 12;

SELECT *
FROM lyfter_car_rental.cars
WHERE id = 12;

SELECT *
FROM lyfter_car_rental.cars
WHERE car_status = 'rented';

SELECT *
FROM lyfter_car_rental.cars
WHERE car_status = 'available';