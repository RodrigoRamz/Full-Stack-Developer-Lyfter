# Ejercicios de JOINs

# Creacion de Tablas e INSERT de Datos

### Table Books
SQL: 
CREATE TABLE Books (
    ID INT,
    Name TEXT,
    Author INT
);

INSERT INTO Books (ID, Name, Author) VALUES
(1,	'Don Quijote',	1),
(2,	'La Divina Comedia', 2),
(3,	'Vagabond 1-3',	3),
(4,	'Dragon Ball 1', 4),
(5,	'The Book of the 5 Rings', NULL);

### Table Authors
SQL:
CREATE TABLE Authors (
    ID INT,
    Name TEXT
);

INSERT INTO Authors (ID, Name) VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');


### Table Customers
SQL:
CREATE TABLE Customers (
    ID INT,
    Name TEXT,
    Email TEXT
);

INSERT INTO Customers (ID, Name, Email) VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');


### Table Rents
SQL:
CREATE TABLE Rents (
    ID INT,
    BookID INT,
    CustomerID INT,
    State TEXT
);

INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');

# Consultas SQL

1. Selecciones todos los libros y sus actores

SELECT b.Name, a.Name
From Books b
JOIN Authors a ON b.Author = a.ID;

2. Selecciones los Libros que no tienen autor

SELECT b.Name,
FROM Books b
WHERE b.Authors IS NULL;

3. Seleccion los Autores que no tienen Libros

SELECT a.Name
FROM Authors a
LEFT JOIN Books b ON b.Author = a.ID
WHERE b.ID IS NULL;

4. Seleccione los Libros que hayan sido rentados:

SELECT b.Name
FROM Books b
INNER JOIN Rents r ON b.ID = r.BookID;

5. Seleecione los Libros que no hayan sido rentados:

SELECT b.Name
FROM Books b
LEFT JOIN Rents r ON b.ID = r.BookID
WHERE r.ID IS NULL;

6. Seleccione los Clientes que nunca han rentado un libro

SELECT c.Name
FROM Customers c
LEFT JOIN Rents r ON c.ID = r.CustomerID
WHERE r.ID IS NULL;

7. Seleccione los Libros que han sido rentados con estado "Overdue"

Select b.Name, r.State
From Books b
INNER JOIN Rents r ON b.ID = r.BookID
WHERE r.State = 'Overdue';


