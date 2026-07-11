# Lab 7: Pivot Tables in Excel

---

## Exercise 1: Introduction to Creating Pivot Tables in Excel

In this exercise, you will learn how to format data as a table, create a Pivot Table,
use fields to arrange data, and perform calculations using Pivot Table data.

---

### Task A: Format Data as a Table

1. Download the file **indian_startup_funding_Lab7.xlsx**. Upload and open it using Excel for the web.
2. Select cell **A2**.
3. On the **Home** tab, in the **Tables** group, click **Format as Table**.
4. Select **Light Gray, Table Style Medium 15**.

---

### Task B: Create a Pivot Table and Arrange Data Using Fields

1. Select cell **D4**.
2. On the **Insert** tab, click **PivotTable**.
3. Click **OK**.
4. Double-click **Sheet1**, type `Pivot1` and click **OK**.
5. In the fields list, drag **Industry Vertical** to **Rows**.
6. In the fields list, drag **City Location** to **Rows**, above **Industry Vertical**.
7. In the fields list, drag **Startup Name** to **Rows**, below **Industry Vertical**.
8. In the fields list, drag **Amount in USD** to **Values**.
9. Use the drop-down arrow for **City Location** and sort by value in **Descending order (Largest to Smallest)** by the **Count of Amount in USD**.
10. In the ribbon, select the **PivotTable** tab, click **Settings**, then in the **PivotTable Settings** pane, under **Layout**, select **Single column**.
11. Right-click on the row label **Amritsar** and select **Expand/Collapse > Collapse Entire Field**.

---

### Task C: Perform a Simple Calculation in a Pivot Table

1. In the **PivotTable Fields** pane, under the **Values** section, click the drop-down arrow next to **Count of Amount in USD** and click **Value Field Settings**.
2. Select **Summarize value field by > Sum**.
3. Click **OK**.
4. Select the column **Sum of Amount in USD**, then on the **Home** tab, select **Accounting Number Format > $ English (United States)**.

---

## Exercise 2: Pivot Table Features

In this exercise, you will learn additional Pivot Table features including
**Recommended Charts**, **Filters**, **Slicers**, and **Timelines**.

> **Note:** The **Recommended Charts** feature only works with full Office for the
> web plans (those included with an Office 365 subscription). It does not work
> with the basic plan that comes with a Microsoft Account.

---

### Task A: Use Recommended Charts _(Optional — Full Office 365 Plan Required)_

1. Switch to the worksheet **indian-startup-funding**.
2. Select column **F** (`City Location`).
3. On the **Insert** tab, select **Recommended Charts**.
4. Click **+ Insert PivotChart**.
5. Switch back to the worksheet **indian-startup-funding**.
6. Select columns **C**, **D**, and **E**.
7. On the **Insert** tab, select **Recommended Charts**.
8. Choose the recommended chart and click **+ Insert PivotChart**.

---

### Task B: Use the Filters Feature

1. Switch to the worksheet **Pivot1**.
2. In the Pivot Table, click the **Row Labels** arrow.
3. Select **City Location**, then click **Filter…**
4. Select only **Burnsville**, **Delhi**, and **New York**, then click **OK** to display amounts for startups in those three cities.
5. Click the **Row Labels** arrow again.
6. Select **City Location**, then click **Clear Filter From 'City Location'** to display all cities again.

---

### Task C: Use the Slicers Feature

1. Download the file **indian_startup_funding_Lab7_with_slicers_timelines.xlsx**. Upload and open it using Excel for the web.
2. Switch to the worksheet **Pivot1** if not already there.
3. In the **City Location** slicer, select **Burnsville**, then **Delhi**, then **New York**.
4. To select multiple items, with **New York** still selected, hold `CTRL` and select **Burnsville** and **Delhi**.
5. To filter using more than one slicer, in the **Investors Name** slicer, select **Amour Infrastructure**, then hold `CTRL` and select **Westbridge Capital** and **Breakthrough Energy Ventures**.
6. In the **City Location** slicer, click the **Clear Filter** button.
7. In the **Investors Name** slicer, click the **Clear Filter** button.

---

### Task D: Use the Timelines Feature

1. In the **Date** timeline, click the top-right drop-down and select **DAYS**, then scroll left and right to explore.
2. Click the top-right drop-down again and select **QUARTERS**.
3. In the **Date** timeline, select **2019 Q1**, then drag to extend the selection to **2019 Q3**.
4. Click the **Clear Filter** icon in the **Date** timeline.
5. Click the top-right drop-down and select **YEARS**, then select **2020** only.

## Solution

- [indian_startup_funding_Lab7.xlsx](./indian_startup_funding_Lab7.xlsx) _(57 KB)_
- [indian_startup_funding_Lab7_with_slicers_timelines.xlsx](./indian_startup_funding_Lab7_with_slicers_timelines.xlsx) _(43 KB)_
