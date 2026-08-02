# Practice Quiz - Questions and Answers

## Module 1 - Basic SQL

1. **Which of the following statements about databases is accurate? Select all that apply.** — 1/1
   - [x] Databases can store data and allow queries on that data.
   - [x] Various types of databases exist, such as relational, hierarchical, and NoSQL.
   - [x] A database serves as a data repository.
   - [ ] All databases store data only in fixed tables of rows and columns.

   **Answer:** A key capability of databases is retrieving, filtering, and analyzing stored data through queries. Databases are implemented using different models, each suited to different data structures and use cases. Databases are designed to store and organize data so it can be managed and used.

2. **Which SQL statement is primarily used to retrieve data from a table?** — 1/1
   - [ ] DELETE
   - [ ] INSERT
   - [x] SELECT
   - [ ] UPDATE

   **Answer:** The SELECT statement is used to retrieve data from one or more tables.

3. **In a Film database with a FilmLocations table, you wish to retrieve a list of films from 2019. However, the query you ran displayed all the films. The query in question is:** `SELECT Title, ReleaseYear, Locations FROM FilmLocations`. **What element is absent from the query?** — 1/1
   - [x] A WHERE clause that limits the results to films from 2019.
   - [ ] A DISTINCT clause to ensure a specific year's uniqueness.
   - [ ] The query is already correct.
   - [ ] A LIMIT clause to restrict the output to films from 2019.

   **Answer:** To isolate films from 2019, the query must include a WHERE clause such as `WHERE ReleaseYear=2019`.

4. **Which of these statements correctly introduces a new entry to the 'Instructor' table?** — 1/1
   - [ ] `UPDATE Instructor(...) WITH VALUES(...)`
   - [ ] `ADD INTO Instructor(...) VALUES(...)`
   - [ ] `SELECT Instructor(...) FROM VALUES(...)`
   - [x] `INSERT INTO Instructor(ins_id, lastname, firstname, city, country) VALUES(4, 'Doe', 'John', 'Sydney', 'AU')`

   **Answer:** The INSERT INTO statement is designed to append new rows to tables.

5. **In an UPDATE statement, what purpose does the WHERE clause serve?** — 1/1
   - [ ] The UPDATE statement never incorporates a WHERE clause.
   - [ ] The WHERE clause designates a new table to accept the updates.
   - [ ] It dictates which column/data gets updated.
   - [x] It defines which specific rows should be updated.

   **Answer:** The WHERE clause filters the result set. Omitting it would mean updating every row in the table.

## Module 2 - Introduction to Relational Databases and Tables

1. **What is the function of a primary key?** — 1/1
   - [x] The primary key uniquely identifies each row in a table.
   - [ ] The primary key is used to identify any rows in the table that contain NULL values.
   - [ ] The primary key is used to grant access to a table.
   - [ ] The primary key enables you to add data to columns.

   **Answer:** The primary key uniquely identifies each row in a table.

2. **True or False: Data Manipulation Language statements like INSERT, SELECT, UPDATE, and DELETE are used to read and modify data.** — 1/1
   - [x] True
   - [ ] False

   **Answer:** Data Manipulation Language statements like INSERT, SELECT, UPDATE, and DELETE are used to read and modify data.

3. **Data Definition Language (or DDL) statements are used to define, change, or delete database objects such as tables. Which of the following statements are all DDL statements?** — 1/1
   - [ ] SELECT and DELETE
   - [ ] INSERT and UPDATE
   - [x] CREATE, ALTER, DROP
   - [ ] SELECT, INSERT, UPDATE

   **Answer:** The CREATE, ALTER, and DROP statements act on objects such as tables, not the data within the table.

4. **Which of the following queries will change the data type of an existing column (phone) to the varchar data type?** — 1/1
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
