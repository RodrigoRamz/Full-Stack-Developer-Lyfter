
### Tabla Original
|Order ID|Customer Name|Customer Phone|Address|Item ID|Price|Quantity|Special Request|Delivery Time|
|---|---|---|---|---|---|---|---|---|---|

| Order ID | Customer Name | Customer Phone | Address        | Item ID | Item Name    | Price | Quantity | Special Request | Delivery Time |
| -------- | ------------- | -------------- | -------------- | ------- | ------------ | ----- | -------- | --------------- | ------------- |
| 001      | Alice         | 123-456-7890   | 123 Main St    | 101     | Cheeseburger | 8     | 2        | No onions       | 6:00 PM       |
| 001      | Alice         | 123-456-7890   | 123 Main St    | 102     | Fries        | 3     | 1        | Extra ketchup   | 6:00 PM       |
| 002      | Bob           | 987-654-3210   | 456 Elm St     | 103     | Pizza        | 12    | 1        | Extra cheese    | 7:30 PM       |
| 002      | Bob           | 987-654-3210   | 456 Elm St     | 104     | Fries        | 3     | 2        | None            | 7:30 PM       |
| 003      | Claire        | 555-123-4567   | 789 Oak St     | 105     | Salad        | 6     | 1        | No croutons     | 12:00 PM      |
| 004      | Claire        | 555-123-4567   | 464 Georgia St | 106     | Water        | 1     | 1        | None            | 5:00 PM       |


### 1FN

Para eliminar redundancia.

Cada columna debe tener datos atomicos
Cada registro debe ser un dato identificable

Primary Key: (Order ID, Item ID)

### 2FN

Para eliminar dependencias parciales

La tabla tiene atributos que dependen solo de Order ID

- Customer Name
- Customer Phone
- Address
- Delivery Time

Otros atribitos dependientes son los que dependen de Item ID

- Items Name
- Price

Orders Table

| Order ID | Customer Name | Customer Phone | Address        | Delivery Time |
| -------- | ------------- | -------------- | -------------- | ------------- |
| 001      | Alice         | 123-456-7890   | 123 Main St    | 6:00 PM       |
| 002      | Bob           | 987-654-3210   | 456 Elm St     | 7:30 PM       |
| 003      | Claire        | 555-123-4567   | 789 Oak St     | 12:00 PM      |
| 004      | Claire        | 555-123-4567   | 464 Georgia St | 5:00 PM       |

Items Table

| Item ID | Item Name    | Price |
| ------- | ------------ | ----- |
| 101     | Cheeseburger | 8     |
| 102     | Fries        | 3     |
| 103     | Pizza        | 12    |
| 104     | Fries        | 3     |
| 105     | Salad        | 6     |
| 106     | Water        | 1     |

OrderItems Table

| Order ID | Item ID | Quantity | Special Request |
| -------- | ------- | -------- | --------------- |
| 001      | 101     | 2        | No onions       |
| 001      | 102     | 1        | Extra ketchup   |
| 002      | 103     | 1        | Extra cheese    |
| 002      | 104     | 2        | None            |
| 003      | 105     | 1        | No croutons     |
| 004      | 106     | 1        | None            |

### 3FN

Para eliminar dependencias transitivas

Customer Phone depende de Customer Name (Un cliente puede tener mas de una orden, debe haber una tabla para ordenes)

Customer Table

| Customer ID | Name   | Phone        |
| ----------- | ------ | ------------ |
| 1           | Alice  | 123-456-7890 |
| 2           | Bob    | 987-654-3210 |
| 3           | Claire | 555-123-4567 |

Orders Table

| Order ID | Customer ID | Address        | Delivery Time |
| -------- | ----------- | -------------- | ------------- |
| 001      | 1           | 123 Main St    | 6:00 PM       |
| 002      | 2           | 456 Elm St     | 7:30 PM       |
| 003      | 3           | 789 Oak St     | 12:00 PM      |
| 004      | 3           | 464 Georgia St | 5:00 PM       |

### Tablas Finales
Customers
Orders
Items
OrderItems
