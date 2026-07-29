# Final Exam

1.  **In Python, what can be either a positive or negative number but lacks a decimal point?**
    - [ ] str
    - [ ] complex
    - [ ] float
    - [x] int

    **Answer:** Integer data type can have positive or negative values but no decimal points.

2.  **What purpose does the Python find() method serve?**
    - [ ] The method finds every second index of a substring.
    - [ ] The method finds the ending index of a substring.
    - [ ] The method finds the length of a substring.
    - [x] The method finds the starting index of a substring.

    **Answer:** The find() method locates the starting index of a substring.

3.  **What following code segment would produce an output of “0”?**
    - [ ] 1/2
    - [ ] 2//1
    - [x] 1//2
    - [ ] 2/1

    **Answer:** Double slash `//` will return the integral part of the result.

4.  **Complete the statement. Dictionary items can be:**
    - [x] Numerous data types
    - [ ] Stored in duplicate keys
    - [ ] A collection of strings only
    - [ ] Only one data type

    **Answer:** Dictionaries can be a collection of different data types stored with unique keys.

5.  **In a list or tuple, what does the index of "1" represent?**
    - [ ] The first element
    - [ ] The last element
    - [ ] The third element
    - [x] The second element

    **Answer:** Index 1 refers to the second element of a list or tuple.

6.  **What line of code would produce this output: ['1','2','3','4']?**
    - [ ] `'1,2,3,4'.join(',')`
    - [ ] `'1,2,3,4'.reverse(',')`
    - [ ] `'1,2,3,4'.split(':')`
    - [x] `'1,2,3,4'.split(',')`

    **Answer:** The split() method breaks the string into a list of strings based on the chosen delimiter.

7.  **If A is a list, what happens with this segment of code: a=set(A)?**
    - [ ] It returns an ordered list.
    - [x] It casts the list “A” to the set “a”
    - [ ] It casts the list “a” to the set “A”
    - [ ] It returns an error

    **Answer:** This statement will convert a list to a set.

8.  **What will be the output if x=7?**

    ```python
    if(x!=1):
        print('Hi')
    else:
        print('Hello')

    print('Mike')
    ```

    - [ ] Mike
    - [ ] Hello
    - [x] Hi \n Mike
    - [ ] Hello \n Mike

    **Answer:** The code executes the if clause along with the statement printing `Mike`.

9.  **What is the process of forcing your program to output a pre-decided error message when it encounters an issue?**
    - [ ] Force out
    - [x] Exception handling
    - [ ] Output errors
    - [ ] Error messages

    **Answer:** Exception handling enables the program to take the required steps when an exception (error) happens during execution.

10. **Which of the following `add` functions would return ‘11’?**
    - [x]

      ```python
      def add(x):
         return(x+x)
      add('1')
      ```

    - [ ]

      ```python
      def add(x):
          return(x + x + x)

      add(1)
      ```

    - [ ]

      ```python
      def add(x):
          return(x+x)

      add(1)
      ```

    - [ ]

      ```python
      def add(x):
          return(x + x + x)

      add('1')
      ```

    **Answer:** Addition of two strings will lead to concatenation.

11. **What code segment would output the following? _2_**
    - [ ]

    ```python
    for i in range(1,5):
        if (i!=1):
            print(i)
    ```

    - [ ]

    ```python
    for i in range(1,5):
        if (i!=2):
            print(i)
    ```

    - [x]

    ```pyhton
    for i in range(1,5):
        if (i==2):
            print(i)
    ```

    - [ ]

    ```python
    for i in range(0,5):
        if (i!=1):
            print(i)
    ```

    **Answer:** Answer: The conditional statement inside the loop filters only the value 2.

12. **Consider the class Rectangle, what are the data attributes?**

    ```python
    class Rectangle(object):

            def __init__(self,width=2,height=3,color='r'):
                self.height = height
                self.width = width
                self.color = color

            def drawRectangle(self):
                import matplotlib.pyplot as plt
                plt.gca().add_patch(
                    plt.Rectangle((0, 0), self.width, self.height, fc=self.color)
                )
                plt.axis('scaled')
                plt.show()
    ```

    - [x] self.height, self.width, self.color
    - [ ] drawRectangle
    - [ ] init
    - [ ] import matplotlib

    **Answer:** Data attributes are the variables of the class.

13. **Complete the statement. You cannot sort a list if it contains:**
    - [ ] only same Case strings
    - [x] strings and numeric values
    - [ ] only numeric values
    - [ ] concatenated strings

    **Answer:** You cannot sort numerical values and string values together.

14. **What outcome do the following lines of code produce?**

    ```python
    a=np.array([0,1,0,1,0])

    b=np.array([1,0,1,0,1])

    a/b
    ```

    - [ ] array([1, 1, 1, 1, 1])
    - [ ] array([0.1, 1.0, 0.1, 1.0, 0.1])
    - [x] Division by zero error
    - [ ] array([0, 0, 0, 0, 0])

    **Answer:** Correct! Arrays divide element by element, resulting in divide by 0 errors for the numbers at Index 1 and Index 3.

15. **What outcome do the following lines of code produce?**

    ```python
    a=np.array([1,1,1,1,1])

    a+1
    ```

    - [ ] array([1,1,1,1,1])
    - [ ] array([0,0,0,0,0])
    - [x] array([2,2,2,2,2])
    - [ ] array([11, 11, 11, 11, 11])

    **Answer:** Each element of the array has the constant added to it.

16. **What does the following line of code select along with the headers ‘Artist’, ‘Length’, ‘Year’ and ‘Genre’ from the dataframe df?**

    ```python
        y=df[['Artist','Length','Genre']]
    ```

    - [ ] The specified Rows
    - [ ] The specified column headers only.
    - [ ] The entire dataframe
    - [x] The specified Columns

    **Answer:** The double brackets select the columns of a dataframe.

17. **What is the method readline() used for?**
    - [ ] It always reads the first line from the text file.
    - [ ] It reads 10 lines of a file at a time.
    - [ ] It reads the entire file all at once.
    - [x] It helps to read one complete line from a given text file.

    **Answer:** The readline() method helps to read one complete line from a given text file.

18. **What mode will write text at the end of the existing text in a file?**
    - [ ] Read binary “rb”
    - [ ] Write “w”
    - [x] Append “a”
    - [ ] Read “r”

    **Answer:** Append mode adds data to an existing version of the file, if any.

19. **What are the three main parts to a URL?**
    - [x] Scheme, internet address, and route
    - [ ] Block, post, and route
    - [ ] Get, post, and scheme
    - [ ] Put, route, and get

    **Answer:** These are the three main parts of a URL.

20. **Which of the following Python libraries are not commonly used while performing web scraping?**
    - [ ] Requests
    - [x] Numpy
    - [ ] BeautifulSoup
    - [ ] Pandas

    **Answer:** Numpy is useful for numerical operations and is not commonly used in web scraping.
