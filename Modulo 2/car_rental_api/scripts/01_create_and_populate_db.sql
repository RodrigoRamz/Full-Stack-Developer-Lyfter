CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;

DROP TABLE IF EXISTS lyfter_car_rental.rentals;
DROP TABLE IF EXISTS lyfter_car_rental.cars;
DROP TABLE IF EXISTS lyfter_car_rental.users;

CREATE TABLE lyfter_car_rental.users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    account_status VARCHAR(20) NOT NULL DEFAULT 'active',
    is_delinquent BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE lyfter_car_rental.cars (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    manufacturing_year INTEGER NOT NULL,
    car_status VARCHAR(20) NOT NULL DEFAULT 'available'
);

CREATE TABLE lyfter_car_rental.rentals (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    rental_date DATE NOT NULL DEFAULT CURRENT_DATE,
    returning_date DATE NOT NULL,
    rental_status VARCHAR(20) NOT NULL DEFAULT 'active',

    CONSTRAINT fk_rental_user
        FOREIGN KEY (user_id)
        REFERENCES lyfter_car_rental.users(id),

    CONSTRAINT fk_rental_car
        FOREIGN KEY (car_id)
        REFERENCES lyfter_car_rental.cars(id)
);

INSERT INTO lyfter_car_rental.cars
(brand, model, manufacturing_year, car_status)
VALUES
('Toyota', 'Corolla', 2020, 'available'),
('Toyota', 'RAV4', 2022, 'available'),
('Toyota', 'Fortuner', 2017, 'available'),
('Hyundai', 'Tucson', 2021, 'available'),
('Hyundai', 'Elantra', 2019, 'available'),
('Nissan', 'Sentra', 2020, 'available'),
('Nissan', 'X-Trail', 2022, 'available'),
('Suzuki', 'Vitara', 2023, 'available'),
('Kia', 'Sportage', 2021, 'available'),
('Honda', 'Civic', 2018, 'available');

INSERT INTO lyfter_car_rental.users
(full_name, email, username, password, birth_date, account_status)
VALUES
('User 1', 'user1@email.com', 'user1', 'pass123', '1990-01-01', 'active'),
('User 2', 'user2@email.com', 'user2', 'pass123', '1991-02-02', 'active'),
('User 3', 'user3@email.com', 'user3', 'pass123', '1992-03-03', 'active'),
('User 4', 'user4@email.com', 'user4', 'pass123', '1993-04-04', 'active'),
('User 5', 'user5@email.com', 'user5', 'pass123', '1994-05-05', 'active'),
('User 6', 'user6@email.com', 'user6', 'pass123', '1995-06-06', 'active'),
('User 7', 'user7@email.com', 'user7', 'pass123', '1996-07-07', 'active'),
('User 8', 'user8@email.com', 'user8', 'pass123', '1997-08-08', 'active'),
('User 9', 'user9@email.com', 'user9', 'pass123', '1998-09-09', 'active'),
('User 10', 'user10@email.com', 'user10', 'pass123', '1999-10-10', 'active'),
('User 11', 'user11@email.com', 'user11', 'pass123', '1990-01-11', 'active'),
('User 12', 'user12@email.com', 'user12', 'pass123', '1991-02-12', 'active'),
('User 13', 'user13@email.com', 'user13', 'pass123', '1992-03-13', 'active'),
('User 14', 'user14@email.com', 'user14', 'pass123', '1993-04-14', 'active'),
('User 15', 'user15@email.com', 'user15', 'pass123', '1994-05-15', 'active'),
('User 16', 'user16@email.com', 'user16', 'pass123', '1995-06-16', 'active'),
('User 17', 'user17@email.com', 'user17', 'pass123', '1996-07-17', 'active'),
('User 18', 'user18@email.com', 'user18', 'pass123', '1997-08-18', 'active'),
('User 19', 'user19@email.com', 'user19', 'pass123', '1998-09-19', 'active'),
('User 20', 'user20@email.com', 'user20', 'pass123', '1999-10-20', 'active'),
('User 21', 'user21@email.com', 'user21', 'pass123', '1990-01-21', 'active'),
('User 22', 'user22@email.com', 'user22', 'pass123', '1991-02-22', 'active'),
('User 23', 'user23@email.com', 'user23', 'pass123', '1992-03-23', 'active'),
('User 24', 'user24@email.com', 'user24', 'pass123', '1993-04-24', 'active'),
('User 25', 'user25@email.com', 'user25', 'pass123', '1994-05-25', 'active'),
('User 26', 'user26@email.com', 'user26', 'pass123', '1995-06-26', 'active'),
('User 27', 'user27@email.com', 'user27', 'pass123', '1996-07-27', 'active'),
('User 28', 'user28@email.com', 'user28', 'pass123', '1997-08-28', 'active'),
('User 29', 'user29@email.com', 'user29', 'pass123', '1998-09-01', 'active'),
('User 30', 'user30@email.com', 'user30', 'pass123', '1999-10-02', 'active'),
('User 31', 'user31@email.com', 'user31', 'pass123', '1990-01-03', 'active'),
('User 32', 'user32@email.com', 'user32', 'pass123', '1991-02-04', 'active'),
('User 33', 'user33@email.com', 'user33', 'pass123', '1992-03-05', 'active'),
('User 34', 'user34@email.com', 'user34', 'pass123', '1993-04-06', 'active'),
('User 35', 'user35@email.com', 'user35', 'pass123', '1994-05-07', 'active'),
('User 36', 'user36@email.com', 'user36', 'pass123', '1995-06-08', 'active'),
('User 37', 'user37@email.com', 'user37', 'pass123', '1996-07-09', 'active'),
('User 38', 'user38@email.com', 'user38', 'pass123', '1997-08-10', 'active'),
('User 39', 'user39@email.com', 'user39', 'pass123', '1998-09-11', 'active'),
('User 40', 'user40@email.com', 'user40', 'pass123', '1999-10-12', 'active'),
('User 41', 'user41@email.com', 'user41', 'pass123', '1990-01-13', 'active'),
('User 42', 'user42@email.com', 'user42', 'pass123', '1991-02-14', 'active'),
('User 43', 'user43@email.com', 'user43', 'pass123', '1992-03-15', 'active'),
('User 44', 'user44@email.com', 'user44', 'pass123', '1993-04-16', 'active'),
('User 45', 'user45@email.com', 'user45', 'pass123', '1994-05-17', 'active'),
('User 46', 'user46@email.com', 'user46', 'pass123', '1995-06-18', 'active'),
('User 47', 'user47@email.com', 'user47', 'pass123', '1996-07-19', 'active'),
('User 48', 'user48@email.com', 'user48', 'pass123', '1997-08-20', 'active'),
('User 49', 'user49@email.com', 'user49', 'pass123', '1998-09-21', 'active'),
('User 50', 'user50@email.com', 'user50', 'pass123', '1999-10-22', 'active');

INSERT INTO lyfter_car_rental.rentals
(user_id, car_id, returning_date, rental_status)
VALUES
(1, 1, '2026-06-25', 'active'),
(2, 2, '2026-06-27', 'active');

UPDATE lyfter_car_rental.cars
SET car_status = 'rented'
WHERE id IN (1, 2);

SELECT * FROM lyfter_car_rental.users;
SELECT * FROM lyfter_car_rental.cars;
SELECT * FROM lyfter_car_rental.rentals;
