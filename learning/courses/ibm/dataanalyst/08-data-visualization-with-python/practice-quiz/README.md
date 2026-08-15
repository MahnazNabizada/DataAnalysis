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
