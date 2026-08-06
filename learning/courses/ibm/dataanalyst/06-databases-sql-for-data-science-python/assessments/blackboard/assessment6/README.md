# Assessment 6: Databases and SQL for Data Science with Python, with Goals

**Final Grade:** 500 / 500

---

## 1. Which SQL function is used to count the number of rows in a SQL query? — ✅ 10/10

- COUNT()
- NUMBER()
- SUM()
- **✅ Correct: COUNT(\*)**

---

## 2. Which SQL keyword is used to retrieve a maximum value? — ✅ 10/10

- MOST
- TOP
- **✅ Correct: MAX**
- UPPER

---

## 3. Which of the following SQL clauses is used to DELETE tuples from a database table? — ✅ 10/10

- **✅ Correct: DELETE**
- REMOVE
- DROP
- CLEAR

---

## 4. \***\*\_\_\_\*\*** removes all rows from a table without logging the individual row deletions. — ✅ 10/10

- DELETE
- REMOVE
- DROP
- **✅ Correct: TRUNCATE**

---

## 5. Which of the following is not a DDL command? — ✅ 10/10

- **✅ Correct: UPDATE**
- TRUNCATE
- ALTER
- none of the above

---

## 6. Which of the following are TCL commands? — ✅ 10/10

- UPDATE and TRUNCATE
- SELECT and INSERT
- GRANT and REVOKE
- **✅ Correct: ROLLBACK and SAVEPOINT**

---

## 7. If you don't specify ASC or DESC after a SQL ORDER BY clause, the following is used by default **\*\***\_\_**\*\*** — ✅ 10/10

- **✅ Correct: ASC**
- DESC
- There is no default
- None of the above

---

## 8. Which of the following statement is true? — ✅ 10/10

- **✅ Correct: DELETE does not free the space containing the table and TRUNCATE frees the space containing the table**
- Both DELETE and TRUNCATE free the space containing the table
- Both DELETE and TRUNCATE do not free the space containing the table
- DELETE frees the space containing the table and TRUNCATE does not free the space containing the table

---

## 9. What is the purpose of the SQL AS clause? — ✅ 10/10

- **✅ Correct: The AS SQL clause is used to change the name of a column in the result set or to assign a name to a derived column**
- The AS clause is used with the JOIN clause only
- The AS clause defines a search condition
- All of the mentioned

---

## 10. What does DML stand for? — ✅ 10/10

- Different Mode Level
- Data Model Language
- Data Mode Lane
- **✅ Correct: Data Manipulation Language**

---

## 11. With SQL, how can you return all the records from a table named "Persons" sorted descending by "FirstName"? — ✅ 10/10

- `SELECT * FROM Persons SORT BY 'FirstName' DESC`
- `SELECT * FROM Persons ORDER FirstName DESC`
- `SELECT * FROM Persons SORT 'FirstName' DESC`
- **✅ Correct: `SELECT * FROM Persons ORDER BY FirstName DESC`**

---

## 12. The UPDATE SQL clause can **\*\***\_**\*\*** — ✅ 10/10

- update only one row at a time
- **✅ Correct: update more than one row at a time**
- delete more than one row at a time
- delete only one row at a time

---

## 13. The UNION SQL clause can be used with **\*\***\_**\*\*** — ✅ 10/10

- **✅ Correct: SELECT Clause only**
- DELETE AND UPDATE clauses
- UPDATE clause only
- All of the above

---

## 14. Which SQL keyword is used to sort the result-set? — ✅ 10/10

- **✅ Correct: ORDER BY**
- SORT
- ORDER
- SORT BY

---

## 15. How can you change "Hansen" into "Nilsen" in the "LastName" column in the Persons table? — ✅ 10/10

- `UPDATE Persons SET LastName='Hansen' INTO LastName='Nilsen'`
- `MODIFY Persons SET LastName='Nilsen' WHERE LastName='Hansen'`
- `MODIFY Persons SET LastName='Hansen' INTO LastName='Nilsen'`
- **✅ Correct: `UPDATE Persons SET LastName='Nilsen' WHERE LastName='Hansen'`**

---

## 16. Which of the following commands makes the updates performed by the transaction permanent in the database? — ✅ 10/10

- ROLLBACK
- **✅ Correct: COMMIT**
- TRUNCATE
- DELETE

---

## 17. Find the name of those cities with temperature and condition whose condition is either sunny or cloudy but temperature must be greater than 70. — ✅ 10/10

- `SELECT city, temperature, condition FROM weather WHERE condition = 'sunny' AND condition = 'cloudy' OR temperature > 70`
- `SELECT city, temperature, condition FROM weather WHERE condition = 'sunny' OR condition = 'cloudy' OR temperature > 70`
- **✅ Correct: `SELECT city, temperature, condition FROM weather WHERE condition = 'sunny' OR condition = 'cloudy' AND temperature > 70`**
- `SELECT city, temperature, condition FROM weather WHERE condition = 'sunny' AND condition = 'cloudy' AND temperature > 70`

---

## 18. Find all the cities with temperature, condition and humidity whose humidity is in the range of 63 to 79. — ✅ 10/10

