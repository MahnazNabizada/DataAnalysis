# Lab 6: Filtering, Sorting, and Data Analysis Functions in Excel

---

## Exercise 1: Filtering and Sorting Data

In this exercise, you will learn how to use the Filter and Sort tools in Excel to
control what information is displayed and how it is displayed in your worksheets.

---

### Task A: Filtering Data

#### Auto Filters

1. Download the file **Customer_demographics_and_sales_Lab6.xlsx**. Upload and open it using Excel for the web.
2. Select any cell in the data, click the **Data** tab, then click **Filter**.
3. Click the filter drop-down in column **AG** (`Purchase_Status`) and select **Filter…**
4. In the list, select only **Frequent** and click **OK**.
5. Click the filter drop-down in column **AG** again and click **Clear Filter From "Purchase_Status"**.
6. Click the filter drop-down in column **AE** (`T_Type`) and select **Filter…**
7. In the list, select only **Cancelled** and click **OK**.
8. Click the filter drop-down in column **AF** (`Purchase_Touchpoint`) and select **Filter…**
9. In the list, select only **Desktop** and click **OK**.
10. On the **Data** tab, click **Clear**.

#### Custom Filters

1. Click the filter drop-down in column **AD** (`Order_Value`), then select **Number Filters > Top 10…**
2. Change the value from `10` to `50` and click **OK**.
3. Click the filter drop-down in column **AD** and click **Clear Filter From "Order_Value"**.

---

### Task B: Sorting Data

1. On the **Data** tab, click **Custom Sort** to open the sort dialog box.
2. Click the **Column** drop-down under **Sort By** and select `Order_Ship_Date`.
3. Click the **Order** drop-down under **Sort By** and select **Sort Ascending**.
4. Click **Add**.
5. Click the **Column** drop-down under **Then By** and select `Order_Value`.
6. Click the **Order** drop-down under **Then By** and select **Sort Descending**.
7. Click **OK**.

---

## Exercise 2: Useful Functions for Data Analysis

In this exercise, you will learn how to use some of the most common functions a
Data Analyst might use: **IF**, **IFS**, **COUNTIF**, and **SUMIF**.

---

### Task A: Use IF to Apply One Condition

1. Select column **AF**, right-click and choose **Insert**.
2. In cell **AF1**, type `Complete?`.
3. In cell **AF2**, type the following formula and press **Enter**:
   ```
   =IF(AE2="Complete","Yes","No")
   ```
4. Double-click the **Fill Handle** on cell **AF2** to copy down the column.

---

### Task B: Use Nested IF to Apply Multiple Conditions

1. Select column **AE**, right-click and choose **Insert**.
2. In cell **AE1**, type `Order Size (IF)`.
3. In cell **AE2**, type the following formula and press **Enter**:
   ```
   =IF(AD2>300,"Large",IF(AD2>100,"Medium",IF(AD2>0,"Small")))
   ```
4. Double-click the **Fill Handle** on cell **AE2** to copy down the column.

---

### Task C: Use IFS as an Alternative to Nested IF

1. Select column **AE**, right-click and choose **Insert**.
2. In cell **AE1**, type `Order Size (IFS)`.
3. In cell **AE2**, type the following formula and press **Enter**:
   ```
   =IFS(AD2>300,"Large",AD2>100,"Medium",AD2>0,"Small")
   ```
4. Double-click the **Fill Handle** on cell **AE2** to copy down the column.

---

### Task D: Use COUNTIF to Count Cells Meeting a Criterion

1. Select cell **BX2** and type `count VISA card`.
2. Select cell **BY2**, type the following formula and press **Enter**:

   ```
   =COUNTIF(N2:N195,"VISA")
   ```

---

### Task E: Use SUMIF to Sum Values Meeting a Criterion

> **Formula:** `=SUMIF(range, criteria, [sum_range])`

1. Select cell **BX3** and type `sum Large order`.
2. Select cell **BY3**, type the following formula and press **Enter**:
   ```
   =SUMIF(AE2:AE195,"Large",AD2:AD195)
   ```

---

### Task F: Use SUMIFS to Sum Values Meeting Multiple Criteria

> **Formula:** `=SUMIFS([sum_range], range1, criteria1, range2, criteria2, …)`

1. Select cell **BX4** and type `sum Large order with Baby Gen`.
2. Select cell **BY4**, type the following formula and press **Enter**:
   ```
   =SUMIFS(AD2:AD195,AE2:AE195,"Large",AL2:AL195,"BABY_BOOMERS")
   ```

---

## Exercise 3: Using VLOOKUP and HLOOKUP Functions

In this exercise, you will learn how to use **VLOOKUP** and **HLOOKUP** to
reference data in vertical and horizontal lookup tables.

---

### Task A: Use VLOOKUP for Vertical Lookup Tables

> **Formula:** `=VLOOKUP(value, table, col_index, [range_lookup])`

1. Download the file **indian_startup_funding_Lab6.xlsx**. Upload and open it using Excel for the web.
2. In cells **K2**, **L2**, and **M2**, type `VLOOKUP`, `Startup Name`, and `Amount in USD` respectively.
3. Copy cells **C9:C15** and paste into cell **L3**.
4. In cell **M3**, type the following formula and press **Enter**:
   ```
   =VLOOKUP(L3,C2:I113,7,FALSE)
   ```
5. Hover over the bottom-right corner of cell **M3** and drag the **Fill Handle** down to **M9**.
6. Select cells **M3:M9** and apply **Number Format > Currency**.

---

### Task B: Use HLOOKUP for Horizontal Lookup Tables

> **Formula:** `=HLOOKUP(value, table, row_index, [range_lookup])`

1. Download the file **Personal_Monthly_Expenditure_Lab6.xlsx**. Upload and open it using Excel for the web.
2. In cells **J2**, **K2**, **L2**, and **M2**, type `HLOOKUP`, `Month`, `Food & Dining`, and `Health & Fitness` respectively.
3. Copy cells **A10:A12** and paste into cell **K3**.
4. In cell **L3**, type the following formula and press **Enter**:
   ```
   =HLOOKUP(D1,A1:H14,10,FALSE)
   ```
5. Drag the **Fill Handle** from cell **L3** down to **L5**.
6. Select cells **L3:L5** and apply **Number Format > Currency**.
7. In cell **M3**, type the following formula and press **Enter**:
   ```
   =HLOOKUP(G1,A1:H14,10,FALSE)
   ```
8. Drag the **Fill Handle** from cell **M3** down to **M5**.
9. Select cells **M3:M5** and apply **Number Format > Currency**.

## Solution

- [Customer_demographics_and_sales_Lab6.xlsx](./Customer_demographics_and_sales_Lab6.xlsx) _(89 KB)_
- [indian_startup_funding_Lab6.xlsx](./indian_startup_funding_Lab6.xlsx) _(22 KB)_
- [Personal_Monthly_Expenditure_Lab6](./Personal_Monthly_Expenditure_Lab6.xlsx) _(13 KB)_
