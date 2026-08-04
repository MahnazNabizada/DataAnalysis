# Practice exercises String Patterns, Sorting and Grouping

## Strings Patterns

### 1. Retrieve the first names F_NAME and last names L_NAME of all employees who live in Elgin, IL

```sql
SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE ADDRESS LIKE '%Elgin,IL%';
```

### 2. Retrieve the employees who were born during the 70s

```sql
SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE B_DATE LIKE '197%';
```

### 3. Retrieve all employee records in department 5 where salary is between 60000 and 70000

```sql
SELECT *
FROM EMPLOYEES
WHERE (SALARY BETWEEN 60000 AND 70000) AND DEP_ID = 5;
```

## Sorting

### 1. Retrieve a list of employees ordered by department ID

```sql
SELECT F_NAME, L_NAME, DEP_ID
FROM EMPLOYEES
ORDER BY DEP_ID;
```

### 2. Retrieve a list of employees in descending order of department ID, and within each deaprtment, the records should be ordered in descending alphabetical order by last name

```sql
SELECT F_NAME, L_NAME, DEP_ID
FROM EMPLOYEES
ORDER BY DEP_ID DESC, L_NAME DESC;
```

## Grouping

### 1. Retrieve the number of employees for each department.

```sql
SELECT DEP_ID, COUNT(*)
FROM EMPLOYEES
GROUP BY DEP_ID;
```

### 2. Retrieve the number of employees in the department and the average employee salary for each department

```sql
SELECT DEP_ID, COUNT(*), AVG(SALARY)
FROM EMPLOYEES
GROUP BY DEP_ID;
```

### 3. Retrieve the last query and label the computed columns in the result set of the last problem as NUM_EMPLOYEES and AVG_SALARY

```sql
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID;
```

### 4. Sort the result of the previous query by average salary

```sql
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
ORDER BY AVG_SALARY;
```

### 5. Limit the result to departments with fewer than 4 employees

```sql
SELECT DEP_ID, COUNT(*) AS "NUM_EMPLOYEES", AVG(SALARY) AS "AVG_SALARY"
FROM EMPLOYEES
GROUP BY DEP_ID
HAVING count(*) < 4
ORDER BY AVG_SALARY;
```

# Practice Questions

### 1. Retrieve the list of all employees, first and last names, whose first names start with 'S'.

```sql
SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE F_NAME LIKE 'S%';
```

### 2. Arrange all the records of the EMPLOYEES table in ascending order of the date of birth.

```sql
SELECT *
FROM EMPLOYEES
ORDER BY B_DATE;
```

### 3. Group the records in terms of the department IDs and filter them of ones that have average salary more than or equal to 60000. Display the department ID and the average salary.

```sql
SELECT DEP_ID, AVG(SALARY)
FROM EMPLOYEES
GROUP BY DEP_ID
HAVING AVG(SALARY) >= 60000;
```

### For the problem above, sort the results for each group in descending order of average salary.

```sql
SELECT DEP_ID, AVG(SALARY)
FROM EMPLOYEES
GROUP BY DEP_ID
HAVING AVG(SALARY) >= 60000
ORDER BY AVG(SALARY) DESC;
```