- `SELECT * FROM weather WHERE humidity IN (63 to 79)`
- `SELECT * FROM weather WHERE humidity NOT IN (63 AND 79)`
- **✅ Correct: `SELECT * FROM weather WHERE humidity BETWEEN 63 AND 79`**
- `SELECT * FROM weather WHERE humidity NOT BETWEEN 63 AND 79`

---

## 19. Which is a valid CREATE TABLE statement? — ✅ 10/10

- `Create table emp add(id integer(3));`
- `Create table emp (id integers(3));`
- `Create table emp modified (id integer(3));`
- **✅ Correct: `Create table emp (id integer(3));`**

---

## 20. How can you insert a new row into the "STORE" table? — ✅ 10/10

- `INSERT ROW (1,'RAM SINGH') INTO STORE;`
- `INSERT VALUES (1,'RAM SINGH') INTO STORE;`
- `INSERT INTO (1,'RAM SINGH') STORE;`
- **✅ Correct: `INSERT INTO STORE VALUES (1,'RAM SINGH');`**

---

## 21. Which statement is valid? — ✅ 10/10

- `ALTER TABLE EMPLOYEE MODIFY (last_name CHAR2(2000));`
- `ALTER TABLE EMPLOYEE CHANGE (last_name CHAR2(2000));`
- `ALTER TABLE EMPLOYEE CHANGE (last_name VARCHAR2(2000));`
- **✅ Correct: `ALTER TABLE EMPLOYEE MODIFY (last_name VARCHAR2(2000));`**

---

## 22. Which of the following commands should be used to create a database named "student"? — ✅ 10/10

- `CREATE ?I student`
- **✅ Correct: `CREATE DATABASE student`**
- `DATABASE /student`
- `DATABASE student`

---

## 23. A row of relation is generally referred to as ……….. and column of a relation is ………… — ✅ 10/10

- Domain & Attribute
- Attribute & Domain
- **✅ Correct: Tuple & Attribute**
- Attribute & Tuple

---

## 24. \***\*\_\*\*** is the attribute or group of attributes that uniquely identify occurrence of each entity. — ✅ 10/10

- Foreign key
- Super Key
- **✅ Correct: Primary Key**
- All of the above

---

## 25. A non-key attribute, whose values are derived from primary key of some other table. — ✅ 10/10

- Alternate key
- **✅ Correct: Foreign Key**
- Primary Key
- Super Key

---

## 26. What type of join is needed when you wish to include rows that do not have matching values? — ✅ 10/10

- Equi-join
- Natural join
- **✅ Correct: Outer join**
- All of the above

---

## 27. The following SQL command is which type of join? — ✅ 10/10

```sql
SELECT CUSTOMER_T.CUSTOMER_ID, ORDER_T.CUSTOMER_ID, NAME, ORDER_ID
FROM CUSTOMER_T, ORDER_T
WHERE CUSTOMER_T.CUSTOMER_ID = ORDER_T.CUSTOMER_ID
```

- **✅ Correct: Equi join**
- Natural join
- Outer join
- Cartesian Join

---

## 28. Which join refers to join records from the right table that have no matching key in the left table are included in the result set: — ✅ 10/10

- Left outer join
- **✅ Correct: Right outer join**
- Full outer join
- Half outer join

---

## 29. Which of the following conditions has to be satisfied for INNER JOIN to work? — ✅ 10/10

- Columns used for joining must have same name
- **✅ Correct: Columns used for joining can have same or different name**
- Columns used for joining must have different names
- None of the above

---

## 30. Which of the following statements is TRUE about FULL OUTER JOIN created on two tables Table1 and Table2? — ✅ 10/10

- Retrieves all the unmatched rows of Table1
- Retrieves all the unmatched rows of Table2
- **✅ Correct: Retrieves both matched and unmatched rows of Table1 and Table2**
- Retrieves only matched rows of Table1 and Table2

---

## 31. Which of the following statements are False? Choose all that apply — ✅ 10/10

- RIGHT OUTER JOIN is equivalent to LEFT OUTER JOIN if order of tables are reversed
- FULL OUTER JOIN is same as CROSS JOIN
- SELF JOIN is a special type of OUTER JOIN
- **✅ Correct: Both B and C**

---

## 32. True/False: You can drop the OUTER keyword and just say LEFT JOIN or RIGHT JOIN or FULL JOIN. — ✅ 10/10

- **✅ Correct: True**
- False

---

## 33. Below two tables (A & B) are given: — ✅ 10/10

```
A: 1, 2, 3, 4
B: 3, 4, 5, 6
```

**What will be the result of inner join between these tables?**

- A:1,B:3 / A:4,B:4
- A:3,B:1 / A:4,B:4
- A:2,B:3 / A:2,B:4
- **✅ Correct: A:3,B:3 / A:4,B:4**

---

## 34. `Select ID, GPA from student grades order by GPA ____________` — In order to give only 10 rank on the whole we should use. — ✅ 10/10

- **✅ Correct: Limit 10**
- Upto 10
- Only 10
- Max 10

---

## 35. Refer to the following table and answer the question: — ✅ 10/10

