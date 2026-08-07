# Graded Quiz - Questions and Answers

## Module 1 - Importing Data Sets

1. **What Python library is primarily used for machine learning?**
   - [ ] NumPy
   - [ ] pandas
   - [x] scikit-learn
   - [ ] matplotlib

   **Answer:** Scikit-learn is specifically designed for data mining and data analysis. It features various classification, regression, and clustering algorithms, including support vector machines and random forests, which are the core of machine learning.

2. **You have `headers_list: headers_list=['A','B','C']` and the DataFrame df that contains three columns. What syntax should you use to replace the headers of the DataFrame df with values in the list headers_list?**
   - [x] `df.columns = headers_list`
   - [ ] `df.head(headers_list)`
   - [ ] `df.tail() = headers_list`
   - [ ] `df.tail(headers_list)`

   **Answer:** In Pandas, the `.columns` attribute allows for direct assignment. By setting it equal to a list of strings, the DataFrame immediately updates its internal index of column names with the new labels provided in the list.

3. **What task does the following command perform?**

   ```python
   df = pandas.read_csv("A.csv")
   ```

   - [ ] Changes the name of the column in df to the ones as in "A.csv"
   - [x] Loads the data from a CSV file called "A.csv" into a DataFrame df.
   - [ ] Saves the data frame df to a CSV file called "A.csv"
   - [ ] Displays the contents of the CSV file

     **Answer:** The read_csv function opens the specified file and translates the comma-separated text into a structured tabular format in Python, allowing for immediate analysis and manipulation.

4. **You are analyzing a used car dataset in Pandas. The column "cylinders" contains numeric values like 4, 6, and 8 to represent engine configuration. What data type is most appropriate for this column?**
   - [ ] float64
   - [ ] string
   - [ ] object
   - [x] int64

   **Answer:** int64 data types are used to store a numeric format.

5. **Zoya wants to view summary statistics—including non-numeric columns—for her DataFrame df. Which command should she use?**
   - [ ] `df.info()`
   - [x] `df.describe(include="all")`
   - [ ] `df.statistics(include="all")`
   - [ ] `df.describe()`

   **Answer:** The `include="all"` parameter forces Pandas to include all columns in the summary. For non-numeric columns, it provides additional metrics such as the number of unique values, the most frequent value ("top"), and its frequency.

6. **You're preparing to analyze a car dataset. The column 'symboling' has values ranging from -3 to +3 and is meant to reflect insurance risk. What does this suggest about the variable?**
   - [x] It's a numeric variable used to quantify risk.
   - [ ] It's the target variable for prediction categories.
   - [ ] It's a string column describing insurance categories.
   - [ ] It's a missing column from the dataset.

   **Answer:** Because the variable uses a scale of numbers to represent a concept (risk), it is a numeric variable. This allows analysts to calculate averages and perform mathematical modeling to predict insurance outcomes.

7. **Which of the following describes the purpose of a cursor object when using Python to connect to a database?**
   - [ ] To close a database connection from the internet.
   - [ ] To read and write CSV files to download the database.
   - [x] To execute SQL queries and retrieve results from the database.
   - [ ] To connect to the internet and download data.

   **Answer:** Think of the cursor as the "active agent" of the connection. While the connection keeps the door open, the cursor is what actually walks into the database, runs the command, and brings back the data.

8. **You're tasked with visualizing trends in used car prices over time. Which Python library would be the best choice for this task?**
   - [x] Matplotlib
   - [ ] NumPy
   - [ ] Scikit-learn
   - [ ] Pandas

   **Answer:** Matplotlib is the foundation of data visualization in Python. It is the most versatile tool for creating line charts, bar graphs, and scatter plots, making it ideal for showing how prices trend over a period.

9. **You opened a CSV file where column names are missing, and integers are used as headers. How would you accurately assign correct headers to the DataFrame?**
   - [ ] Use `headers_list = df.columns`
   - [ ] Use `df.add_header(headers_list)`
   - [ ] Use `df.header = headers_list`
   - [x] `df.columns = headers_list`

   **Answer:** This is the standard assignment method. By setting the `.columns` attribute equal to a new list of names, you overwrite the default integers (0, 1, 2...) with meaningful descriptions.

10. **Jack wants to query a database using Python. Which step must come first after importing the sqlite3 module?**
    - [ ] Apply `fetchall()` to query results
    - [ ] Define `cursor()` directly
    - [x] Use `connect()` to establish connection
    - [ ] Run SQL using `execute()` directly

    **Answer:** Establishing a connection is the mandatory first step. It tells Python which database file to interact with and prepares the environment for SQL commands.
