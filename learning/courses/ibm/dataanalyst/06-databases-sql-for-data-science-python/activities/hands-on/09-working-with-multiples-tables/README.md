# Practice exercises Working with Multiple Tables

## Accessing multiple tables with sub-queries

### 1. Retrieve only the EMPLOYEES records corresponding to jobs in the JOBS table

```sql
SELECT * FROM EMPLOYEES WHERE JOB_ID IN (SELECT JOB_IDENT FROM JOBS);
```

### 2. Retrieve JOB information for employees earning over $70,000

```sql
SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY, JOB_IDENT
FROM JOBS
WHERE JOB_IDENT IN (select JOB_ID from EMPLOYEES where SALARY > 70000 );
```

## Accessing multiple tables with Implicit Joins

### 1. Retrieve only the EMPLOYEES records corresponding to jobs in the JOBS table

```sql
SELECT *
FROM EMPLOYEES, JOBS
WHERE EMPLOYEES.JOB_ID = JOBS.JOB_IDENT;
```

### 2. Redo the previous query using shorter aliases for table names

```sql
SELECT *
FROM EMPLOYEES E, JOBS J
WHERE E.JOB_ID = J.JOB_IDENT;
```

### 3. In the previous query, retrieve only the Employee ID, Name, and Job Title

```sql
SELECT EMP_ID,F_NAME,L_NAME, JOB_TITLE
FROM EMPLOYEES E, JOBS J
WHERE E.JOB_ID = J.JOB_IDENT;
```

### 4. Redo the previous query, but specify the fully qualified column names with aliases in the SELECT clause.

```sql
SELECT E.EMP_ID, E.F_NAME, E.L_NAME, J.JOB_TITLE
FROM EMPLOYEES E, JOBS J
WHERE E.JOB_ID = J.JOB_IDENT;
```

# Practice Problems

### 1. Retrieve only the list of employees whose JOB_TITLE is Jr. Designer using sub-queries

```sql
SELECT *
FROM EMPLOYEES
WHERE JOB_ID IN (SELECT JOB_IDENT
	             FROM JOBS
	             WHERE JOB_TITLE= 'Jr. Designer');
```

### 2. Retrieve only the list of employees whose JOB_TITLE is Jr. Designer using implicit joins

```sql
SELECT *
FROM EMPLOYEES E, JOBS J
WHERE E.JOB_ID = J.JOB_IDENT AND J.JOB_TITLE= 'Jr. Designer';
```

### 3. Retrieve JOB information and a list of employees whose birth year is after 1976 using sub-queries

```sql
SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY, JOB_IDENT
FROM JOBS
WHERE JOB_IDENT IN (SELECT JOB_ID
	                FROM EMPLOYEES
	                WHERE YEAR(B_DATE)>1976 );
```

### 4. Retrieve JOB information and a list of employees whose birth year is after 1976 using implict joins

```sql
SELECT J.JOB_TITLE, J.MIN_SALARY, J.MAX_SALARY, J.JOB_IDENT
FROM JOBS J, EMPLOYEES E
WHERE E.JOB_ID = J.JOB_IDENT AND YEAR(E.B_DATE)>1976;
```
