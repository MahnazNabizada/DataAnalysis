# Final Assignment Part 1: Data Cleaning

## Assignment Scenario

In this final assignment, you will be following the scenario of a recently hired Junior Data Analyst in a local government office, who has been tasked with importing some data from another department which relates to inventory information about their fleet of vehicles. The data is in comma-separated value (CSV) format and the data also needs cleaning up before you can start to run any kind of analysis on it.

## Guidelines for the Submission

Download the file `Montgomery_Fleet_Equipment_Inventory_FA_PART_1_START.CSV`. Upload and open the file with Excel for the web and convert it to an .XLSX file. Then clean the data as detailed below.

Use the course videos from Module 3 and the lab **"Hands-on Lab 5: Cleaning Data"** to help you complete these tasks.

## Tasks to Perform

**Step 1: Save the CSV file as an XLSX file**
Change the 'Viewing' in the ToolTip to 'Editing' in order to save the file as an XLSX file. The file is converted when you click 'Convert' in the prompt.

**Step 2: Column widths**
Sort out the widths of all columns so that the data is clearly visible in all cells.

**Step 3: Empty rows**
Use the Filter feature to look for blanks and remove all empty rows from the data.

**Step 4: Duplicate records**
Use either the Conditional Formatting or Remove Duplicates feature to look for and remove any duplicated records from the data.

**Step 5: Spelling**
The original source file data has not been checked for errors in the spelling. Check for spelling mistakes in the data and fix them.

**Step 6: Whitespace**
Use the Find and Replace feature to remove all double-spaces from the data.

**Step 7: Department names**
When the data was converted from its data source, the department names (see correct list below) didn't import correctly and they are now split over two columns in the data. Use Flash Fill to reduce the department names to just one column, and then remove any unnecessary columns.

| Department                         | Department                |
| ---------------------------------- | ------------------------- |
| Board of Elections                 | Economic Development      |
| Circuit Court                      | Environmental Protection  |
| Community Engagement Cluster       | Finance                   |
| Community Use of Public Facilities | Fire and Rescue           |
| Consumer Protection                | General Services          |
| Correction and Rehabilitation      | Health and Human Services |
| County Executives Office           |                           |

**Step 8: Download your workbook**
Use 'Save As' and select 'Download a copy' to download your completed workbook as `Montgomery_Fleet_Equipment_Inventory_FA_PART_1_END.XLSX`.

> **Note:** In Excel web version, files are auto saved.

## Grading Information

For your assignment to be graded in a subsequent step in this course, you will be required to upload the completed Excel workbook that you saved in Task 8.

**The main grading criteria will be:**

- Is the data saved correctly?
- Is the data formatted correctly?
- Has the data been cleaned correctly?

**You will not be judged on:**

- Your English language, including spelling or grammatical mistakes.
- The content of any text or image(s) or where a link is hyperlinked to.

---

# Final Assignment Part 2: Pivot Tables

## Assignment Scenario

In this final assignment, you will be following the scenario of a recently hired Junior Data Analyst in a local government office, who has been tasked with sorting and analyzing fleet inventory data that was previously imported and cleaned. You plan to use pivot tables to analyze the data in preparation for the results to be visualized in a dashboard and added to a data findings report later.

## Guidelines for the Submission

Download and open the [Montgomery_Fleet_Equipment_Inventory_FA_PART_2_START.XLSX](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0130EN-SkillsNetwork/Hands-on%20Labs/Peer%20Graded%20Assignment%20-%20Part%202/Montgomery_Fleet_Equipment_Inventory_FA_PART_2_START.xlsx) file in Excel for the web.

Use the course videos from Module 4 and the lab **"Hands-on Lab 7: Using Pivot Tables"** to help you complete these tasks.

## Tasks to Perform

**Step 1: Format the data as a table**
Use the Format as Table option to format the data as a table.

**Step 2: Use AutoSum to calculate values**
Use AutoSum to find the following values for column 'C' and record each of the values:

- SUM
- AVERAGE
- MIN
- MAX
- COUNT

**Step 3: Create a Pivot Table**
Create a new worksheet and name it _Pivot Table 1_. Use the PivotTable feature to create a pivot table that displays the Department field in the Rows section, and the Equipment Count in the Values section, so that the pivot table displays the sum of equipment count by department.

**Step 4: Sort the pivot table data**
Use the Sort By Value setting on the pivot table to sort it in descending order by the sum of equipment count.

**Step 5: Make two more pivot tables exactly the same as task 3**
Create two new worksheets named _Pivot Table 2_ and _Pivot Table 3_. Follow the same steps you performed in Tasks 3 and 4 to create two more identical pivot tables so that you end up with 3 worksheets that contain identical pivot tables.

**Step 6: Analyze data in the pivot table**
Use the PivotTable Fields pane to manipulate and analyze data in the two copied pivot tables as follows:

- In _Pivot Table 2_ add the Equipment Class field below the Department field so that the different vehicle types appear under each department with their respective counts.
- Collapse all fields except the top one — Transportation.
- In _Pivot Table 3_ add the Equipment Class field above the Department field so that the different vehicle types appear first, with the different departments listed underneath each vehicle type with their respective counts.
- Collapse all fields except the top one — CUV.

Ensure the worksheets are arranged in the following order in the workbook: _Montgomery_Fleet_Equipment_Inventory_, followed by _Pivot Table 1_, _Pivot Table 2_, and _Pivot Table 3_.

**Step 7: Download your workbook**
Use Save As and select Download a copy to download your completed workbook as `Montgomery_Fleet_Equipment_Inventory_FA_PART_2_END.XLSX`.

> **Note:** In Excel web version, files are auto saved.

## Grading Information

For your assignment to be graded in a subsequent step in this course, you will be required to upload the completed Excel workbook that you saved in Task 7.

**The main grading criteria will be:**

- Is the data formatted as a table?
- Are the AutoSum values correct?
- Has the correct pivot table been created and sorted?
- Has the pivot table been created two more times?
- Have the correct fields been used in pivot tables 2 and 3?
- Has the workbook been saved correctly?

**You will not be judged on:**

- Your English language, including spelling or grammatical mistakes.
- The content of any text or image(s) or where a link is hyperlinked to.

## Solution

- [Montgomery_Fleet_Equipment_Inventory_FA_PART_1_END.xlsx](./Montgomery_Fleet_Equipment_Inventory_FA_PART_1_END.xlsx) _(12 KB)_
- [Montgomery_Fleet_Equipment_Inventory_FA_PART_2_END.xlsx](./Montgomery_Fleet_Equipment_Inventory_FA_PART_2_END.xlsx) _(23 KB)_
