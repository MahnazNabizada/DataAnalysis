# Graded Quiz - Questions and Answers

## Module 1 - Basic SQL

1. **Assume an INSTRUCTOR table exists with columns including FIRSTNAME, LASTNAME, and others. What would be the most likely result set for the query:**

   ```sql
   SELECT DISTINCT FIRSTNAME FROM INSTRUCTOR
   ```

   - [ ] LEON, PAUL, LEON, JOE
   - [ ] LEON KATSNELSON, PAUL ZIKOPOLOUS, JOE SANTARCANGELO
   - [x] LEON, PAUL, JOE
   - [ ] LEON, LEON, PAUL, PAUL, LEON, PAUL, JOE

     **Answer:** The DISTINCT keyword is used to return only distinct or different rows.

2. **What does the following statement do?**

   ```sql
   UPDATE INSTRUCTOR SET LASTNAME = 'Brewster' WHERE LASTNAME = 'Smith'
   ```

   - [ ] Changes the last name of the instructor named 'Brewster' to 'Smith.'
   - [ ] Updates all rows in the table to have the last name 'Brewster.'
   - [x] Changes the last name of all instructors named 'Smith' to 'Brewster.'
   - [ ] Updates all rows in the table to have the last name 'Smith.'

     **Answer:** This statement updates the last name of all instructors named 'Smith' to 'Brewster.'

3. **What would occur if you executed a DELETE FROM statement on a table without the WHERE clause?**
   - [ ] The command would result in an error.
   - [ ] The command would only delete the first entry in the table.
   - [x] The command would remove all entries in the table, leaving it empty but still present in the database.
   - [ ] The command would delete the table from the database.

   **Answer:** Without the WHERE clause, the DELETE statement removes all entries from a table, leaving it empty in the database.

4. **What is the expected result of the following SQL statement?**

   ```sql
   SELECT COUNT(DISTINCT FIRSTNAME) FROM INSTRUCTOR
   ```

   - [x] The number of unique FIRSTNAME entries in the INSTRUCTOR table.
   - [ ] Only the distinct FIRSTNAME entries.
   - [ ] The statement would throw an error.
   - [ ] The count of unique entries along with the distinct FIRSTNAME entries.

   **Answer:** The DISTINCT keyword identifies unique entries, and COUNT returns the number of these distinct entries.

5. **Considering the execution of the following SQL statement, what would be the expected output?**

   ```sql
   SELECT * FROM INSTRUCTOR WHERE LASTNAME='Smith' LIMIT 5
   ```

   - [ ] The first 5 rows from the INSTRUCTOR table.
   - [ ] The last 5 rows from the INSTRUCTOR table.
   - [ ] The last 5 entries in the INSTRUCTOR table where LASTNAME is 'Smith.'
   - [x] The first 5 entries in the INSTRUCTOR table where LASTNAME is 'Smith.'

   **Answer:** The WHERE clause filters the results based on the LASTNAME, and the LIMIT clause restricts the output to the first 5 rows.

## Module 2 - DB Concepts and Tables

1. **Which of the following statements about a database is/are correct?**
   - [x] A database is a logically coherent collection of data with some inherent meaning
   - [ ] Data can only be added and queried from a database but not modified.
   - [ ] Only SQL can be used to query data in a database.
   - [ ] All of the above

   **Answer:** A database is a repository or logically coherent collection of data with some inherent meaning.

2. **Attributes of an entity become **\_\_\_\_** in a table.**
   - [x] columns
   - [ ] keys
   - [ ] constraints
   - [ ] rows

   **Answer:** Attributes of an entity become columns in a table.

3. **The CREATE TABLE statement is a **\_\_\_\_**.**
   - [ ] DML statement
   - [x] DDL statement
   - [ ] DQL statement
   - [ ] All of the above

   **Answer:** The CREATE TABLE statement defines a table, so it is a DDL statement.

4. **Which command is used for removing a table and all its data from the database?**
   - [x] DROP table command
   - [ ] CREATE command
   - [ ] TRUNCATE table command
   - [ ] ALTER table command

   **Answer:** Drop command deletes the entire table along with its contents from the database.

5. **What would be the correct syntax to add a column 'ID' that contains 7 character alpha-numeric values to a database table 'Employees' using MySQL?**
   - [ ] `ALTER Employees TABLE ADD ID char`
   - [ ] `ALTER Employees ADD COLUMN ID varchar(7)`
   - [x] `ALTER TABLE Employees ADD ID char(7)`
   - [ ] `ALTER TABLE COLUMN Employees ID char(7)`

   **Answer:** This is the appropriate syntax for the said task.

## Module 3 - Refining Your Results

1. **You want to select the author's `lastname` from a table, but you only remember that it starts with the letter `J`. Which of the following queries uses the correct string pattern?**
   - [ ] `SELECT lastname FROM author WHERE lastname LIKE 'J#';`
   - [x] `SELECT lastname FROM author WHERE lastname LIKE 'J%';`
   - [ ] `SELECT lastname FROM author WHERE lastname LIKE 'J*';`
   - [ ] `SELECT lastname FROM author WHERE lastname LIKE 'J$';`

   **Answer:** The `%` wildcard represents zero or more characters, so `LIKE 'J%'` returns all last names that begin with the letter `J`.

