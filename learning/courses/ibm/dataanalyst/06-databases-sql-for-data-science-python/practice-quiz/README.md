# Practice Quiz - Questions and Answers

## Module 1 - Basic SQL

1. **Which of the following statements about databases is accurate? Select all that apply.**
   - [x] Databases can store data and allow queries on that data.
   - [x] Various types of databases exist, such as relational, hierarchical, and NoSQL.
   - [x] A database serves as a data repository.
   - [ ] All databases store data only in fixed tables of rows and columns.

   **Answer:** A key capability of databases is retrieving, filtering, and analyzing stored data through queries. Databases are implemented using different models, each suited to different data structures and use cases. Databases are designed to store and organize data so it can be managed and used.

2. **Which SQL statement is primarily used to retrieve data from a table?**
   - [ ] DELETE
   - [ ] INSERT
   - [x] SELECT
   - [ ] UPDATE

   **Answer:** The SELECT statement is used to retrieve data from one or more tables.

3. **In a Film database with a FilmLocations table, you wish to retrieve a list of films from 2019. However, the query you ran displayed all the films. The query in question is:** `SELECT Title, ReleaseYear, Locations FROM FilmLocations`. **What element is absent from the query?**
   - [x] A WHERE clause that limits the results to films from 2019.
   - [ ] A DISTINCT clause to ensure a specific year's uniqueness.
   - [ ] The query is already correct.
   - [ ] A LIMIT clause to restrict the output to films from 2019.

   **Answer:** To isolate films from 2019, the query must include a WHERE clause such as `WHERE ReleaseYear=2019`.

4. **Which of these statements correctly introduces a new entry to the 'Instructor' table?**
   - [ ] `UPDATE Instructor(...) WITH VALUES(...)`
   - [ ] `ADD INTO Instructor(...) VALUES(...)`
   - [ ] `SELECT Instructor(...) FROM VALUES(...)`
   - [x] `INSERT INTO Instructor(ins_id, lastname, firstname, city, country) VALUES(4, 'Doe', 'John', 'Sydney', 'AU')`

   **Answer:** The INSERT INTO statement is designed to append new rows to tables.

5. **In an UPDATE statement, what purpose does the WHERE clause serve?**
   - [ ] The UPDATE statement never incorporates a WHERE clause.
   - [ ] The WHERE clause designates a new table to accept the updates.
   - [ ] It dictates which column/data gets updated.
   - [x] It defines which specific rows should be updated.

   **Answer:** The WHERE clause filters the result set. Omitting it would mean updating every row in the table.

## Module 2 - Introduction to Relational Databases and Tables

1. **What is the function of a primary key?**
   - [x] The primary key uniquely identifies each row in a table.
   - [ ] The primary key is used to identify any rows in the table that contain NULL values.
   - [ ] The primary key is used to grant access to a table.
   - [ ] The primary key enables you to add data to columns.

   **Answer:** The primary key uniquely identifies each row in a table.

2. **True or False: Data Manipulation Language statements like INSERT, SELECT, UPDATE, and DELETE are used to read and modify data.**
   - [x] True
   - [ ] False

   **Answer:** Data Manipulation Language statements like INSERT, SELECT, UPDATE, and DELETE are used to read and modify data.

3. **Data Definition Language (or DDL) statements are used to define, change, or delete database objects such as tables. Which of the following statements are all DDL statements?**
   - [ ] SELECT and DELETE
   - [ ] INSERT and UPDATE
   - [x] CREATE, ALTER, DROP
   - [ ] SELECT, INSERT, UPDATE

   **Answer:** The CREATE, ALTER, and DROP statements act on objects such as tables, not the data within the table.

