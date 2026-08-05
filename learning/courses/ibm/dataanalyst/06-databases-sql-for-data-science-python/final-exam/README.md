# Final Exam

1. **The `SELECT` statement is called a query, and the output produced by executing the query is called what?**
   - [ ] The database
   - [ ] The table
   - [ ] The index
   - [x] A result set

   **Answer:** A `SELECT` statement retrieves data from a database, and the returned data is known as a **result set**.

2. **Which of the following SQL statements will delete the customers whose `Country` is Italy?**
   - [ ] `DELETE FROM CUSTOMERS WHERE COUNTRY IS 'ITALY';`
   - [x] `DELETE FROM CUSTOMERS WHERE COUNTRY = 'ITALY';`
   - [ ] `DELETE COUNTRY 'ITALY' FROM CUSTOMERS;`
   - [ ] `DELETE 'ITALY' FROM CUSTOMERS;`

   **Answer:** The `DELETE` statement removes rows from a table, while the `WHERE` clause specifies which rows should be deleted.

3. **What does the primary key of a relational table do?**
   - [ ] Uniquely identifies each relation in a table.
   - [ ] Uniquely identifies each column in a table.
   - [x] Uniquely identifies each row in a table.
   - [ ] Uniquely identifies each attribute in a table.

   **Answer:** A **primary key** uniquely identifies every row in a table and ensures that no duplicate or null values exist in the key column(s).

4. **What are the basic categories of SQL commands based on functionality?**
   - [ ] Data Manipulation Language (DML)
   - [ ] Data Definition Language (DDL)
   - [x] Both of the above
   - [ ] None of the above

   **Answer:** SQL commands are broadly categorized into **Data Definition Language (DDL)** for defining database structures and **Data Manipulation Language (DML)** for working with data.

5. **When querying a table called `Teachers` that contains a list of teachers and the city they teach in, which query returns the number of teachers from each city?**
   - [ ] `SELECT DISTINCT(City) FROM Teachers;`
   - [ ] `SELECT City, COUNT(City) FROM Teachers;`
   - [ ] `SELECT City, DISTINCT(City) FROM Teachers GROUP BY City;`
   - [x] `SELECT City, COUNT(City) FROM Teachers GROUP BY City;`

   **Answer:** `GROUP BY City` groups the rows by city, and `COUNT(City)` counts the number of teachers in each group.

6. **You want to retrieve a list of employees with first and last names who are between the ages of 30 and 50. Which clause would you add to the following statement?**

   ```sql
   SELECT First_Name, Last_Name, Age
   FROM Company;
   ```

   - [ ] `WHERE Age < 30`
   - [ ] `IF Age >= 30 AND Age <= 50`
   - [x] `WHERE Age >= 30 AND Age <= 50`
   - [ ] `WHERE Age > 30`

   **Answer:** The `WHERE` clause filters the rows returned, limiting the results to employees between the ages of 30 and 50.

7. **Which of the following queries retrieves the lowest value of `PRICE` from a table called `PRODUCTS`?**
   - [ ] `SELECT LOWEST(PRICE) FROM PRODUCTS;`
   - [ ] `SELECT LEAST(PRICE) FROM PRODUCTS;`
   - [ ] `SELECT MAX(PRICE) FROM PRODUCTS;`
   - [x] `SELECT MIN(PRICE) FROM PRODUCTS;`

   **Answer:** The `MIN()` aggregate function returns the smallest value in the specified column.

8. **Which of the following queries retrieves the product name that has the lowest price?**
   - [ ] `SELECT PRODUCT_NAME FROM PRODUCTS WHERE UNIT_PRICE = MIN;`
   - [x] `SELECT PRODUCT_NAME FROM PRODUCTS WHERE UNIT_PRICE = (SELECT MIN(UNIT_PRICE) FROM PRODUCTS);`
   - [ ] `SELECT MIN(UNIT_PRICE) FROM PRODUCTS;`
   - [ ] `SELECT PRODUCT_NAME FROM PRODUCTS WHERE UNIT_PRICE IS LOWEST;`

   **Answer:** The subquery calculates the minimum unit price, and the outer query returns the product name whose price matches that minimum value.

9. **Which of the following statements is correct?**
   - [ ] A database connection is a control structure that enables traversal over the records in a database.
   - [ ] A database cursor is a control structure that enables traversal over the records in a DataFrame.
   - [ ] A database cursor is a control structure that restricts traversal over the records in a database.
   - [x] A database cursor is a control structure that enables traversal over the records in a database.

   **Answer:** A **database cursor** is a control structure that allows a program to traverse and process records returned by a database query.

10. **Which of the following Python statements saves the contents of a DataFrame `df` as a table named `Sample` in an SQL database?**

- [ ] `df.read_sql('Sample', connection_object)`
- [x] `df.to_sql('Sample', connection_object)`
- [ ] `df.read_sql('Sample')`
- [ ] `df.to_sql('Sample')`

**Answer:** The `to_sql()` method writes the contents of a pandas DataFrame to an SQL database table using the specified database connection.
