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

## Module 3 - Python Programming Fundamentals

1. **A traffic management system uses the following code to control pedestrian crossing signals:**

   ```python
      signal_state = "Red"
      if signal_state == "Green":
         print("Walk")
      else:
         print("Wait")
      print("Look both ways")
   ```

   **What message will pedestrians see on the display?**
   - [ ] Walk / Look both ways
   - [ ] Walk / Wait
   - [x] Wait / Look both ways
   - [ ] Look both ways

   **Answer:** Since the signal_state is "Red" and not "Green," the else clause executes first, followed by the unconditional print statement.

2. **A temperature monitoring system uses the following code to check if a reading exceeds a threshold:**

   ```python
      current_temp = 18
      current_temp = current_temp > 25
   ```

   **What value will be stored in current_temp after these lines execute?**
   - [ ] 18
   - [ ] True
   - [ ] 25
   - [x] False

   **Answer:** The comparison 18 > 25 evaluates to False, which becomes the new value stored in the current_temp variable.

3. **A file download progress tracker uses the following code to show the percentage remaining:**

   ```python
      remaining_percent = 100
      while remaining_percent > 25:
         print(f"{remaining_percent}% remaining")
         remaining_percent = remaining_percent - 25
   ```

   **What will be displayed to the user during this download?**
   - [x] 100% remaining / 75% remaining / 50% remaining
   - [ ] 100% remaining / 75% remaining / 50% remaining / 25% remaining
   - [ ] 100% remaining / 75% remaining / 50% remaining / 25% remaining / 0% remaining
   - [ ] 100% remaining

   **Answer:** The loop tracks download progress and prints each percentage until it drops to 25% or below, showing only these three values.

4. **A graphics application uses a class to represent screen coordinates. What will be displayed when the following code runs?**

   ```python
      class Coordinate(object):
         def __init__(self, x, y):
            self.x = x
            self.y = y
         def display(self):
            print(f"Position: ({self.x}, {self.y})")
      cursor = Coordinate(15, 30)
      cursor.display()
   ```

   - [ ] (15, 30)
   - [ ] Position: (x, y)
   - [x] Position: (15, 30)
   - [ ] Coordinate(15, 30)

   **Answer:** The display method shows the position using the numeric values that were passed when creating the coordinate object.

5. **A museum curator is labeling artifacts using Python. The following code processes a list of ancient items:**

   ```python
      items = ["Vase", "Statue", "Mask"]
      for index, item in enumerate(items, start=1):
         print(f"Exhibit {index}: {item} - Ancient Greece")
   ```

   **What will be displayed on the museum labels?**
   - [x] Exhibit 1: Vase - Ancient Greece / Exhibit 2: Statue - Ancient Greece / Exhibit 3: Mask - Ancient Greece
   - [ ] Exhibit Vase: 1 - Ancient Greece / Exhibit Statue: 2 - Ancient Greece / Exhibit Mask: 3 - Ancient Greece
   - [ ] Vase - Ancient Greece / Statue - Ancient Greece / Mask - Ancient Greece
   - [ ] Exhibit 0: Vase - Ancient Greece / Exhibit 1: Statue - Ancient Greece / Exhibit 2: Mask - Ancient Greece

   **Answer:** The enumerate function with start=1 begins counting from 1 instead of 0, creating sequential exhibit numbers for each item.

6. **What is the result of running the following lines of code?**

   ```python
      class Points(object):
         def __init__(self, x, y):
            self.x = x
            self.y = y
         def print_point(self):
            print('x=', self.x, ' y=', self.y)
      p2 = Points('Boston', 'Chicago')
      p2.y = 'Denver'
      p2.print_point()
   ```

   - [ ] x= Boston y= Chicago
   - [ ] x= Denver y= Denver
   - [ ] x= Denver y= Boston
   - [x] x= Boston y= Denver

   **Answer:** The attribute y was changed to 'Denver' before the print_point method was called, resulting in the modified output.

7. **Given the conditional function delta, under what circumstances does this function evaluate unity?**

   ```python
      def delta(x):
         if x == 0:
            y = 1
         else:
            y = 0
         return y
   ```

   - [ ] When the parameter represents any non-zero value
   - [ ] Under no computational conditions
   - [ ] When the argument equals unity
   - [x] When the parameter equals zero

   **Answer:** The function evaluates unity when the input parameter satisfies the zero-equality condition.

8. **What is the output of the following line of code?**

   ```python
      a = 1
      def do(x):
         a = 100
         return x + a
      print(do(1))
   ```

   - [ ] 102
   - [ ] 2
   - [x] 101
   - [ ] 1

   **Answer:** The function uses the local variable a=100 within its scope, ignoring the global variable a=1, and adds it to the parameter value.

9. **Which function definition demonstrates the most efficient implementation for adding two numbers?**
   - [ ] Intermediate variable assignment before return
   - [x] Direct return of parameter summation
   - [ ] Built-in sum function with tuple conversion
   - [ ] Built-in sum function with individual parameters

   **Answer:** This implementation returns the arithmetic sum of two parameters, demonstrating optimal efficiency through minimal computational overhead.

10. **What constitutes the primary rationale for implementing granular exception handling with explicitly typed catch blocks?**
    - [ ] To ensure complete program termination upon error occurrence
    - [ ] Explicit exception typing provides no operational benefit
    - [ ] To enable selective code segment bypassing during execution
    - [x] To identify precise exception classification and source location

    **Answer:** Granular except statements enable accurate identification of exception types and facilitate targeted error responses, enhancing debugging capabilities and exception management precision.

## Module 4 - Reading and Writing Files with Open

1. **What are the most commonly used modes when opening a file?**
   - [ ] (a)ppend, (r)edline, (w)rite
   - [x] (a)ppend, (r)ead, (w)rite
   - [ ] (s)ave, (r)ead, (w)rite
   - [ ] (a)ppend, (c)lose, (w)rite

   **Answer:** (a)ppend, (r)ead, (w)rite are the three modes of operation.

2. **Which data attribute retrieves the file's title?**
   - [ ] `file1.close()`
   - [ ] `file1.open()`
   - [ ] `file1.mode`
   - [x] `file1.name`

   **Answer:** The name attribute returns the filename.

3. **Which command instructs Python to initiate a new line?**
   - [x] `\n`
   - [ ] `\b`
   - [ ] `\q`
   - [ ] `\e`

   **Answer:** In Python `\n` instructs the code to begin a new line.

4. **Which method is used to write data into a file in Python?**
   - [ ] `file1.close()`
   - [ ] `file1.read()`
   - [x] `file1.write()`
   - [ ] `file1.open()`

   **Answer:** The "write" method writes data into a file.