2. **In SQL, which of the following is the correct way to sort a result set in descending order?**
   - [x] `SELECT * FROM TABLE_NAME ORDER BY ID DESC;`
   - [ ] `SELECT ID FROM TABLE_NAME ORDER BY ID;`
   - [ ] `SELECT ID FROM TABLE_NAME ORDER BY ID DESC;`
   - [ ] `SELECT * FROM TABLE_NAME ORDER BY ID;`

   **Answer:** The `DESC` keyword sorts the results in descending order. `ORDER BY ID DESC` arranges records from the highest ID to the lowest.

3. **What is the role of the `HAVING` clause in SQL queries in MySQL?** _(Select all that apply.)_
   - [ ] Checks whether individual data records meet a specified condition.
   - [x] Restricts the result set for a query using the `GROUP BY` clause.
   - [x] It does **not** organize the result set in a specific order.
   - [ ] Acts as an alternative to the `WHERE` clause in all SQL queries.

   **Answer:** The `HAVING` clause is used with `GROUP BY` to filter grouped results based on aggregate conditions. Unlike `ORDER BY`, it does not sort the results.

4. **Which of the following best describes the function of the SQL query below?**

   ```sql
   SELECT *
   FROM employees
   ORDER BY emp_name
   LIMIT 5;
   ```

   - [ ] Retrieves the top 5 `emp_name` values ordered alphabetically.
   - [ ] Retrieves the entire contents of the table, sorted alphabetically by `emp_name`.
   - [x] Retrieves all the columns of the first 5 rows of the table, sorted alphabetically by `emp_name`.
   - [ ] Retrieves all the columns of the first 5 rows of the table, sorted in reverse alphabetical order by `emp_name`.

   **Answer:** `ORDER BY emp_name` sorts the records alphabetically, and `LIMIT 5` returns only the first five rows from the sorted result.

5. **Which of the following SQL statements lists the number of customers in each country, showing only the countries with more than five customers?**
   - [x] `SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) > 5;`
   - [ ] `SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING CustomerID > 5;`
   - [ ] `SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(Customers) > 5;`
   - [ ] `SELECT COUNT(CustomerID), Country FROM Customers GROUP BY Country HAVING COUNT(CustomerID) < 5;`

   **Answer:** `GROUP BY Country` groups customers by country, `COUNT(CustomerID)` counts the customers in each group, and `HAVING COUNT(CustomerID) > 5` filters the results to include only countries with more than five customers.

## Module 3 - Functions, Multiple Tables, and Sub-queries

1. **Which of the following queries will return the data for employees who belong to the department with the highest department ID?**
   - [ ] `SELECT * FROM EMPLOYEES WHERE DEP_ID = MAX(DEP_ID);`
   - [ ] `SELECT * FROM EMPLOYEES WHERE DEPT_ID_DEP = MAX(SELECT DEPT_ID_DEP FROM DEPARTMENTS);`
   - [x] `SELECT * FROM EMPLOYEES WHERE DEP_ID = (SELECT MAX(DEPT_ID_DEP) FROM DEPARTMENTS);`
   - [ ] `SELECT * FROM EMPLOYEES WHERE DEP_ID = (SELECT DEPT_ID_DEP FROM DEPARTMENTS WHERE DEPT_ID_DEP IS MAX);`

   **Answer:** This query uses a subquery with the `MAX()` function to retrieve the highest department ID from the `DEPARTMENTS` table, then returns all employees belonging to that department.

2. **A `DEPARTMENTS` table contains `DEP_NAME` and `DEPT_ID_DEP` columns, and an `EMPLOYEES` table contains `F_NAME` and `DEP_ID`. You want to retrieve the department name for each employee. Which query correctly accomplishes this?**
   - [ ] `SELECT E.F_NAME, D.DEP_NAME FROM EMPLOYEES, DEPARTMENTS;`
   - [ ] `SELECT D.F_NAME, E.DEP_NAME FROM EMPLOYEES E, DEPARTMENTS D WHERE D.DEPT_ID_DEP = E.DEP_ID;`
   - [ ] `SELECT F_NAME, DEP_NAME FROM EMPLOYEES E, DEPARTMENTS D WHERE E.DEPT_ID_DEP = D.DEP_ID;`
   - [x] `SELECT F_NAME, DEP_NAME FROM EMPLOYEES, DEPARTMENTS WHERE DEPT_ID_DEP = DEP_ID;`

   **Answer:** This query performs an **implicit join** between the `EMPLOYEES` and `DEPARTMENTS` tables by matching `DEP_ID` with `DEPT_ID_DEP`, allowing the employee's first name and department name to be returned together.

