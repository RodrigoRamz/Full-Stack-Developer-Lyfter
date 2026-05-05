1. La operación All - Odd representa una diferencia de conjuntos, donde se obtienen los elementos que están en el conjunto All pero no en el conjunto Odd.

2. En SQL, una operación similar se puede representar utilizando un LEFT JOIN entre dos tablas. El LEFT JOIN permite traer todos los registros de la tabla principal y relacionarlos con otra tabla. Luego, utilizando una condición WHERE con IS NULL, se pueden identificar los registros que no tienen coincidencia en la segunda tabla.

3. El tipo de JOIN que se utiliza es LEFT JOIN, combinado con una condición WHERE IS NULL para filtrar los elementos que no existen en la segunda tabla.


2. Agrupamiento y conteo cruzado

SELECT c.Name, COUNT(r.ID) AS TotalRents
FROM Customers c
JOIN Rents r ON c.ID = r.CustomerID
GROUP BY c.Name
ORDER BY TotalRents DESC
LIMIT 3;

3. Consulta con múltiples JOINS anidados

SELECT c.Name AS Customer,
       b.Name AS Book,
       a.Name AS Author,
       r.State
FROM Rents r
JOIN Customer c ON c.ID = r.CustomerID
JOIN Books b ON b.ID = r.BookID
LEFT JOIN Authors ON b.Author = a.ID;