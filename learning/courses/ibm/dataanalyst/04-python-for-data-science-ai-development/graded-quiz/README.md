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

## Module 4 - Working with Data in Python

1. **In a machine learning algorithm, two feature vectors are represented as NumPy arrays:** `a=np.array([-1,1])` **and** `b=np.array([1,1])`. **What will be returned when calculating** `np.dot(a,b)`**?**
   - [ ] array([0,2])
   - [x] 0
   - [ ] array([[-1, -1], [1, 1]])
   - [ ] 1

   **Answer:** The dot product of these vectors performs element-wise multiplication, then addition: (-1×1) + (1×1) = -1 + 1 = 0.

2. **What does the following code calculate in NumPy:** `np.dot(A.T, B)`**?**
   - [ ] Element-wise multiplication of the transpose of A and B
   - [ ] The dot product of the diagonal elements
   - [x] It performs matrix multiplication between the transposed version of A and matrix B
   - [ ] The sum of all elements in both matrices

   **Answer:** The .T attribute transposes matrix A before performing matrix multiplication with B.

3. **What does the shape attribute tell you about a NumPy array?**
   - [ ] It returns the total number of elements in the array.
   - [ ] It returns the memory allocated for the array.
   - [ ] It returns the data type of the array elements.
   - [x] It returns a tuple indicating the size of the array in each dimension.

   **Answer:** The shape attribute provides the array's dimensions as a tuple of integers.

4. **What happens when you multiply a NumPy array by a scalar value?**
   - [ ] Only the first row is multiplied by the scalar
   - [x] Each element in the array is multiplied by the scalar value
   - [ ] Only the diagonal elements are multiplied by the scalar
   - [ ] The scalar becomes a new dimension in the array

   **Answer:** When multiplying an array by a scalar, the operation is applied to every element in the array.

5. **Given the following file content for "Example1.txt":**
   This is line 1
   This is line 2
   This is line 3

   **What would be the output of this code?**

   ```python
      with open("Example1.txt","r") as file1:
         FileContent = file1.readline()
         print(FileContent)
   ```

   - [x] This is line 1
   - [ ] This
   - [ ] Empty output
   - [ ] This is line 1 This is line 2 This is line 3

   **Answer:** The readline() method reads only the first line of the file.

6. **Consider the following line of code:**

   ```python
      with open(example1,"r") as file1:
   ```

   **What mode is the file object in?**
   - [ ] append
   - [ ] write
   - [x] read
   - [ ] binary

   **Answer:** The mode is set to "r" for read.

7. **How can you write multiple lines to a file at once using a list?**
   - [ ] Convert the list to a string first
   - [ ] Use the insert() method to place lines in the file
   - [x] Use a for loop to iterate through the list, writing each element with write()
   - [ ] Use the print() function with a file parameter

   **Answer:** You can iterate through a list and write each element to the file.

8. **What task do the following lines of code accomplish?**

   ```python
      with open('Example2.txt','r') as readfile:
         with open('Example3.txt','w') as writefile:
            for line in readfile:
                  writefile.write(line)
   ```

   - [x] Copying the text from Example2.txt to Example3.txt
   - [ ] Checking the mode of the open function for each file object
   - [ ] Printing out the content of Example2.txt
   - [ ] Reading the content of Example2.txt

   **Answer:** This is the expected outcome.

9. **Using the loc method, how would you access the second row of a DataFrame's column named "artist"?**
   - [ ] `df.artist[1]`
   - [ ] `df.loc[2, 'artist']`
   - [ ] `df.loc['artist', 1]`
   - [x] `df.loc[1, 'artist']`

   **Answer:** The loc method uses row index and column labels to access data.

10. **What function would you use to load a CSV file in Pandas?**
    - [x] `pd.read_csv(path)`
    - [ ] `np.read_csv(path)`
    - [ ] `pd.read_excel(path)`
    - [ ] `pd.load_csv(path)`

    **Answer:** The read_csv method will read the CSV file in Pandas.

## Module 5 - APIs and Data Collection

1. **A web developer is troubleshooting an HTTP response with a status code of 404. What does this indicate about the client’s request?**
   - [x] The requested resource could not be found on the server
   - [ ] The server encountered an internal error while processing the request
   - [ ] The client lacks proper authentication to access the resource
   - [ ] The request was successful, and the resource was retrieved

   **Answer:** The 404 status code means “Not Found” and indicates that the server cannot find the requested resource.

