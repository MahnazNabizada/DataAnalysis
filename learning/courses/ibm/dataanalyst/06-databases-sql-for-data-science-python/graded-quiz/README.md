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