```
Name
Annie
Bob
Callie
Derek
```

**Which of these queries will display the table given above?**

- `Select employee from name`
- `Select name`
- **✅ Correct: `Select name from employee`**
- `Select employee`

---

## 36. In the SQL given below there is an error. Identify the error. — ✅ 10/10

```sql
SELECT * FROM employee WHERE dept_name="Comp Sci";
```

- Dept_name
- Employee
- **✅ Correct: "Comp Sci"**
- From

---

## 37. SQL view is said to be updatable (that is, inserts, updates or deletes can be applied on the view) if which of the following conditions are satisfied by the query defining the view? — ✅ 10/10

- The from clause has only one database relation
- The query does not have a group by or having clause
- The select clause contains only attribute names of the relation and does not have any expressions, aggregates, or distinct specification
- **✅ Correct: All of the above**

---

## 38. Consider the two relations instructor and department: — ✅ 10/10

**Instructor:**

| ID   | Name | Dept_name | Salary |
| ---- | ---- | --------- | ------ |
| 1001 | Ted  | Finance   | 10000  |
| 1002 | Bob  | Music     | 20000  |
| 1003 | Ron  | Physics   | 50000  |

**Department:**

| Dept_name | Building | Budget |
| --------- | -------- | ------ |
| Biology   | Watson   | 40000  |
| Chemistry | Painter  | 30000  |
| Music     | Taylor   | 50000  |

**Which of the following is used to create a view for these relations together?**

- **✅ Correct:**
  ```sql
  CREATE VIEW instructor_info AS
  SELECT ID, name, building
  FROM instructor, department
  WHERE instructor.dept_name = department.dept_name;
  ```
- ```sql
  CREATE VIEW instructor_info
  SELECT ID, name, building
  FROM instructor, department;
  ```
- ```sql
  CREATE VIEW instructor_info AS
  SELECT ID, name, building
  FROM instructor;
  ```
- ```sql
  CREATE VIEW instructor_info AS
  SELECT ID, name, building
  FROM department;
  ```

---

## 39. This query does which of the following operation? — ✅ 10/10

```sql
SELECT instructor.*
FROM instructor, teaches
WHERE instructor.ID = teaches.ID;
```

- All attributes of instructor and teaches are selected
- **✅ Correct: All attributes of instructor are selected on the given condition**
- All attributes of teaches are selected on given condition
- Only some attributes from instructor and teaches are selected

---

## 40. Aggregate functions can be used in the select list or the **\_\_** clause of a select statement or subquery. They cannot be used in a **\_\_** clause. — ✅ 10/10

- Where, having
- **✅ Correct: Having, where**
- Group by, having
- Group by, where

---

## 41. If we want to eliminate duplicates, we use the keyword **\_\_** in the aggregate expression. — ✅ 10/10

```sql
SELECT COUNT (____ ID)
FROM teaches
WHERE semester = 'Spring' AND YEAR = 2010;
```

- **✅ Correct: Distinct**
- Count
- Avg
- Primary key

---

## 42. What is the meaning of "GROUP BY" clause in SQL? — ✅ 10/10

- **✅ Correct: Group data by column values**
- Group data by row values
- Group data by column and row values
- None of the above

---

## 43. A \***\*\_\*\*** consists of a sequence of query and/or update statements. — ✅ 10/10

- **✅ Correct: Transaction**
- Commit
- Rollback
- Flashback

---

## 44. In order to maintain the consistency during transactions, database provides — ✅ 10/10

- Commit
- **✅ Correct: Atomic**
- Flashback
- Retain

---

## 45. In case of any shut down during transaction before commit which of the following statement is done automatically? — ✅ 10/10

- View
- Commit
- **✅ Correct: Rollback**
- Flashback

---

## 46. Point out the correct statement. — ✅ 10/10

- Stored procedures assist in achieving consistent implementation of logic across applications
- A stored procedure is a group of Transact-SQL statements compiled into a single execution plan
- Stored procedures can also improve performance
- **✅ Correct: All of the mentioned**

---

## 47. Point out the wrong statement. — ✅ 10/10

- Stored procedure can accept input and output parameters
- **✅ Correct: Stored procedure can return multiple values using input parameters**
- Using stored procedure, we can Select, Insert, Update, Delete data in database
- None of the above

---

## 48. Nesting level of a stored procedure's execution is stored in the \***\*\_\*\*** function. — ✅ 10/10

- @@NEST
- **✅ Correct: @@NESTLEVEL**
- @@LEVEL
- None of the above

---

## 49. Which of the following is a property of transactions? — ✅ 10/10

- Atomicity
- Concurrency
- Isolation
- **✅ Correct: All of the above**

---

## 50. Constraint checking can be disabled in existing **\*\***\_\_\_**\*\*** and **\*\***\_**\*\*** constraints so that any data you modify or add to the table is not checked against the constraint. — ✅ 10/10

- **✅ Correct: CHECK, FOREIGN KEY**
- DELETE, FOREIGN KEY
- CHECK, PRIMARY KEY
- PRIMARY KEY, FOREIGN KEY
