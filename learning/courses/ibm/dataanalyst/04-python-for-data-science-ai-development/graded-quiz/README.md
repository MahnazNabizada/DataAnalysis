# Graded Quiz - Questions and Answers

## Module 1 - Python Basics

1. **A data scientist is tracking the daily temperature. The code below represents the temperature dropping 3 degrees from the morning reading. What will the value of `evening_temp` be after execution?**

   ```python
   morning_temp = 22
   evening_temp = morning_temp - 3
   ```

   - [ ] 3
   - [ ] 25
   - [x] 19
   - [ ] 22

   **Answer:** The evening temperature is calculated by subtracting 3 from the morning temperature value (22 - 3 = 19).

2. **What is the output of the following operation in Python?**

   ```python
   2 + 3 * 4 / 2
   ```

   - [ ] 4.0
   - [ ] 14.0
   - [x] 8.0
   - [ ] 10.0

   **Answer:** The operation follows standard mathematical order of operations: multiplication and division first (3 \* 4 / 2 = 6), then addition (2 + 6 = 8.0).

3. **What data type is represented by `"3.14"`?**
   - [ ] Boolean
   - [x] String
   - [ ] Float
   - [ ] Integer

   **Answer:** This is a string because the numbers are enclosed in quotation marks, making it text rather than a numerical value.

4. **What is the output of the following code segment?**

   ```python
   int(False)
   ```

   - [ ] 1
   - [x] 0
   - [ ] Error
   - [ ] "False"

   **Answer:** Converting the Boolean value False to an integer results in the value 0.

5. **A web developer is creating a form that collects a user's first and last name as separate inputs. Which Python code correctly combines the inputs "Maria" and "Rodriguez" into the full name "Maria Rodriguez" with a space between?**
   - [ ] `"Maria Rodriguez"`
   - [x] `"Maria" + " " + "Rodriguez"`
   - [ ] `"Maria" - "Rodriguez"`
   - [ ] `"Maria" + "Rodriguez"`

   **Answer:** This string concatenation joins the first name, a space, and the last name to create the properly formatted full name.

6. **Which statement accurately describes the purpose of string methods in Python?**
   - [x] String methods allow manipulation and transformation of string data.
   - [ ] String methods generate random text based on patterns.
   - [ ] String methods only work on strings with alphabetic characters.
   - [ ] String methods convert strings to other data types.

   **Answer:** String methods provide built-in functionality to perform common operations like changing case, finding substrings, and replacing text.

7. **For the string "Hello World" stored in variable `text`, what will `text[0:5]` return?**
   - [ ] "Hello "
   - [ ] "Hello World"
   - [x] "Hello"
   - [ ] "ello"

   **Answer:** String slicing with `[0:5]` extracts characters from index 0 up to (but not including) index 5.

8. **What key characteristic of Python contributes to its widespread adoption across diverse user groups?**
   - [ ] Python's exclusive focus on scientific computing.
   - [x] Python's readability and relatively flat learning curve.
   - [ ] Python's compatibility with only Windows operating systems.
   - [ ] Python requires users to have advanced mathematics skills.

   **Answer:** Python's emphasis on readability and simpler syntax makes it accessible to beginners while remaining powerful for experts.

9. **A data scientist is preparing to present findings from a complex analysis to non-technical stakeholders. Why would Jupyter Notebook be an appropriate tool for this task?**
   - [ ] Jupyter Notebooks automatically generate PowerPoint presentations.
   - [ ] Jupyter Notebooks hide all technical details from viewers.
   - [ ] Jupyter Notebooks can only display statistical results in table format.
   - [x] Jupyter Notebooks allow code, explanations, and visualizations to be combined in a narrative flow.

   **Answer:** Jupyter Notebooks enable the creation of documents that combine explanatory text with code and visual outputs, which is ideal for presenting technical work to diverse audiences.

10. **What will be the output of the following code?**

    ```python
    print("Python is \"awesome\"")
    ```

    - [x] `Python is "awesome"`
    - [ ] `Python is awesome`
    - [ ] `Python is \awesome`
    - [ ] Error

    **Answer:** The backslash escape sequence includes quotation marks within a string.
