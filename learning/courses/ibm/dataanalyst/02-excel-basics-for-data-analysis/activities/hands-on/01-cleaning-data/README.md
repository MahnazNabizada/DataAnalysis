# Lab 5: Data Cleaning in Excel

---

## Exercise 1: Removing Duplicated, Irrelevant or Inaccurate Data

In this exercise, you will learn how to deal with inaccurate data, how to remove
empty rows, and how to remove duplicated data.

---

### Task A: Check Spelling

1. Download the file **Customer_demographics_and_sales_Lab5.xlsx**. Upload and open it using Excel for the web.
2. Select column **L** (`CREDITCARD_TYPE`), then click the **Review** tab and select **Spelling**.

> **Note:** Do not change the spelling of `jcb` during the spell check — it will be needed in Exercise 1, Task D.

3. Close the **Spelling** pane.

---

### Task B: Remove Empty Rows

1. Press `CTRL+HOME`, then press `CTRL+SHIFT+END` to select the whole datasheet.
2. On the **Data** tab, click **Filter**.
3. Press `CTRL+HOME`, click the filter arrow in the **CUST_NAME** column, then click **Filter**.
4. Click the **Select All** checkbox to deselect all, then select only **Blanks** and click **OK**.
5. Select the first row, then press `CTRL+SHIFT+END` to select all blank rows.
6. Right-click the selected rows and choose **Delete Rows**.
7. On the **Data** tab, click **Clear**, then click **Filter**.

---

### Task C: Remove Duplicate Rows

1. Select column **T** (`ORDER_ID`), since `ORDER_ID` values are unique.
2. On the **Home** tab, click **Conditional Formatting > Highlight Cells Rules > Duplicate Values**, then click **OK**.
3. Select the whole datasheet (`CTRL+SHIFT+END`).
4. On the **Data** tab, click **Remove Duplicates**.
5. In the **Remove Duplicates** dialog box, ensure **Select all columns** and **My data has headers** are both checked, then click **OK**.
6. In the confirmation pop-up, click **OK**.

---

### Task D: Use Find & Replace to Correct Misspelling

1. On the **Home** tab, click **Find & Select**.
2. Click **Find**. In **Find what**, type `jcb`, then click **Find All**.
3. Click **Replace**. In **Replace with**, type `JCB`, click **Replace All**, then click the **Close** icon.
4. On the **Home** tab, click **Conditional Formatting > Clear Rules > Clear Rules from Entire Sheet**.

---

## Exercise 2: Dealing with Inconsistencies in Data

In this exercise, you will learn how to change the case of text, change date
formatting, and trim whitespace from data.

---

### Task A: Use PROPER to Change Text to Proper Case

1. Select row **2**, right-click and choose **Insert Rows**.
2. In cell **A2**, type `=PROPER(A1)` and press **Enter**.
3. Select row **2**, then press `CTRL+C`.
4. Select row **1**, right-click and choose **Paste Options > Values**.
5. Select row **2**, right-click and choose **Delete Rows**.

---

### Task B: Use UPPER to Change Text to Upper Case

1. Select column **AG** (`Generation`), right-click and choose **Insert Columns**.
2. In cell **AG1**, type `Generation`.
3. In cell **AG2**, type `=UPPER(AH2)` and press **Enter**.
4. Hover over the bottom-right corner of cell **AG2** and double-click the **Fill Handle**.
5. Select column **AG**, then press `CTRL+C`.
6. Select column **AH**, right-click and choose **Paste Options > Values**.
7. Select column **AG**, right-click and choose **Delete Columns**.

---

### Task C: Use LOWER to Change Text to Lower Case

1. Select column **AC** (`T_Type`), right-click and choose **Insert Columns**.
2. In cell **AC1**, type `T_Type`.
3. In cell **AC2**, type `=LOWER(AD2)` and press **Enter**.
4. Hover over the bottom-right corner of cell **AC2** and double-click the **Fill Handle**.
5. Select column **AC**, then press `CTRL+C`.
6. Select column **AD**, right-click and choose **Paste Options > Values**.
7. Select column **AC**, right-click and choose **Delete Columns**.

---

### Task D: Change Date Formatting

1. Select column **Z** (`Order_Ship_Date`).
2. On the **Home** tab, in the **Number** group, click **Number Format > More Number Formats**.
3. In the **Category** list, select **Date**.
4. In the **Format Cells** box, under **Locale**, select **English (United States)**.
5. Under **Type**, select **Wednesday, March 14, 2012** and click **OK**.

---

### Task E: Use Find & Replace to Trim Whitespace

1. Press `CTRL+HOME`.
2. Select all data using `CTRL+SHIFT+END`.
3. On the **Home** tab, click **Find & Select**, then **Replace**.
4. In **Find what**, type **2 spaces**. In **Replace with**, type **1 space**.
5. Click **Find All**, then click **Replace All**.
6. Click the **Close** icon.

---

## Exercise 3: More Excel Features for Cleaning Data

In this exercise, you will learn how to use the Flash Fill feature and functions
in Excel to help clean data.

---

### Task A: Use Flash Fill to Clean Data

1. Select column **A** (`Cust_Name`), right-click and choose **Insert Columns**.
2. In cell **A1**, type `Customer_Name` and press **Enter**.
3. In cell **A2**, type `Mr. Allen Perl` and press **Enter**.
4. Select column **A** (`Customer_Name`), then on the **Data** tab, click **Flash Fill**.
5. Click **Undo** to undo this step.

> **Note:** In the **desktop version** of Excel, you can use the **Text to Columns**
> feature for this task (see the corresponding topic video). In **Excel for the web**,
> this feature is unavailable — use the functions below instead.

---

### Task B: Use LEFT, RIGHT, LEN, and SEARCH Functions to Clean Data

1. Select column **A** (`Cust_Name`), right-click and choose **Insert Columns**.
2. Select column **A** again, right-click and choose **Insert Columns**.
3. In cell **A1**, type `Customer_Firstname`. In cell **B1**, type `Customer_Lastname`.
4. Click **C1**, then on the **Home** tab, click **Format Painter** and drag across to **A1** and **B1**.
5. Double-click the divider between columns **A** and **B** to auto-fit.
6. In cell **A2**, type `=LEFT(C2, SEARCH(" ",C2,1))` and press **Enter**.
7. In cell **B2**, type `=RIGHT(C2,LEN(C2)-SEARCH(" ",C2,1))` and press **Enter**.
8. Double-click the **Fill Handle** on cell **A2**.
9. Double-click the **Fill Handle** on cell **B2**.

---

## Solution

- [Customer_demographics_and_sales_Lab5.xlsx](./Customer_demographics_and_sales_Lab5.xlsx) _(76 KB)_
