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

## Bonus Module 6 - Views, Stored Procedures, and Transactions

1. **Which of the following statements about SQL views is correct?**
   - [ ] You cannot change data in the base tables through a view.
   - [ ] A view is an independent copy of a single table's structure, including the data.
   - [ ] A view can only represent data from a single table.
   - [x] When you define a view, only the definition of the view is stored, not the data that it represents.

   **Answer:** A view stores only the SQL query (its definition). The underlying data remains in the base tables and is retrieved whenever the view is queried.

2. **Which SQL statement creates a view displaying job names and salary ranges for jobs where the salary range is between 50,000 and 100,000?**
   - [ ]
     ```sql
     CREATE VIEW
     AS
     SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY
     FROM JOBS
     WHERE MIN_SALARY > 50000
       AND MAX_SALARY < 100000;
     ```
   - [x]
     ```sql
     CREATE VIEW JobSalaryRanges(Job, StartingSalary, MaximumSalary)
     AS
     SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY
     FROM JOBS
     WHERE MIN_SALARY >= 50000
       AND MAX_SALARY <= 100000;
     ```
   - [ ]
     ```sql
     CREATE VIEW JobSalaryRanges(Job, StartingSalary, MaximumSalary)
     AS
     SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY
     FROM JOBS
     WHERE SALARY > 50000
       AND SALARY < 100000;
     ```
   - [ ]
     ```sql
     CREATE VIEW JobSalaryRanges(Job, StartingSalary, MaximumSalary)
     FROM JOBS
     WHERE MIN_SALARY > 50000
       AND MAX_SALARY < 100000;
     ```

   **Answer:** A valid `CREATE VIEW` statement requires the `AS SELECT` clause, and the `WHERE` clause correctly filters jobs whose minimum and maximum salaries fall within the specified range.

3. **Which of the following are benefits of stored procedures?**
   - [x] All are valid benefits.
   - [ ] Reduction in network traffic.
   - [ ] Reuse of code.
   - [ ] Improvement in performance.

   **Answer:** Stored procedures provide several advantages, including **code reuse**, **reduced network traffic**, and **improved performance**, making **"All are valid benefits"** the correct answer.

4. **Which of the following parameters can a stored procedure use?**
   - [x] Input and output parameters.
   - [ ] No parameters, as a stored procedure cannot accept parameters.
   - [ ] Input parameters.
   - [ ] Output parameters.

   **Answer:** Stored procedures can accept **input parameters**, return **output parameters**, or use both to pass values into and out of the procedure.

5. **What does ACID stand for?**
   - [ ] Asynchronous, Complete, Individual, Direct.
   - [x] Atomic, Consistent, Isolated, Durable.
   - [ ] Atomic, Consistent, Initiated, Duplicated.
   - [ ] Alternative, Creative, Isolated, Durable.

   **Answer:** ACID is a set of properties that ensure reliable database transactions:
   - **Atomicity** – A transaction is completed entirely or not at all.
   - **Consistency** – A transaction leaves the database in a valid state.
   - **Isolation** – Concurrent transactions do not interfere with one another.
   - **Durability** – Once committed, changes are permanent, even after a system failure.

## Bonus Module 6 - JOIN Statements

1. **You usually create a join between...?**
   - [ ] The foreign keys in each table.
   - [ ] Any column in either table.
   - [x] The primary key in one table and the foreign key in another table.
   - [ ] The primary keys in each table.

   **Answer:** Joins are typically created by matching a **primary key** in one table with a corresponding **foreign key** in another table.

2. **Which type of join returns all of the rows that an inner join returns and also all of the rows in the second table that do not have a match in the first table?**
   - [ ] Full outer join
   - [ ] Left outer join
   - [ ] Left inner join
   - [x] Right outer join

   **Answer:** A **RIGHT OUTER JOIN** returns all matching rows plus all rows from the right (second) table, even if they have no corresponding match in the left table.

3. **Which of the following statements correctly uses an `INNER JOIN`?**
   - [ ] `SELECT * FROM EMPLOYEES e INNER JOIN DEPARTMENTS d ON DEP_ID`
   - [ ] `SELECT * FROM EMPLOYEES INNER JOIN DEPARTMENTS ON DEP_ID = DEP_ID`
   - [ ] `CREATE INNER JOIN BETWEEN EMPLOYEES e AND DEPARTMENTS d ON e.DEP_ID = d.DEP_ID`
   - [x] `SELECT * FROM EMPLOYEES e INNER JOIN DEPARTMENTS d ON e.DEP_ID = d.DEP_ID`

   **Answer:** When the join columns have the same name in both tables, you should qualify them using the table name or alias to avoid ambiguity.

4. **Which of the following are the three valid types of outer join?**
   - [ ] Left outer join, right outer join, left/right outer join
   - [ ] Left outer join, right outer join, both outer join
   - [x] Left outer join, right outer join, full outer join
   - [ ] Left outer join, right outer join, total outer join

   **Answer:** SQL supports three types of outer joins: **LEFT OUTER JOIN**, **RIGHT OUTER JOIN**, and **FULL OUTER JOIN**.

5. **Which type of join would you use to select all the rows from both tables?**
   - [ ] Left outer join
   - [ ] Right outer join
   - [x] Full outer join
   - [ ] Total outer join

   **Answer:** A **FULL OUTER JOIN** returns every row from both tables, including matching rows and non-matching rows from each side.
