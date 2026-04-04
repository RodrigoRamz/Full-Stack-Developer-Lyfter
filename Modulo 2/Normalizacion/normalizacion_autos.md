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
|VIN|Make|Model|Year|Color|

Owners Table
|Owner ID|Owner Name|Owner Phone|

CarsOwners Table
|VIN|Owner ID|

### 3FN

La columan Insurance Company se separa en una tabla nueva para evitar redundancias

InsuranceCompanies Table
|Company ID|Name|

InsurancePolicies Table
|Policy ID|VIN|Company ID|

Tablas Normalizadas:
- Cars
- Owners
- CarOwners
- InsuranceCompanies
- InsurancePolicies

