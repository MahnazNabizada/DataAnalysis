# Activity Time: Case Analysis

Maria is a 25-year-old US Army veteran, newly returned to the civilian workforce.
She has recently completed a six-year commitment with the Army. During her time
in the Army, she worked in supply management and logistics. She has decided to
pursue a degree in Management Systems and Information Technology.

Maria has asked you to use your data skills to help her search for the best school
for her. She is willing to relocate anywhere in the continental United States, but
she has a few criteria that her ideal schools must satisfy:

1. Safety of the city
2. Schools should be offering a degree in IT
3. Ranking of the school

Please refer to the following datasets:

- [CollegeScorecard2.xlsx](CollegeScorecard2.xlsx) _(8.2 KB)_
- [Crime_2015.xlsx](./Crime_2015.xlsx) _(6.8 KB)_

---

## Your Next Steps

### 1. Clean the Data

- Duplicates
- Missing values
- Inconsistent values

### 2. Data Enrichment

- Calculate school ranking
- Calculate the overall crime rate

### 3. Structure the Data

Merge the tables and produce a dataset which must:

- Include the **top 5 schools** ranked for IT colleges
- Be located in a city **below the 50th percentile** in overall crime
- Have all **unnecessary columns removed**

---

## Solution

| University                            | City        | Courses                       | Total Crimes |
| ------------------------------------- | ----------- | ----------------------------- | ------------ |
| University of California, Los Angeles | Los Angeles | Architecture / ARTS / IT      | 3,469.7      |
| Duke University                       | Durham      | Electronics / IT / Biomedical | 3,192.9      |

- [CaseAnalysis.xlsx](./CaseAnalysis.xlsx) _(18 KB)_
