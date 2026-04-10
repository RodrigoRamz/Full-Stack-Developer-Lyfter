### Tabla Original

| VIN         | Make      | Model  | Year | Color  | Owner ID | Owner Name | Owner Phone  | Insurance Company | Insurance Policy |
| ----------- | --------- | ------ | ---- | ------ | -------- | ---------- | ------------ | ----------------- | ---------------- |
| 1HGCM82633A | Honda     | Accord | 2003 | Silver | 101      | Alice      | 123-456-7890 | ABC Insurance     | POL12345         |
| 1HGCM82633A | Honda     | Accord | 2003 | Silver | 102      | Bob        | 987-654-3210 | XYZ Insurance     | POL54321         |
| 5J6RM4H79EL | Honda     | CR-V   | 2014 | Blue   | 103      | Claire     | 555-123-4567 | DEF Insurance     | POL67890         |
| 1G1RA6EH1FU | Chevrolet | Volt   | 2015 | Red    | 104      | Dave       | 111-222-3333 | GHI Insurance     | POL98765         |


### 1FN
Los valores de la tabla son atomicos
Cada fila es identificable

### 2FN 

La tabla tiene dependencias. 
La columna VIN determina: Make, Model, Year, Color
La columna Owner ID determina: Owner Name, Owner Phone

Se debe separa las tablas

Cars Table

| VIN         | Make      | Model  | Year | Color  | 
| ----------- | --------- | ------ | ---- | ------ |
| 1HGCM82633A | Honda     | Accord | 2003 | Silver |
| 1HGCM82633A | Honda     | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda     | CR-V   | 2014 | Blue   |
| 1G1RA6EH1FU | Chevrolet | Volt   | 2015 | Red    |

Owners Table
| Owner ID | Owner Name | Owner Phone  |
| -------- | ---------- | ------------ |
| 101      | Alice      | 123-456-7890 |
| 102      | Bob        | 987-654-3210 |
| 103      | Claire     | 555-123-4567 |
| 104      | Dave       | 111-222-3333 |

CarsOwners Table

| VIN         | Owner ID |
|-------------|----------|
| 1HGCM82633A | 101      |
| 1HGCM82633A | 102      |
| 5J6RM4H79EL | 103      |
| 1G1RA6EH1FU | 104      |

### 3FN

La columan Insurance Company se separa en una tabla nueva para evitar redundancias

InsuranceCompanies Table
|Company ID|Name         |
|----------|-------------|
|1         |ABC Insurance|
|2         |XYZ Insurance|
|3         |DEF Insurance|
|4         |GHI Insurance|

InsurancePolicies Table
| Policy ID | VIN         | Company ID |
| --------- | ----------- | ---------- |
| POL12345  | 1HGCM82633A | 1          |
| POL54321  | 1HGCM82633A | 2          |
| POL67890  | 5J6RM4H79EL | 3          |
| POL98765  | 1G1RA6EH1FU | 4          |


Tablas Normalizadas:
- Cars
- Owners
- CarOwners
- InsuranceCompanies
- InsurancePolicies

