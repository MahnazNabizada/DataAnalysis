# Final Exam

1. **Which of the following describes a file you receive with plain text, rows, and columns of data?**
   - [x] A text file that saves data in tables
   - [ ] An array of values separated by a comma
   - [ ] A Microsoft Excel spreadsheet
   - [ ] A text file containing key-value pairs

   **Answer:** A CSV is a text-based file that saves data in a tabular format.

2. **Your project requires libraries that support regression models and hypothesis testing. Which Python libraries are primarily algorithmic libraries?**
   - [ ] Pandas, Numpy, SciPy
   - [x] Scikit-learn, Statsmodels
   - [ ] Matplotlib, Seaborn
   - [ ] Jupyter, Regression

   **Answer:** Scikit-learn and Statsmodels Python libraries are primarily algorithmic libraries.

3. **A financial analyst uses Pandas to load transaction logs stored in CSV files on a remote server. What are the two most important factors to read data using the Python Pandas package?**
   - [ ] Encoding scheme and file path
   - [ ] File types and encoding scheme
   - [ ] File types and formats
   - [x] Format and file path

   **Answer:** Format and file path are two important factors to read data using Pandas library

4. **Why do data analysts prefer Python's DB API when working with relational databases?**
   - [ ] It adds advanced encryption without database configuration.
   - [ ] It removes the need for authentication in connection setup.
   - [ ] It generates a database schema automatically in Python.
   - [x] It offers consistent functions for connection, transaction, and query execution.

   **Answer:** DB API abstracts database interaction into a standardized interface, simplifying coding across databases.

5. **Which regression method best fits the equation below?**

   $$\hat{y} = b_0 x^3 + b_1 x^2 + b_2 x + b_3$$
   - [x] Polynomial regression
   - [ ] Multiple linear regression
   - [ ] Exponential regression
   - [ ] Linear regression

   **Answer:** Polynomial regression involves applying exponents to input features to model nonlinear relationships.

6. **While running a polynomial regression, you noticed that the residual plot displays a curved pattern. What does this indicate about the model?**
   - [ ] The independent variable has no measurable impact.
   - [ ] The low R-squared values are aligned with MSE.
   - [ ] The model fits the linear trend for data distribution.
   - [x] The model lacks nonlinear relationships in the data.

   **Answer:** A curved pattern in the residual plot suggests nonlinearity in the linear model that fails to capture the data.

7. **A data scientist performs various experiments by repeatedly separating a housing dataset into 70% training and 30% testing and notices different R² values each time. **What best explains the inconsistency in the R² scores across different trials?\*\*
   - [ ] Changes in the distribution of price values
   - [ ] Modifying learning patterns between runs
   - [x] Unsystematic variation in train-test partitions
   - [ ] Lowered accuracy due to reduced testing data

   **Answer:** Diverse training and test breaks can lead to different results, affecting consistency.

8. **What function should you use to remove rows and columns with null or NaN values?**
   - [ ] `removena()`
   - [ ] `replacena()`
   - [ ] `findna()`
   - [x] `dropna()`

   **Answer:** The `dropna()` method removes rows and columns with null or NaN values.

9. **You are using numpy.linspace and pandas.cut for segmenting the car price features into three equal-width bins. How will the binning approach help you in this task?**
   - [ ] It filters price values that do not fit into a bin.
   - [x] It creates labeled segments for price intervals.
   - [ ] It equalizes price values across cars.
   - [ ] It randomizes the price into labeled bins.

   **Answer:** Using linspace and cut helps categorize continuous data into labeled intervals, improving interpretability.

10. **A data analyst is evaluating a used car dataset where "length" ranges from 150 to 250, whereas "width" and "height" range from 50 to 100. They want all features to contribute equally to the analysis. **Which technique should they apply to ensure fair comparison across features with different ranges?\*\*
    - [ ] Increase larger values to match smaller ones.
    - [ ] Remove high-value features from the dataset.
    - [ ] Prioritize only features with similar ranges.
    - [x] Use normalization to standardize data values.

    **Answer:** Normalization enables a fairer comparison between the different features, making sure they have the same impact.