3. **You are writing a query that will give you the total cost to the Pet Rescue organization of rescuing animals. The cost of each rescue is stored in the `Cost` column, and you want the result column to be called `Total_Cost`. Which SQL query is correct?**
   - [ ] `SELECT SUM(Cost) FROM PetRescue;`
   - [x] `SELECT SUM(Cost) AS Total_Cost FROM PetRescue;`
   - [ ] `SELECT SUM(Total_Cost) FROM PetRescue;`
   - [ ] `SELECT Total_Cost FROM PetRescue;`

   **Answer:** The `SUM(Cost)` aggregate function calculates the total rescue cost, and the `AS` keyword assigns the alias `Total_Cost` to the result column.

4. **Which of the following queries correctly calculates the total number of days an employee has lived, using their date of birth (`DOB`) and the current date, in MySQL?**
   - [ ] `SELECT (CURRENT_DATE - DOB) FROM Employees;`
   - [x] `SELECT DATEDIFF(CURRENT_DATE, DOB) FROM Employees;`
   - [ ] `SELECT FROM_DAYS(DATEDIFF(CURRENT_DATE, DOB)) FROM Employees;`
   - [ ] `SELECT FROM_DAYS(DATE_SUB(CURRENT_DATE, DOB)) FROM Employees;`

   **Answer:** The `DATEDIFF()` function returns the number of days between two dates. In this case, it calculates the number of days from the employee's date of birth to the current date.

5. **You have a table of medicines named `MEDS`. The manufacturing date is stored in the `DOM` column, and each medicine expires exactly one year later. Which SQL statement generates the medicine name and its expiry date as a column named `DOE`?**
   - [ ] `SELECT NAME, DATE_ADD(DOM, INTERVAL 1 YEARS) AS DOE FROM MEDS;`
   - [ ] `SELECT NAME, DATEADD(DOM, INTERVAL 1 YEAR) FROM MEDS;`
   - [x] `SELECT NAME, DATE_ADD(DOM, INTERVAL 1 YEAR) AS DOE FROM MEDS;`
   - [ ] `SELECT NAME, DATEADD(DOM, INTERVAL 1 YEAR) AS DOE FROM MEDS;`

   **Answer:** The `DATE_ADD()` function adds one year to the manufacturing date (`DOM`), and the `AS DOE` clause assigns the alias `DOE` to the calculated expiry date column.

## Module 4 - Accessing databases using Python

1. **Which of the following statements establishes the connection between a Jupyter Notebook SQL extension and an SQLite database `EMP.db`?**
   - [x] `%sql sqlite:///EMP.db`
   - [ ] `%sql`<br>`sqlite:///EMP.db`
   - [ ] `%sql sqlite:/EMP.db`
   - [ ] `%sql sqlite3://EMP.db`

   **Answer:** `%sql sqlite:///EMP.db` is the correct syntax for establishing a connection between a Jupyter Notebook SQL extension and an SQLite database.

2. **Which two of the following can be stated as uses of cell magic in Jupyter Notebooks?** _(Select two.)_
   - [x] Coding in a Jupyter Notebook using a programming language other than Python.
   - [ ] Converting Jupyter Notebook's default programming language to a desired one.
   - [x] Timing a complete cell block as required.
   - [ ] Loading an SQL database into a Jupyter Notebook.

   **Answer:** Cell magic commands operate on an entire notebook cell. Common uses include executing code in languages other than Python (such as SQL) and timing the execution of an entire cell.

3. **What would be the outcome of the following Python code?**

   ```python
   import sqlite3
   import pandas as pd

   conn = sqlite3.connect('HR.db')
   data = pd.read_csv('./employees.csv')
   data.to_sql('Employees', conn)
   ```

   - [x] The CSV file is read and converted into an SQL table `Employees` under the `HR` database.
   - [ ] The CSV file is converted to an SQL file.
   - [ ] The code throws a syntax error.
   - [ ] The CSV file is saved to the `HR.db` file created by the code.

   **Answer:** The `read_csv()` function loads the CSV file into a pandas DataFrame, and `to_sql()` writes that DataFrame to an SQL table named `Employees` in the SQLite database.

4. **What is the correct way to query a database table using Python?** _(Choose two.)_
   - [x] `out = pandas.read_sql(query_statement, connection_object)`
   - [ ] `out = dataframe.read_sql(query_statement, connection_object)`
   - [x]
     ```python
     cursor = connection.execute(query_statement)
     out = cursor.fetchall()
     ```
   - [ ] `out = connection.execute(query_statement)`

   **Answer:** You can query a database using either `pandas.read_sql()` to return the results as a DataFrame or by executing the query with a database cursor and retrieving the results using `fetchall()`.

5. **Which of the following statements would you use to perform a statistical analysis of data in a pandas DataFrame `df`?**
   - [x] `df.describe()`
   - [ ] `df.head()`
   - [ ] `df.tail()`
   - [ ] `df.info()`

   **Answer:** The `describe()` method generates descriptive statistics for the DataFrame, including count, mean, standard deviation, minimum, maximum, and quartile values.
