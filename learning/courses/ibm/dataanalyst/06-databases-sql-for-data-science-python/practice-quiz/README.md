# Practice Quiz - Questions and Answers

## Module 1 - Basic SQL

## SQL Databases Quiz

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
