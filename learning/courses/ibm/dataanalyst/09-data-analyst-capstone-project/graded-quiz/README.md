# Graded Quiz - Questions and Answers

## Module 1 - Data Collection

1. **Which Python module helps you to easily access an API?**
   - [ ] Matplotlib
   - [x] Requests
   - [ ] NumPy
   - [ ] Pandas

   **Answer:** Requests is a Python library that allows you to access an API easily.

2. **Which of the following URL formats would you use to retrieve the JSON representation of a job listing?**
   - [ ] /positions.csv
   - [ ] /positions.html
   - [x] /positions.json
   - [ ] /positions.xml

   **Answer:** The correct URL format to retrieve the JSON representation of a job listing is "/positions.json." This endpoint provides the job details in JSON format.

3. **What step should you take after downloading the Jobs_API file to run it in the lab?**
   - [ ] Convert the file to a CSV
   - [x] Upload the file to the lab
   - [ ] Compile the file
   - [ ] Open the file in a text editor

   **Answer:** After downloading the Jobs_API file, you should upload it to the lab to execute the code.

4. **You are building a web scraping tool in Python and need to retrieve data from a web page. Which module will you use to download a web page in Python?**
   - [ ] urllib
   - [ ] bs4
   - [x] requests
   - [ ] json

   **Answer:** The requests module downloads webpages in Python.

5. **Which function in the csv module allows you to write rows into a CSV file?**
   - [ ] writecsv
   - [x] writerow
   - [ ] writeline
   - [ ] write

   **Answer:** `writerow` allows you to write rows into a CSV file.

6. **You are designing a web page that includes a complex table layout. Which tag will you use to identify a table row in an HTML table?**
   - [ ] `<row>`
   - [x] `<tr>`
   - [ ] `<table>`
   - [ ] `<td>`

   **Answer:** You can use the `<tr>` tag to identify a table row in an HTML table.

7. **Which library is required to load and manipulate the dataset in this lab?**
   - [ ] 'matplotlib'
   - [ ] 'seaborn'
   - [x] 'pandas'
   - [ ] numpy

   **Answer:** Pandas helps to load and manipulate data in this lab.

8. **After loading the dataset, how many rows are present in the dataset?**
   - [ ] 115
   - [ ] 54,728
   - [x] 65,457
   - [ ] 12,345

   **Answer:** The dataset contains 65,457 rows, as shown in the output of `df.shape[0]`.

9. **What is the approximate mean age of the survey participants in this dataset?**
   - [ ] 25.4
   - [ ] 29.6
   - [ ] 39.5
   - [x] 32.6

   **Answer:** The mean age is approximately 32.6 years, as calculated after mapping age ranges to numeric values.

10. **How many unique countries are represented in the 'Country' column of this dataset?**
    - [x] 185
    - [ ] 120
    - [ ] 200
    - [ ] 175

    **Answer:** 185 unique countries are represented in the 'Country' column of this dataset.

## Module 2 - Data Wrangling

1. **What code would you use to identify the number of duplicate rows in a DataFrame named df?**
   - [ ] `df.find_duplicates()`
   - [ ] `df.sum_duplicates()`
   - [x] `df.duplicated().sum()`
   - [ ] `df.duplicates().sum()`

   **Answer:** `df.duplicated().sum()` is the appropriate method to identify the number of duplicate rows in a DataFrame named df.

2. **What is the primary goal of identifying duplicate rows in a dataset during data cleaning?**
   - [x] To ensure data accuracy and reliability
   - [ ] To improve visualization aesthetics
   - [ ] To increase the size of the dataset
   - [ ] To convert categorical data into numerical values

   **Answer:** Identifying and removing duplicates helps ensure that analyses are accurate and not biased by repeated records representing the same observation.

3. **Which code would you use to identify the columns in a DataFrame named df that have the same values in duplicate rows?**
   - [x] `df.loc[df.duplicated(keep=False)].nunique(axis=0)`
   - [ ] `df[df.duplicated()].nunique(axis=1)`
   - [ ] `df.loc[df.duplicated(keep=False)].nunique()`
   - [ ] `df.loc[df.duplicated(keep='first')].unique()`

   **Answer:** This is the correct way to determine which columns have unique values across duplicate rows by calculating the count of unique values column-wise.

4. **After identifying duplicates, which statement accurately verifies if they were successfully removed?**
   - [ ] Checking if `df.drop_duplicates()` returns zero
   - [ ] Counting rows before and after `df.dropna()`
   - [ ] Checking if `df.isnull().sum()` returns zero
   - [x] Re-running `df.duplicated().sum()` and ensuring it equals zero

   **Answer:** Re-running `df.duplicated().sum()` and ensuring it equals zero rechecks the DataFrame for duplicates, confirming their removal.

5. **Which of the following is the most appropriate method to replace missing values in a column with the column's most frequent value?**
   - [ ] `df['column'].fillna(df['column'].mean())`
   - [x] `df['column'].fillna(df['column'].mode()[0])`
   - [ ] `df['column'].fillna(0)`
   - [ ] `df['column'].replace(0)`

   **Answer:** `df['column'].fillna(df['column'].mode()[0])` fills with the most frequent value.

6. **What is the purpose of using `df.describe(include='all')` on a DataFrame?**
   - [ ] Identify missing values in all columns
   - [x] Display summary statistics for all columns, including categorical data
   - [ ] Calculate the total number of missing values
   - [ ] Remove duplicate values from the DataFrame

   **Answer:** `df.describe(include='all')` on a DataFrame displays summary statistics for all columns, including categorical data.

7. **What is the most appropriate method to fill missing values with the most frequent value in a specific column?**
   - [ ] Independent contractor, freelancer, or self-employed
   - [ ] `df.fillna(df.mode())`
   - [x] `df['column'].fillna(df['column'].mode()[0])`
   - [ ] `df.mode().fillna()`

   **Answer:** Using `df['column'].fillna(df['column'].mode()[0])` replaces missing values with the column's most frequent value.

8. **Which command should you use to replace all NaN values in the column 'RemoteWork' with a specific value?**
   - [ ] `df['RemoteWork'].fillna(df.mean()`
   - [ ] `df['RemoteWork'].dropna()`
   - [x] `df['RemoteWork'].fillna('value', inplace=True)`
   - [ ] `df['RemoteWork'].replace()`

   **Answer:**
