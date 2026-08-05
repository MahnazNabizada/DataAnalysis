# Using Views - MYSQL

## Create a View

### 1. Let's create a view called EMPSALARY to display salary along with some basic sensitive data of employees from the HR database. To create the EMPSALARY view from the EMPLOYEES table, Copy the code below and paste it to the textarea of the SQL page. Click Go.

```sql
CREATE VIEW EMPSALARY AS
SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, SALARY
FROM EMPLOYEES;
```

### 2. Using SELECT, query the EMPSALARY view to retrieve all the records. Use the following statement.

```sql
SELECT * FROM EMPSALARY;
```

## Update a View

### 3. Assume that the EMPSALARY view we created in Task 1 doesn't contain enough salary information, such as max/min salary and the job title of the employees. For this, we need to get information from other tables in the database. You need all columns from EMPLOYEES table used above, except for SALARY. You also need the columns JOB_TITLE, MIN_SALARY, MAX_SALARY of the JOBS table. The command to be used is as follows:

```sql
CREATE OR REPLACE VIEW EMPSALARY AS
SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, JOB_TITLE,
MIN_SALARY, MAX_SALARY
FROM EMPLOYEES, JOBS
WHERE EMPLOYEES.JOB_ID = JOBS.JOB_IDENT;
```

### 4. Using SELECT, query the updated EMPSALARY view to retrieve all the records

```sql
SELECT * FROM EMPSALARY;
```

## Drop a View

### 5. Drop the created View EMPSALARY

```sql
DROP VIEW EMPSALARY;
```

# Practice Problems

### 1. Create a view "EMP_DEPT" which has the following information. EMP_ID, FNAME, LNAME and DEP_ID from EMPLOYEES table

```sql
CREATE VIEW EMP_DEPT AS
SELECT EMP_ID, F_NAME, L_NAME, DEP_ID
FROM EMPLOYEES;
```

### 2. Modify "EMP_DEPT" such that it displays Department names instead of Department IDs. For this, we need to combine information from EMPLOYEES and DEPARTMENTS as follows.

```sql
CREATE OR REPLACE VIEW EMP_DEPT AS
SELECT EMP_ID, F_NAME, L_NAME, DEP_NAME
FROM EMPLOYEES, DEPARTMENTS
WHERE EMPLOYEES.DEP_ID = DEPARTMENTS.DEPT_ID_DEP;
```

### 3. Drop the view "EPM_DEPT"

```sql
DROP VIEW EMP_DEPT
```