2. **What is the relationship between parent and child elements in an HTML document tree used in BeautifulSoup?**
   - [ ] Child elements must always be of the same type as their parent elements
   - [x] Child elements are nested within parent elements, allowing navigation up and down the tree
   - [ ] Parent elements can only be accessed after all child elements are processed
   - [ ] Parent elements can only contain a maximum of three child elements

   **Answer:** BeautifulSoup represents HTML as a tree where nested tags become children of their containing tags.

3. **A programmer is extracting cryptocurrency data using the PyCoinGecko API. When receiving the response, what format conversion is needed to work with the data as a Python dictionary?**
   - [ ] Apply the csv() method to the response object
   - [x] Apply the json() method to the response object
   - [ ] Apply the xml() method to the response object
   - [ ] Apply the text attribute to the response object

   **Answer:** The json() method converts the JSON response to a Python dictionary that can be easily manipulated.

4. **When working with time series data, what is the purpose of pandas’ to_datetime function?**
   - [x] To convert timestamps into standard datetime objects for easier analysis and visualization
   - [ ] To compare dates across multiple datasets
   - [ ] To filter out non-business days from financial data
   - [ ] To extract only the date portion from datetime objects

   **Answer:** The to_datetime function standardizes time data, enabling proper sorting, filtering, and display of time-based information.

5. **A web developer is creating an HTML table showing quarterly sales results. How should they structure the HTML to display this tabular data properly?**
   - [x] Use a `<table>` tag with `<tr>` tags for rows and `<td>` tags for cells
   - [ ] Use a `<form>` tag with `<input>` tags for each cell
   - [ ] Use a `<div>` tag with `<span>` tags for each data point
   - [ ] Use a `<p>` tag with `<br>` tags between each row

   **Answer:** This structure creates proper HTML tables where `<tr>` defines rows and `<td>` defines individual cells within each row.

6. **What is the difference between GET and POST HTTP methods when making requests?**
   - [ ] GET requests can send files while POST requests cannot
   - [ ] GET requests use JSON while POST requests use XML
   - [x] GET requests include data in the URL, while POST requests send data in the request body
   - [ ] GET requests are asynchronous, while POST requests are synchronous

   **Answer:** This fundamental difference affects how data is transmitted and the visibility of parameters.

7. **What distinguishes REST APIs from other types of APIs?**
   - [ ] They are restricted to local communication within a single application
   - [ ] They can only be implemented in Python
   - [x] They communicate through the internet using HTTP methods and typically exchange data in formats like JSON
   - [ ] They require specialized hardware to function

   **Answer:** REST (Representational State Transfer) APIs use web protocols for communication between clients and servers.

8. **What Python library would you use to parse XML files?**
   - [ ] pandas.xml
   - [ ] beautifulsoup.xml
   - [ ] json.parser
   - [x] xml.etree

   **Answer:** `xml.etree` is a Python library module used to parse and work with XML files.

9. **A developer is creating an application that needs to retrieve data from a REST API. Which code snippet correctly sends a GET request with parameters?**
   - [ ] `import requests; r = requests.get('https://api.example.com/data?name=John&ID=123', data={'secure': True})`
   - [x] `import requests; payload = {'name': 'John', 'ID': '123'}; r = requests.get('https://api.example.com/data', params=payload)`
   - [ ] `import requests; r = requests.post('https://api.example.com/data', headers={'name': 'John', 'ID': '123'})`
   - [ ] `import requests; r = requests.get('https://api.example.com/data', json={'name': 'John', 'ID': '123'})`

   **Answer:** This properly formats a GET request with query parameters using the `params` argument.

10. **A data scientist needs to extract player statistics from an NBA website. After obtaining the HTML, what BeautifulSoup method would help locate all table rows containing player data?**
    - [ ] `soup.search('players')` to find player information
    - [ ] `soup.extract('statistics')` to pull out statistical data
    - [x] `soup.find_all('tr')` to identify all table rows
    - [ ] `soup.read_table()` to automatically process the table

    **Answer:** The `find_all` method returns all instances of the specified tag, allowing further processing of each row.