11. **After importing a dataset, a data scientist wants to evaluate the statistics inputs for each column before preprocessing. Which Pandas method should they use?**
    - [ ] `dataframe.astype("int")`
    - [x] `dataframe.dtypes`
    - [ ] `dataframe.rename()`
    - [ ] `dataframe.values()`

    **Answer:** The dtypes attribute returns the data type of each column in a DataFrame, which is useful for reviewing and validating data types before transformation.

12. **Ramaya is working with a dataset to understand what factors affect housing prices. He wants to uncover relationships between variables to extract important features. **Which method best helps summarize the main characteristics of a dataset and identify key influencing variables?\*\*
    - [ ] Model tuning and optimization
    - [ ] Data normalization and feature scaling
    - [ ] Data splitting into train and test sets
    - [x] Exploratory data analysis techniques

    **Answer:** Exploratory data analysis is an approach to analyze data to summarize the main characteristics of the data, gain a better understanding of the dataset, uncover relationships between different variables, and extract important variables.

13. **A data scientist evaluates scatter plots with regression lines to examine variable relationships between engine size and price. What does this scatter plot indicate?**
    - [ ] Exponential relationship
    - [ ] No clear relationship
    - [ ] Negative linear relationship
    - [x] Positive linear relationship

    **Answer:** Since the price tends to increase per unit of increase in the engine size, this plot has a positive linear relationship.

14. **Which visualization technique should a company leverage to compare price distribution across drive types?**
    - [ ] Use the describe function
    - [ ] Create a line graph
    - [ ] Create a scatter plot
    - [x] Create a box plot

    **Answer:** Box plots make easy price comparison between groups. Using a box plot, you can distribute different categories of the drive-wheels feature over the price feature.

15. **Your team is preparing a summary report showing how average prices vary across car features. Which method is useful in this scenario?**
    - [ ] Sort the data by numerical values
    - [ ] Filter data using a logical algorithm
    - [x] Form groups using category values
    - [ ] Join datasets with similar columns

    **Answer:** The groupby method allows the creation of grouped subsets by one or more categorical columns.

16. **Jenny uses color, mileage, and model year to estimate car prices with linear regression. Why is it important to add car color to the model?**
    - [ ] Fewer features increase model complexity.
    - [ ] Features reduce the output range.
    - [x] Eliminating relevant features leads to inaccurate predictions.
    - [ ] Irrelevant features confuse the output.

    **Answer:** Ignoring impactful features such as color may cause the model to predict the same price for dissimilar cars.

17. **After fitting a regression model, a data analyst visualizes the residuals and notices a clear curve in the pattern. What can be inferred when residuals in a regression plot follow a systematic, curved pattern?**
    - [ ] The relationship between variables is linear.
    - [ ] The prediction errors are uniformly low across values.
    - [ ] Residuals are randomly distributed around zero.
    - [x] The model may be inaccurate in capturing the data structure.

    **Answer:** A curved pattern in residuals often implies that a linear model is inappropriate for the data.

18. **While evaluating a regression model's performance, you noticed unpredictable variations in the predicted values, even though the model fits the data well. What is true about noise in the data?**
    - [ ] If your training data fits your function well, you will not see noise in your predicted values.
    - [ ] Your model accounts for it with a parameter.
    - [x] It is random and cannot be predicted.
    - [ ] If your testing data fits your function well, you will not see noise in your predicted values.

    **Answer:** Noise in the data is random and cannot be predicted.

19. **Sofia uses a ridge regression model to predict housing prices. She noticed that increasing the alpha value results in a smoother curve and significantly shows poor prediction accuracy on both training and test sets. What does a large alpha value indicate in this scenario?**
    - [ ] The model should be a lower-order function.
    - [x] The model is underfitted.
    - [ ] The model is overfitted.
    - [ ] The higher the alpha, the better the fit.

    **Answer:** A high alpha value indicates that the coefficient will approach zero and underfit the model.

20. **What does the GridSearchCV() method do?**
    - [ ] It selects the appropriate hyperparameters for your model.
    - [ ] It is another way to cross-validate your dataset.
    - [x] It iterates over hyperparameters using cross-validation.
    - [ ] It gives you R2 values for different orders of polynomial models.

    **Answer:** The `GridSearchCV()` iterates over hyperparameters using cross-validation.