4. **Which of the following queries will change the data type of an existing column (phone) to the varchar data type?**
   - [x] `ALTER TABLE author MODIFY phone VARCHAR(20);`
   - [ ] `ALTER TABLE author ALTER COLUMN phone SET TYPE VARCHAR(20);`
   - [ ] `ALTER COLUMN phone SET DATA TYPE VARCHAR(20);`
   - [ ] `ALTER TABLE author ALTER COLUMN phone DATA TYPE = VARCHAR(20);`

   **Answer:** This query will change the data type to varchar.

5. **The five basic SQL commands are:**
   - [ ] None of the above
   - [ ] CREATE, INSERT, RETRIEVE, MODIFY, DELETE
   - [ ] SELECT, COPY, PASTE, INSERT, ALTER
   - [x] CREATE, SELECT, INSERT, UPDATE, DELETE

   **Answer:** The five basic SQL commands are CREATE, SELECT, INSERT, UPDATE, and DELETE.

## Module 3 - Refining Your Results

1. **You want to retrieve a list of employees in alphabetical order of `Lastname` from the `Employees` table. Which SQL statement should you use?**
   - [ ] `SELECT * FROM Employees ORDER BY Lastname DESC;`
   - [ ] `SELECT * FROM Employees SORT BY Lastname;`
   - [x] `SELECT * FROM Employees ORDER BY Lastname;`
   - [ ] `SELECT * FROM Employees GROUP BY Lastname;`

   **Answer:** The `ORDER BY` clause sorts the result set in ascending order by default, returning employees in alphabetical order by `Lastname`.

2. **Which of the following keyword should be used in order to set a filtering condition when using the `GROUP BY` clause?**
   - [x] `HAVING`
   - [ ] `WHERE`
   - [ ] `ORDER BY`
   - [ ] `SELECT`

   **Answer:** The `HAVING` clause is used to filter grouped results after the `GROUP BY` operation has been performed.

3. **You want to retrieve a list of authors from Australia, Canada, and India from the `Author` table. Which SQL statement is correct?**
   - [x] `SELECT * FROM Author WHERE Country IN ('Australia', 'Canada', 'India');`
   - [ ] `SELECT * FROM Author WHERE Country LIST ('CA', 'IN');`
   - [ ] `SELECT * FROM Author WHERE Country BETWEEN ('Australia', 'Canada', 'India');`
   - [ ] `SELECT * FROM Author IF Country ('Australia', 'Canada', 'India');`

   **Answer:** The `IN` operator allows you to specify multiple values in a `WHERE` clause, making it the correct choice for matching several countries.

4. **You want to retrieve a list of books priced in the range `$10` to `$25` from the `Book` table. What are the two ways you can specify the range?**
   - [ ] `SELECT Title, Price FROM Book WHERE Price 10 to 25;`
   - [x] `SELECT Title, Price FROM Book WHERE Price BETWEEN 10 AND 25;`
   - [x] `SELECT Title, Price FROM Book WHERE Price >= 10 AND Price <= 25;`
   - [ ] `SELECT Title, Price FROM Book WHERE Price IN (10, 25);`

   **Answer:** You can specify a range using either the `BETWEEN ... AND ...` operator or by combining the `>=` and `<=` comparison operators.

5. **You want to retrieve salary information for an employee called Ed from the `Employees` table. You write the following statement:**

   ```sql
   SELECT Firstname, Lastname, Salary
   FROM Employees;
   ```

   **You see all the employees listed, and it’s hard to find Ed’s information. Which clause should you add to reduce the number of rows returned?**
   - [x] `WHERE Firstname = 'Ed';`
   - [ ] `GROUP BY Firstname = 'Ed';`
   - [ ] `ORDER BY Firstname;`
   - [ ] `WHERE Employees = 'Ed';`

   **Answer:** The `WHERE` clause filters the rows returned by the query. In this case, `WHERE Firstname = 'Ed'` limits the results to employees whose first name is Ed.

## Module 3 - Functions, Multiple Tables, and Sub-queries

