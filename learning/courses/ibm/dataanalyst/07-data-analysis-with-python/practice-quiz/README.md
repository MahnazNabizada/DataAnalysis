# Practice Quiz - Questions and Answers

## Module 1 - Importing Data Sets

1. **Which of the following commands would you use to retrieve only the attribute datatypes of a dataset loaded as pandas data frame df?**
   - [ ] `df.describe(include='all')`
   - [x] `df.dtypes`
   - [ ] `df.info()`
   - [ ] `df.describe()`

   **Answer:** `df.dtypes` is the command that retrieves only the attribute datatypes.

2. **What description best describes the library Pandas?**
   - [ ] Includes functions for creating various plots that can be used to create different visualizations for the dataset.
   - [x] Offers data structures and tools for effective data manipulation and analysis, providing fast access to structured data.
   - [ ] Includes functions for some advanced math problems and scientific processes such as integration and optimization.
   - [ ] A highly efficient array processing library capable of quickly performing mathematical transformation functions on single or multi-dimensional arrays.

   **Answer:** The primary instrument of Pandas is the DataFrame, a two-dimensional table with rows and columns. It simplifies tasks like indexing, slicing, and cleaning data, making it the standard for data manipulation.

3. **What task does the following code perform?**

   ```python
   path = 'C:\Windows\...\automobile.csv'
   df.to_csv(path)
   ```

   - [ ] Opens a CSV file specified by the path for manual editing.
   - [ ] Converts a CSV file in the directory specified by the path to a data frame.
   - [x] Exports your Pandas data frame to a new CSV file in the location specified by the variable path.
   - [ ] Loads a CSV file from the local directory into a new data frame.

     **Answer:** The `.to_csv()` method is an "output" function. It takes the data currently held in the DataFrame df and writes it into a permanent file on your local machine at the specified path.

4. **How would you use the describe() method with a data frame df to get a statistical summary of all the columns in the data frame?**
   - [ ] `df.describe(include="None")`
   - [ ] `df.describe(include="columns")`
   - [x] `df.describe(include="all")`
   - [ ] `df.describe(include="summary")`

   **Answer:** By passing `include="all"`, you tell Pandas to calculate statistics for every column regardless of type. For text columns, it will provide the number of unique values, the most frequent value, and its frequency.
