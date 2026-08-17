# Practice Quiz - Questions and Answers

## Module 1 - Introduction to Data Visualization Tools

1. **A stakeholder says a table of raw numbers is enough for an executive update on immigration trends. What is the strongest reason to include a visualization as well?**
   - [ ] It replaces the need to compute summary statistics.
   - [ ] It automatically corrects missing or inconsistent data.
   - [x] It can make patterns, changes, and comparisons easier to spot quickly.
   - [ ] It stores large datasets more efficiently than a DataFrame.

   **Answer:** A good visualization helps learners and stakeholders see trends, comparisons, and anomalies faster than a table of raw values alone.

2. **Which statement best reflects Matplotlib's historical design?**
   - [x] It was created to emulate MATLAB-style plotting while remaining an independent Python library.
   - [ ] It was designed mainly as a spreadsheet replacement for tabular analysis.
   - [ ] It was built to generate only web dashboards in browsers.
   - [ ] It was created as a database tool for storing scientific results.

   **Answer:** Matplotlib drew inspiration from MATLAB-style graphics commands, but it is an independent Python plotting library.

3. **Your team is writing a reusable function that creates several customized subplots. Which Matplotlib interface is usually the better choice?**
   - [x] The Axes or object-oriented interface, because it gives explicit control over figures and axes.
   - [ ] The implicit pyplot state-based interface, because complex plots are easiest when nothing is passed explicitly.
   - [ ] Direct Renderer calls, because everyday analysis code should work at the rendering layer.
   - [ ] Backend configuration commands, because they replace the need to work with figure or axes objects.

   **Answer:** The object-oriented interface is usually the clearer and more maintainable choice when you need explicit control over multiple plots and custom formatting.

4. **In a Jupyter notebook, a learner edits the cell that defines `years` but reruns only the cell that plots the chart. The plot still shows the old x-values. What should the learner do next?**
   - [ ] Close the notebook and create the plot in a different library.
   - [ ] Clear the chart title so the axis updates correctly.
   - [ ] Convert `years` to strings so the notebook refreshes the plot.
   - [x] Rerun the cell that defines `years`, then rerun the plotting cell.

   **Answer:** Notebook output reflects the state of variables in executed cells, so the data-definition cell must run before the plotting cell uses the updated values.

5. **Which code example best creates a line plot of annual immigration totals with years on the x-axis?**
   - [ ] `fig, ax = plt.subplots(); ax.scatter(years, totals)`
   - [ ] `fig, ax = plt.subplots(); ax.bar(years, totals)`
   - [ ] `fig, ax = plt.subplots(); ax.hist(totals)`
   - [x] `fig, ax = plt.subplots(); ax.plot(years, totals)`

   **Answer:** This code creates axes explicitly and plots yearly values as a line, which is appropriate for showing how totals change over time.

6. **The immigration DataFrame stores one row per country and one column per year. After selecting one country, which data shape is most useful for plotting its trend over time?**
   - [ ] A list that repeats the country name for every year
   - [ ] A table containing only metadata columns such as region
   - [x] A single series of yearly values indexed by year
   - [ ] A single total that sums all years into one number

   **Answer:** A one-dimensional series indexed by year is the most direct structure for plotting one country's change over time.

7. **Before plotting the immigration dataset, which actions help you understand its structure and potential data-quality issues? Select all that apply.**
   - [x] Use `df.head()` to preview the first rows.
         _Feedback: `df.head()` is a quick way to inspect how the data is laid out before you decide how to filter or plot it._
   - [ ] Use `plt.show()` before creating any plot.
   - [x] Use `df.info()` to inspect columns, data types, and missing values.
         _Feedback: `df.info()` helps you check whether the DataFrame structure and data types are suitable for analysis and plotting._
   - [ ] Use `df.to_csv()` to understand the structure.

8. **Which sequence is the most sensible workflow for analyzing an immigration dataset in a Pandas DataFrame before building a chart?**
   - [ ] Export the data to a spreadsheet, recolor rows manually, then build the chart.
   - [ ] Visualize immediately, then inspect structure only if the chart looks odd.
   - [x] Inspect structure, clean or select relevant data, organize the index or shape, then visualize.
   - [ ] Drop the year columns first, then choose a chart type.

   **Answer:** That sequence supports reliable analysis because you understand the data first, prepare it for the task, and then visualize the relevant result.

