# Practice exercises Built-in Functions

## Aggregation Functions

### 1. Write a query that calculates the total cost of all animal rescues in the PETRESCUE table

```sql
SELECT SUM(COST) AS SUM_OF_COST FROM PETRESCUE;
```

### 2. Write a query that displays the maximum quantity of animals rescued (of any kind)

```sql
SELECT MAX(QUANTITY) FROM PETRESCUE;
```

### 3. Write a query that displays the average cost of animals rescued

```sql
SELECT AVG(COST) FROM PETRESCUE;
```

## Scalar Functions and String Functions

### Write a query that displays the rounded integral cost of each rescue

```sql
SELECT ROUND(COST, 2) FROM PETRESCUE;
```

### 2. Write a query that displays the length of each animal name

```sql
SELECT LENGTH(ANIMAL) FROM PETRESCUE;
```

### 3. Write a query that displays the animal name in each rescue in uppercase

```sql
SELECT UCASE(ANIMAL) FROM PETRESCUE;
```

### 4. Write a query that displays the animal name in each rescue in lowercase

```sql
SELECT LCASE(ANIMAL) FROM PETRESCUE;
```

## Date Functions

### 1. Write a query that displays the rescue date day

```sql
SELECT DAY(RESCUEDATE) FROM PETRESCUE;
```

### 2. Write a query that displays the rescue date month

```sql
SELECT MONTH(RESCUEDATE) FROM PETRESCUE;
```

### 3. Write a query that displays the rescue date year

```sql
SELECT YEAR(RESCUEDATE) FROM PETRESCUE;
```

### 4. Animals rescued should see the vet within three days of arrival. Write a query that displays the third day of each rescue

```sql
SELECT DATE_ADD(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE
```

### 5. Animals rescued should see the vet within three days of arrival. Write a query that displays the 2 months of each rescue

```sql
SELECT DATE_ADD(RESCUEDATE, INTERVAL 2 MONTH) FROM PETRESCUE
```

### 6. Animals rescued should see the vet within three days of arrival. Write a query that displays the 3 days before of each rescue

```sql
SELECT DATE_SUB(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE
```

### 7. Write a query that displays the length of time the animals have been rescued, for example, the difference between the current date and the rescue date

```sql
SELECT DATEDIFF(CURRENT_DATE, RESCUEDATE) FROM PETRESCUE
```

### 8 Present the output in a YYYY-MM-DD format using function FROM_DAYS(number_of_days)

```sql
SELECT FROM_DAYS(DATEDIFF(CURRENT_DATE, RESCUEDATE)) FROM PETRESCUE
```

# Practice Problems

### 1. Write a query that displays the average cost of rescuing a single dog. Note that the cost per dog would not be the same in different instances

```sql
SELECT AVG(COST/QUANTITY) FROM PETRESCUE WHERE ANIMAL = 'Dog';
```

### 2. Write a query that displays the animal name in each rescue in uppercase without duplications

```sql
SELECT DISTINCT UCASE(ANIMAL) FROM PETRESCUE;
```

### 3. Write a query that displays all the columns from the PETRESCUE table where the animal(s) rescued are cats. Use cat in lowercase in the query

```sql
SELECT * FROM PETRESCUE WHERE LCASE(ANIMAL)="cat";
```

### 4. Write a query that displays the number of rescues in the 5th month

```sql
SELECT SUM(QUANTITY) FROM PETRESCUE WHERE MONTH(RESCUEDATE)="05";
```

### 5. The rescue shelter is supposed to find good homes for all animals within 1 year of their rescue. Write a query that displays the ID and the target date

```sql
SELECT ID, DATE_ADD(RESCUEDATE, INTERVAL 1 YEAR) FROM PETRESCUE;
```
