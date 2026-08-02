# Practice exercises CREATE, ALTER, TRUNCATE, DROP

## CREATE

```sql
CREATE TABLE PETSALE (
    ID INTEGER NOT NULL,
    PET CHAR(20),
    SALEPRICE DECIMAL(6,2),
    PROFIT DECIMAL(6,2),
    SALEDATE DATE
    );

CREATE TABLE PET (
    ID INTEGER NOT NULL,
    ANIMAL VARCHAR(20),
    QUANTITY INTEGER
    );
```

## INSERT

```sql
INSERT INTO PETSALE VALUES
    (1,'Cat',450.09,100.47,'2018-05-29'),
    (2,'Dog',666.66,150.76,'2018-06-01'),
    (3,'Parrot',50.00,8.9,'2018-06-04'),
    (4,'Hamster',60.60,12,'2018-06-11'),
    (5,'Goldfish',48.48,3.5,'2018-06-14');

INSERT INTO PET VALUES
    (1,'Cat',3),
    (2,'Dog',4),
    (3,'Hamster',2);
```

## ALTER

### Adding a Column

```sql
ALTER TABLE PETSALE
ADD COLUMN QUANTITY INTEGER;
```

#### Update the newly added QUANTITY column of the PETSAL

```sql
UPDATE PETSALE SET QUANTITY = 9 WHERE ID = 1;
UPDATE PETSALE SET QUANTITY = 3 WHERE ID = 2;
UPDATE PETSALE SET QUANTITY = 2 WHERE ID = 3;
UPDATE PETSALE SET QUANTITY = 6 WHERE ID = 4;
UPDATE PETSALE SET QUANTITY = 24 WHERE ID = 5;
```

### Deleting a column

```sql
ALTER TABLE PETSALE
DROP COLUMN PROFIT;
```

### Modify a column

```sql
ALTER TABLE PETSALE
MODIFY PET VARCHAR(20);
```

### Rename a Column

```sql
ALTER TABLE `PETSALE` CHANGE `PET` `ANIMAL` varchar(20);
```

## TRUNCATE

```sql
TRUNCATE TABLE PET ;
```

## DROP

```sql
DROP TABLE PET;
```

# Practice problems CREATE, ALTER, TRUNCATE, DROP

### 1. Create a new table in the database named Toys with attributes as ID (integer), Variety (variable length string), and Quantity (integer). Make sure the ID is not Null.

```sql
CREATE TABLE Toys (
    ID INTEGER NOT NULL,
    Variety VARCHAR(20),
    Quantity INTEGER
    );
```

### 2. Add the below-mentioned entries to the table using the INSERT statement.

| ID  | Variety      | Quantity |
| --- | ------------ | -------- |
| 1   | Chew toy     | 20       |
| 2   | Balls        | 50       |
| 3   | Bowls        | 30       |
| 4   | Foldable bed | 40       |

```sql
INSERT INTO Toys VALUES
    (1, 'Chew toy', 20),
    (2, 'Balls', 50),
    (3, 'Bowls', 30),
    (4, 'Foldable bed', 40);

```

### 3. ALTER the length of 'Variety' in the table to 30 characters

```sql
ALTER TABLE Toys
MODIFY Variety VARCHAR(30);
```

### 4. TRUNCATE the table 'Toys'

```sql
TRUNCATE TABLE Toys;
```

### 5. DROP the table 'Toys'

```sql
DROP TABLE Toys;
```