9. **After plotting immigration totals for several countries, one country's line shows a sharp single-year spike. What is the best next step?**
   - [ ] Assume the spike proves the country had the strongest long-term growth.
   - [ ] Remove the spike because line plots should always look smooth.
   - [ ] Replace the line plot with a histogram because time-based changes cannot be interpreted from a line chart.
   - [x] Check the underlying values and investigate whether the spike reflects a real event or a data-quality issue.

   **Answer:** A strong analyst verifies unusual patterns before drawing conclusions, especially when a sudden spike could reflect either a real-world event or a problem in the data.

10. **The DataFrame immigration_df has a Year column and one numeric column named India. Which command is the clearest choice for a line plot of immigration from India by year?**
    - [ ] `immigration_df.info()`
    - [ ] `immigration_df["India"].hist()`
    - [ ] `immigration_df.plot(x="India", y="Year", kind="bar")`
    - [x] `immigration_df.plot(x="Year", y="India", kind="line")`

    **Answer:** This command clearly identifies the x-axis, the y-axis, and the line plot type, which makes the intent of the chart easy to read.

## Module 2 - Basic Visualization Tools

1. **Select two: An area plot depicts cumulated totals using `_______` or `_______` over time.**
   - [ ] Charts
   - [x] Percentages
   - [ ] Data
   - [x] Numbers

   **Answer:** An area plot depicts cumulated totals using percentages or numbers over time.

2. **An area plot, also known as an area chart or graph, displays the `__________________` of multiple variables.**
   - [ ] Proportion and area
   - [x] Magnitude and proportion
   - [ ] Proportion and perimeter
   - [ ] Magnitude and area

   **Answer:** An area plot displays the magnitude and proportion of multiple variables over a continuous axis, typically representing time or another ordered dimension.

3. **A histogram is a way of representing the frequency distribution of a `________________`.**
   - [ ] Statistical dataset
   - [ ] Demographic dataset
   - [ ] Alphabetical dataset
   - [x] Numeric dataset

   **Answer:** A histogram works by partitioning the spread of numeric data into bins, assigning each data point to a bin, and then counting the number of data points assigned to each bin.

4. **In a Histogram, the `______________` axis is the frequency or the number of data points in each bin.**
   - [x] Vertical
   - [ ] Horizontal
   - [ ] Perpendicular
   - [ ] Parallel

   **Answer:** The vertical axis is the frequency or the number of data points in each bin.

5. **True or False. The following code will create a horizontal bar chart of the data in the pandas DataFrame `question`:**
   `question.plot(type='bar', rot=90)`
   - [ ] True
   - [x] False

   **Answer:** The parameters used are incorrect — for example, `type` is used instead of `kind`.

## Module 2 - Specialized Visualization Tools

1. **What is a scatter plot?**
   - [ ] A scatter plot represents the frequency distribution of a numeric dataset
   - [ ] A scatter plot displays the magnitude and proportion of multiple variables over a continuous axis
   - [ ] A scatter plot is a circular statistical graphic divided into segments
   - [x] A scatter plot is a type of plot that displays values pertaining to typically two variables against each other

   **Answer:** A scatter plot is a type of plot that displays values pertaining to typically two variables against each other. Usually, it is a dependent variable plotted against an independent variable.

2. **True or False. Matplotlib is a general-purpose comprehensive plotting library that provides a flexible interface for creating a wide range of plots.**
   - [x] True
   - [ ] False

   **Answer:** Matplotlib is a general-purpose comprehensive plotting library that provides a flexible interface for creating a wide range of plots. Its pyplot module offers a convenient way to create and customize plots quickly.

3. **What is a pie chart?**
   - [ ] A pie chart is a type of plot in which the length of each bar is proportional to the value of the item that it represents
   - [ ] A pie chart is a graphical representation that showcases the relative size and proportion of various variables along a continuous axis
   - [ ] A pie chart visually depicts the distribution of a numeric dataset by showcasing the frequency of each category
   - [x] A pie chart is a circular statistical graphic divided into segments to illustrate numerical proportions

   **Answer:** A pie chart is a circular statistical graphic divided into segments to illustrate numerical proportions. The explode property in a pie chart enables you to offset slices from the center, highlighting specific sections.

4. **A box plot is a way of statistically representing the distribution of a dataset using how many key statistical measures?**
   - [ ] 3
   - [ ] 8
   - [x] 5
   - [ ] 1

   **Answer:** A box plot is a way of statistically representing the distribution of given data through five main measures. These include Minimum, First quartile, Median, Third quartile, and Maximum.

5. **What is the first step when plotting with Matplotlib?**
   - [ ] Import Pandas
   - [x] Import matplotlib.pyplot as plt
   - [ ] Call the subplot function
   - [ ] Call the plot function

   **Answer:** The first step is to import the library. You import matplotlib.pyplot as plt.