1. **Which of the following statements about built-in database functions is correct?**
   - [ ] Built-in database functions may increase processing time.
   - [ ] Built-in database functions may increase network bandwidth consumed.
   - [ ] Built-in database functions must be called from a programming language like Python.
   - [x] Built-in database functions reduce the amount of data that is retrieved.

   **Answer:** Built-in database functions execute within the database server, reducing the amount of data that needs to be transferred to the client and improving efficiency.

2. **Which of the following SQL queries would return the day of the week each dog was rescued?**
   - [ ] `SELECT RescueDate FROM PetRescue WHERE Animal = 'Dog';`
   - [x] `SELECT DAYOFWEEK(RescueDate) FROM PetRescue WHERE Animal = 'Dog';`
   - [ ] `SELECT DAYOFWEEK(RescueDate) FROM PetRescue;`
   - [ ] `SELECT DAY(RescueDate) FROM PetRescue WHERE Animal = 'Dog';`

   **Answer:** The `DAYOFWEEK()` function returns the day of the week for a given date, and the `WHERE` clause restricts the results to dogs only.

3. **What is the result of the following query?**

   ```sql
   SELECT (CURRENT_DATE - RescueDate)
   FROM PetRescue;
   ```

   - [ ] Returns today's date.
   - [ ] Returns the rescue date for each rescue.
   - [ ] Returns the current date and rescue date columns.
   - [x] Returns how long it has been since each rescue.

   **Answer:** Subtracting `RescueDate` from `CURRENT_DATE` returns the elapsed time (typically in days) since each animal was rescued.

4. **Which of the following queries will return the employees who earn less than the average salary?**
   - [ ] `SELECT AVG(Salary) FROM Employees WHERE Salary < AVG(Salary);`
   - [ ] `SELECT * FROM Employees WHERE Salary < (SELECT AVG(Salary));`
   - [x] `SELECT * FROM Employees WHERE Salary < (SELECT AVG(Salary) FROM Employees);`
   - [ ] `SELECT * FROM Employees WHERE Salary < AVG(Salary);`

   **Answer:** The average salary must be calculated in a subquery. The outer query then compares each employee's salary against that average.

5. **What are the three ways to work with multiple tables in the same query?**
   - [ ] Sub-queries, Implicit joins, normalization.
   - [x] Sub-queries, Implicit joins, `JOIN` operators.
   - [ ] Sub-queries, `APPEND`, `JOIN` operators.
   - [ ] Built-in functions, Implicit joins, `JOIN` operators.

   **Answer:** SQL supports retrieving data from multiple tables using **subqueries**, **implicit joins**, and explicit **JOIN operators** such as `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`.

## Module 4 - Accessing Databases using Python

1. **Which API do you use to connect to a database from Python?** — 1/1
   - [ ] REST API
   - [ ] Census API
   - [ ] Watson API
   - [x] DB API

   **Answer:** A DB API will enable you to connect to a database from Python to access and manipulate data.

2. **Which of the following functions would you use to query data from a table in SQLite using Python?** — 1/1
   - [ ] `sqlite.query()`
   - [ ] `sqlite.cursor()`
   - [x] `sqlite.cursor.execute()`
   - [ ] `sqlite.connect()`

   **Answer:** The function "sqlite.cursor.execute()" is used to execute SQL queries and statements in SQLite from Python.

3. **True or false: Resources used by the db API are released automatically when the program ends. There is no need to specifically close the connection.** — 1/1
   - [ ] True
   - [x] False

   **Answer:** It is important to use the close() method to close connections and avoid unused connections taking up resources.

4. **Which of the following is the correct order for accessing relational databases using Python?** — 1/1
   - [x] connect, create and execute SQL statements, close connection.
   - [ ] create statements, connect.
   - [ ] create and execute SQL statements, connect, close connection.
   - [ ] create, execute Python statements, connect, close connection.

   **Answer:** Correct.

5. **Line magics: start with a single % (percent) sign and apply to a particular line in a cell.**
   - [x] True.
   - [ ] False

   **Answer:** Correct.
