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

   **Answer:** Using `df['RemoteWork'].fillna('value', inplace=True)` replaces missing values with a specific value

## Module 3 - Exploratory Data Analysis

## Data Analysis, Correlation, and Outlier Detection Quiz

1. **Which function helps identify missing values in each column of a DataFrame?**
   - [ ] `df.describe()`
   - [x] `df.isnull().sum()`
   - [ ] `df.info()`
   - [ ] `df.missing_values()`

   **Answer:** `df.isnull().sum()` identifies missing values in each column.

2. **Which of the following commands is used to visualize the distribution of a categorical variable?**
   - [ ] `sns.lineplot(data=df, x='column')`
   - [ ] `sns.scatterplot(data=df, x='column')`
   - [ ] `sns.histplot(data=df, x='column')`
   - [x] `sns.countplot(data=df, x='column')`

   **Answer:** `sns.countplot()` is effective for visualizing categorical data distributions.

3. **Which pandas function can you use to compute cross-tabulations?**
   - [x] `pd.crosstab()`
   - [ ] `pd.correlation()`
   - [ ] `pd.merge()`
   - [ ] `pd.groupby()`

   **Answer:** `pd.crosstab()` computes cross-tabulations between two variables.

4. **What is the median ConvertedCompYearly of respondents in the dataset?**
   - [x] 65,000
   - [ ] 55,000
   - [ ] 50,000
   - [ ] 60,000

   **Answer:** The median ConvertedCompYearly is 65,000, providing insight into typical yearly compensation.

5. **Which method is used to detect outliers by calculating the range between the 25th and 75th percentiles?**
   - [ ] Standard deviation
   - [ ] Mean absolute deviation
   - [x] Interquartile Range (IQR)
   - [ ] Z-score

   **Answer:** The IQR method is commonly used to detect outliers by analyzing the spread of the middle 50% of data.

6. **Which pandas function can you use to calculate the skewness of a data column?**
   - [x] `df.skew()`
   - [ ] `df.corr()`
   - [ ] `df.describe()`
   - [ ] `df.var()`

   **Answer:** The `skew()` function in pandas is used to calculate the skewness of a column.

7. **What is the best practice for handling extreme outliers in a dataset when analyzing average compensation?**
   - [x] Remove the outliers to prevent skewing the analysis
   - [ ] Replace outliers with NaN
   - [ ] Ignore the outliers as they are part of the data
   - [ ] Set outliers to the maximum value within 1.5 IQR

   **Answer:** Removing extreme outliers helps in obtaining a more accurate measure of central tendency, like the median.

8. **How would you identify the median ConvertedCompYearly for full-time employees in the dataset?**
   - [ ] By calculating the mode of ConvertedCompYearly
   - [ ] By removing all outliers first
   - [x] By filtering the dataset for full-time employees and calculating the median
   - [ ] By calculating the mean of all ConvertedCompYearly values

   **Answer:** Filtering for full-time employees first ensures accurate median calculation.

9. **What does the correlation between Age and WorkExp indicate?**
   - [ ] As age increases, work experience decreases.
   - [ ] Work experience is unrelated to the dataset.
   - [ ] Age has no impact on work experience in the dataset.
   - [x] There is a strong relationship between Age and Work Experience, but it is not perfect.

   **Answer:** The correlation of 0.85 indicates that Work Experience strongly correlates with Age, but other factors might also contribute.

10. **What is the purpose of removing outliers from the ConvertedCompYearly column before analyzing salary trends?**
    - [ ] Ensure all data points are unique
    - [ ] Increase the median salary
    - [ ] Decrease the dataset size
    - [x] Focus on more common salary values and reduce skewness

    **Answer:** Removing outliers provides a clearer view of common salary trends by reducing skewness.

# Module 4 - Data Visualization

1. **Which visualization method is most suitable for displaying the distribution of YearsCodePro among respondents?**
   - [ ] Pie chart
   - [x] Histogram
   - [ ] Line chart
   - [ ] Bubble plot

   **Answer:** A histogram is appropriate as it effectively shows the spread of continuous data like YearsCodePro.

2. **Which of the following variables is most appropriate for examining the distribution of work arrangement preferences?**
   - [ ] The end of the whisker
   - [ ] CompTotal
   - [ ] The upper boundary of the box
   - [x] RemoteWork

   **Answer:** RemoteWork indicates work arrangement preferences, suitable for distribution analysis.

3. **Which of the following visualizations is ideal for analyzing the composition of desired databases among respondents?**
   - [ ] Box plot
   - [ ] Line chart
   - [ ] Bubble plot
   - [x] Histogram

   **Answer:** Histogram is ideal for analyzing the composition of desired databases among respondents.

4. **Which column combination is most suitable for creating a bubble plot to analyze job satisfaction and compensation, with age as the bubble size?**
   - [ ] ConvertedCompYearly and DatabaseWantToWorkWith
   - [x] ConvertedCompYearly and JobSatPoints_6
   - [ ] Age and ConvertedCompYearly
   - [ ] JobSatPoints_6 and MainBranch

   **Answer:** The combination of ConvertedCompYearly and JobSatPoints_6, with age as the bubble size, allows for analyzing job satisfaction relative to compensation.

5. **Why is it essential to understand data relationships before choosing variables for scatterplots?**
   - [ ] To ensure visualization is aesthetically pleasing
   - [x] To choose variables that show meaningful correlations
   - [ ] To convert all data into numeric format
   - [ ] To use data for decorative purposes

   **Answer:** Selecting variables with meaningful relationships allows scatterplots to reveal insightful correlations.

6. **For visualizing the top 5 programming languages respondents have experience with, which column is most suitable?**
   - [ ] MainBranch
   - [x] LanguageHaveWorkedWith
   - [ ] DatabaseWantToWorkWith
   - [ ] LanguageAdmired

   **Answer:** 'LanguageHaveWorkedWith' contains the programming languages respondents have experience with.

7. **In the lab, how do you create a stacked chart comparing median job satisfaction for 'JobSatPoints_6' and 'JobSatPoints_7' across different employment statuses?**
   - [ ] Use a scatter plot with `Employment` as one axis
   - [ ] Use `.hist()` for histogram plotting
   - [x] Use `.groupby()` on `Employment` and plot with `kind='bar', stacked=True`
   - [ ] Use `plt.plot()` for a line chart

   **Answer:** Grouping by 'Employment' and plotting with `stacked=True` shows median values across categories.

8. **Which type of data is most suitable for visualization with a line chart?**
   - [x] Continuous data over time
   - [ ] Categorical data
   - [ ] Nominal data
   - [ ] Ordinal data without a specific order

   **Answer:** Line charts are excellent for visualizing continuous data over time.

9. **Where should the age groups typically be placed in a line chart showing median compensation by age group?**
   - [x] On the X-axis
   - [ ] On the Y-axis
   - [ ] In the legend
   - [ ] In tooltips

   **Answer:** Age groups should typically be displayed on the X-axis to represent categories across the timeline.

10. **What advantage does a grouped bar chart provide over a standard bar chart when comparing median compensation across age groups?**
    - [ ] It combines all categories into a single visual
    - [ ] It focuses on a single category at a time
    - [x] It provides a comparison across multiple categories side by side
    - [ ] It eliminates the need for a legend

    **Answer:** Grouped bar charts allow comparison across multiple categories side by side.
