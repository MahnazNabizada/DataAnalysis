# Practice exercises Sub-queries and Nested Selects

### 1. Retrieve all employee records whose salary is lower than the average salary

```sql
SELECT *
FROM EMPLOYEES
WHERE SALARY < (SELECT AVG(SALARY) FROM EMPLOYEES);
```

### 2. Retrieve all employee records with EMP_ID, SALARY, and maximum salary as MAX_SALARY in every row

```sql
SELECT EMP_ID, SALARY, (SELECT MAX(SALARY) FROM EMPLOYEES) AS MAX_SALARY
FROM EMPLOYEES;
```

### 3. Extract the first and last names of the oldest employee

```sql
SELECT F_NAME, L_NAME
FROM EMPLOYEES
WHERE B_DATE = (SELECT MIN(B_DATE) FROM EMPLOYEES);
```

### 4. Extract the average salary of the top 5 earners in the company

```sql
SELECT AVG(SALARY)
FROM (SELECT SALARY
	  FROM EMPLOYEES
	  ORDER BY SALARY DESC
	  LIMIT 5) AS SALARY_TABLE;
```

# Practice Problems

### 1. Write a query to find the average salary of the five least-earning employees

```sql
SELECT AVG(SALARY)
FROM (SELECT SALARY
	  FROM EMPLOYEES
	  ORDER BY SALARY
	  LIMIT 5) AS SALARY_TABLE;
```

### 2. Write a query to find the records of employees older than the average age of all employees

```sql
SELECT *
FROM EMPLOYEES
WHERE YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,B_DATE))) >
	(SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE,B_DATE))))
	FROM EMPLOYEES);
```

### 3. From the Job_History table, display the list of Employee IDs, years of service, and average years of service for all entries

```sql
SELECT EMPL_ID, YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE))),
	(SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE))))
	FROM JOB_HISTORY)
FROM JOB_HISTORY;
```
