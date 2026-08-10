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

## Module 2 - Data Wrangling

1. **Which method replaces a missing value in a column with continuous numeric data most appropriately?**
   - [x] Use the average of the other values in the column
   - [ ] Apply the mean square error of the other data in the column
   - [ ] Use an educated guess to replace values in the column
   - [ ] Use the difference between the minimum and maximum values

   **Answer:** The average is often a good choice to fill in a missing value for an attribute with continuous values.

2. **You need to decide on bin values while preprocessing continuous data. What should you do first?**
   - [ ] Use the interquartile range value
   - [ ] Convert object data types
   - [ ] Divide the average by the standard deviation
   - [x] Visualize the distribution of histogram

   **Answer:** Creating a histogram of values can help you decide how to group your data.

3. **You need to check and convert column names and units in a dataset using methods like rename() and astype(). What Pandas structure allows you to perform these operations across multiple features at once?**
   - [x] DataFrame
   - [ ] float
   - [ ] int
   - [ ] object

   **Answer:** A DataFrame is the core structure in Pandas that allows you to manipulate entire datasets, including renaming columns, converting data types, and performing unit conversions.

4. **Meera is scaling her dataset before feeding it into a model. She wants all features to be on a similar range. What is the purpose of this process?**
   - [ ] Eliminate data outliers and incorrect values
   - [ ] Remove missing entries from the dataset
   - [x] Scale features to similar value ranges
   - [ ] Set all features equal in values

   **Answer:** Normalization scales features to a similar range, ensuring fair comparisons and balanced model influence.

5. **Which function transforms categorical values into numerical columns suitable for analysis?**
   - [x] Encode categories as numbers
   - [ ] Transform column data types
   - [ ] Converts numerical into labels
   - [ ] Assign values to fixed bins

   **Answer:** It creates a separate column with names as the variable's categorical value entries and assigns numerical values to each column based on the value of the actual attribute.

6. **Which of the following is the correct sequence of steps in a typical data pre-processing pipeline?**
   - [ ] Encoding → Visualization → Modeling → Cleaning
   - [ ] Data import → Modeling → Normalization → Visualization
   - [ ] Modeling → Normalization → Cleaning → Encoding
   - [x] Cleaning → Formatting → Normalization → Encoding

   **Answer:** The standard flow is to clean data, standardize formats, normalize values, and encode categorical variables.

7. **Ahmed wants to prepare the "fuel type" column with values like "gas" and "diesel" for model training. What should he use?**
   - [x] `get_dummies()`
   - [ ] `dropna()`
   - [ ] `astype()`
   - [ ] `cut()`

   **Answer:** The `get_dummies()` method transforms each category into its own column.

8. **In a customer survey dataset, you found that the value "N/A" is used inconsistently to represent missing data, and you want to convert all "N/A" entries to actual NaN values for proper handling. Which Pandas function should you use in this scenario?**
   - [ ] `dropna()`
   - [ ] `astype()`
   - [x] `replace()`
   - [ ] `fillna()`

   **Answer:** To replace missing values like NaNs with actual values, the Pandas library has a built-in method called `replace()`, which can be used to fill in the missing values with the newly calculated values.

## Module 3 - Exploratory Data Analysis

1. **While exploring a dataset with Pandas, Elina wants to view summary statistics such as count, mean, and standard deviation. What should she use?** — 1/1
   - [ ] `summary()`
   - [x] `describe()`
   - [ ] `head()`
   - [ ] `tail()`

   **Answer:** The method described provides summary statistics.

2. **What does a Pearson Correlation value near zero most likely indicate about two variables?** — 1/1
   - [x] The variables are likely not correlated.
   - [ ] The values of one variable deviate very little from the mean.
   - [ ] The meaning of both variables is near zero.
   - [ ] The correlation between variables is inconclusive.

   **Answer:** The Pearson Correlation indicates the strength of the correlation between two variables.

3. **You want to reshape grouped data so that one variable appears in rows and another in columns. Which Pandas method helps restructure this data into a more readable tabular format?** — 1/1
   - [ ] `merge()`
   - [x] `pivot()`
   - [ ] `pcolor()`
   - [ ] `groupby()`

   **Answer:** The `pivot()` method rearranges data, so one variable becomes columns and another becomes rows, making the table easier to interpret.

4. **Sara filters a dataset to include just the 'body-style' and 'price' columns. She then uses groupby with mean() to analyze it. What does this operation calculate?** — 1/1
   - [x] It calculates the average price for each body style.
   - [ ] It calculates the average price for all vehicles.
   - [ ] It calculates the average body-style categories.
   - [ ] It writes the mean price for each body style to the data frame.

   **Answer:** The `groupby.mean()` method finds the means of different groups of values.

5. **You have analyzed that as highway miles per gallon (MPG) increase, the car price tends to decrease on a scatter plot with a regression line. What type of correlation exists between highway MPG and price?**
   - [ ] No correlation
   - [ ] Cyclical correlation
   - [x] Negative correlation
   - [ ] Positive correlation

   **Answer:** When the slope of the line is steep, it means that highway miles per gallon is still a good predictor of price. These two variables are said to have a negative correlation.

## Module 4 - Model Development

1. **Thomas came across the code `LinearRegression()`, while building a machine learning pipeline. Which of the following is correct about this code line?** — 1/1
   - [x] Initializes and stores regression model in the lm variable
   - [ ] Predicts outcomes using the lm model
   - [ ] Evaluates the performance of the lm model
   - [ ] Fits training data to the lm object

   **Answer:** The code uses the constructor to initialize a linear regression model and assigns it to the lm variable.

2. **A data analyst is evaluating the performance of a linear regression model using a residual plot. What pattern indicates that the model fits the data well?** — 1/1
   - [ ] Residuals align directly with the fitted regression line.
   - [ ] Residuals form a clear upward-sloping pattern.
   - [ ] Residuals increase steadily as predictor values increase.
   - [x] Residuals are randomly scattered around the zero line.

   **Answer:** Randomly scattered residuals around the zero line indicate that the model captures the data's trend without systematic bias. Patterns or trends in the residuals suggest model misfit or violations of regression assumptions.

3. **What is the order of a polynomial created with this code?**

   ```python
      Pr = PolynomialFeatures(degree=2)
   ```

   - [x] A polynomial of degree 2
   - [ ] A maximum of 2
   - [ ] A minimum of 2
   - [ ] Between 0 and 2, inclusive

   **Answer:** You can use the code `PolynomialFeatures(degree=2)` to create a 2nd-order polynomial.

4. **An engineer is plotting a regression and mean lines for their model and sees that the blue regression mean square error (MSE) area is much smaller than the red mean line MSE area. What can be inferred about the regression model's fit?** — 1/1
   - [ ] It adds variations to predictions.
   - [ ] It copies the mean of the data.
   - [ ] It performs poorly overall.
   - [x] It captures data trends well.

   **Answer:** Smaller blue squares (regression MSE) compared to the red ones (mean MSE) suggest that the model explains the data better than using just the mean.

5. **Romy is predicting car prices using a model, showing a value of $13,771.30 for a car with 30 highway miles per gallon (MPG). What should he do next to ensure that the results make sense?**
   - [x] Analyze values to validate their range
   - [ ] Compare values using a residual plot
   - [ ] Plot results using a regression graph
   - [ ] Fit the model again using the same data

   **Answer:** Before trusting predictions from the model, you should validate that the output is realistic and within expected bounds. This helps validate the model's usefulness.
