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

## Module 2 - Python Data Structures

1. **Examine the tuple** `A=((11,12),[21,22])`, **which contains a tuple and list. What is the outcome of the following operation** `A[1]`**?**
   - [x] [21,22]
   - [ ] (11,12)
   - [ ] ((11,12),[21,22])
   - [ ] 11

   **Answer:** The index 1 corresponds to the second element in the tuple, which contains a list.

2. **A programmer is creating a music playlist system where artists and their songs are stored in tuples. The data structure** `playlist = (("Pop", "Rock"), ["Madonna", "Elvis"], ["Like a Prayer", "Jailhouse Rock"])` **contains genres, artists, and songs. Which code would extract only the list of songs?**
   - [ ] `playlist[0]`
   - [ ] `playlist[1]`
   - [x] `playlist[2]`
   - [ ] `playlist[2][0]`

   **Answer:** This index accesses the third element of the tuple, which contains the list of songs.

3. **A data analyst is building a shopping cart application. The current cart contains items** `['shirt', 'pants']` **stored in the variable cart. The analyst wants to add a collection of accessories as a single entry. What will the cart contain after executing** `cart.append(['hat', 'belt'])`**?**
   - [ ] ['shirt', 'pants', 'hat', 'belt']
   - [ ] ['hat', 'belt', 'shirt', 'pants']
   - [ ] [['hat', 'belt'], 'shirt', 'pants']
   - [x] ['shirt', 'pants', ['hat', 'belt']]

   **Answer:** The append method adds the entire list as a single nested element at the end of the original list.

4. **Consider the following list:** `A=["hard rock",10,1.2]`. **What will list A contain after the following command is run?** `del(A[1])`
   - [ ] [10, 1.2]
   - [ ] ["hard rock", 10]
   - [ ] Syntax error
   - [x] ["hard rock", 1.2]

   **Answer:** The del command removes the element at index 1, leaving the first and third elements of the original list.

   _Note: The provided source materials mark "hard rock", 10 as correct, but based on the code (deleting index 1 from ["hard rock", 10, 1.2]) the actual result would be ["hard rock", 1.2]. This discrepancy exists in the original document._

5. **If A is a list, what does the following syntax do?** `B=A[:]`
   - [ ] B gets a transposed form of list A
   - [ ] Assigns list A to list B
   - [ ] List A gets converted to a set and is loaded into B
   - [x] Creates a new reference variable B that points to a copy or clone of the original list A

   **Answer:** The slice notation [:] creates a new copy of all elements, making B independent from future changes to A.

6. **A researcher analyzes demographic data stored in a tuple:** `demographics = ("Female", 35, "PhD", "Engineering", "Urban")`. **To validate the data structure, the researcher needs to confirm how many characteristics are stored for each participant. Which code will provide this information?**
   - [ ] `sum(demographics)`
   - [ ] `count(demographics)`
   - [ ] `demographics.size()`
   - [x] `len(demographics)`

   **Answer:** The len function determines the number of elements in the tuple, recording the total number of demographic characteristics.

7. **A music streaming service stores album release years in a dictionary:** `album_years = {"Thriller":"1982", "Back in Black":"1980", "The Dark Side of the Moon":"1973"}`. **When generating a "Years in Music" report, which elements from this dictionary should be extracted?**
   - [x] "1982", "1980", "1973"
   - [ ] "Thriller", "Back in Black", "The Dark Side of the Moon"
   - [ ] The dictionary structure itself
   - [ ] Both the album names and years together

   **Answer:** These elements are the values in the dictionary, representing the years when each album was released.

8. **The variable release_year_dict is a Python dictionary. What is the outcome of applying the following method?** `release_year_dict.values()`
   - [ ] Changes the dictionary to a list
   - [ ] Retrieves the keys of the dictionary
   - [x] Retrieves the values of the dictionary
   - [ ] Retrieves the entire contents of the dictionary

   **Answer:** The values() method returns a view object containing all values from the dictionary.

9. **A data analyst is tracking unique website visitors. The current visitors set is** `visitors = {'user123', 'user456'}`. **A new visitor with ID 'user789' visits the site. What will the visitors set contain after executing** `visitors.add('user789')`**?**
   - [ ] {'user123', 'user456', 'user789', 'user789'}
   - [ ] {'user123', 'user456'}
   - [ ] Error
   - [x] {'user789', 'user123', 'user456'}

   **Answer:** The add method includes the new visitor ID in the set while maintaining the set of unique visitors.

10. **What is the outcome of the following?** `'1' in {'1','2'}`
    - [ ] -9
    - [x] True
    - [ ] 3
    - [ ] False

    **Answer:** The in operator checks if an element exists within a set and returns True when the element is found.
