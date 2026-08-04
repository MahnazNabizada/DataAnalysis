# Assessment 4: Python for Data Science, AI & Development, with Goals

**Final Grade:** 140 / 140

## 1. Which of the following is not a core data type? — ✅ 1/1

- Lists
- Dictionary
- Tuples
- **✅ Correct: Class**

---

## 2. What data type is the object below? — ✅ 1/1

```python
L = [1, 23, 'hello', 1]
```

- **✅ Correct: List**
- Dictionary
- Tuple
- Array

---

## 3. Which of the following function convert a string to a float in python? — ✅ 1/1

- `int(x [,base])`
- `long(x[,base])`
- **✅ Correct: `float(x)`**
- `str(x)`

---

## 4. What will be the output of the following Python code snippet? — ✅ 1/1

```python
print('The sum of {0} and {1} is {2}'.format(2, 10, 12))
```

- **✅ Correct: The sum of 2 and 10 is 12**
- Error
- The sum of 0 and 1 is 2
- None of the mentioned

---

## 5. What is the return type of function id? — ✅ 1/1

- **✅ Correct: int**
- float
- bool
- dict

---

## 6. What error occurs when you execute the following Python code snippet? — ✅ 1/1

```python
apple = mango
```

- SyntaxError
- **✅ Correct: NameError**
- ValueError
- TypeError

---

## 7. In python we do not specify types, it is directly interpreted by the compiler, so consider the following operation to be performed: — ✅ 1/1

```python
>>> x = 13 ? 2
```

**Objective is to make sure x has an integer value, select all that apply (python 3.xx)**

- `x = 13 // 2`
- `x = int(13 / 2)`
- `x = 13 % 2`
- **✅ Correct: All of the above**

---

## 8. In order to store values in terms of key and value we use what core data type? — ✅ 1/1

- list
- tuple
- class
- **✅ Correct: dictionary**

---

## 9. Which of the following is a Python tuple? — ✅ 1/1

- [1, 2, 3]
- **✅ Correct: (1, 2, 3)**
- {1, 2, 3}
- {}

---

## 10. What type of data is: `a=[(1,1),(2,4),(3,9)]`? — ✅ 1/1

- Array of tuples
- **✅ Correct: List of tuples**
- Tuples of lists
- Invalid type

---

## 11. Tuples can't be made keys of a dictionary. — ✅ 1/1

- True
- **✅ Correct: False**

---

## 12. Suppose `d = {"john":40, "peter":45}`, what happens when we try to retrieve a value using the expression `d["susan"]`? — ✅ 1/1

- Since "susan" is not a value in the set, Python raises a KeyError exception
- It is executed fine and no exception is raised, and it returns None
- **✅ Correct: Since "susan" is not a key in the set, Python raises a KeyError exception**
- Since "susan" is not a key in the set, Python raises a syntax error

---

## 13. Which of these about a dictionary is false? — ✅ 1/1

- The values of a dictionary can be accessed using keys
- **✅ Correct: The keys of a dictionary can be accessed using values**
- Dictionaries aren't ordered
- Dictionaries are mutable

---

## 14. Which of the statements about dictionary values is false? — ✅ 1/1

- More than one key can have the same value
- The values of the dictionary can be accessed as `dict[key]`
- **✅ Correct: Values of a dictionary must be unique**
- Values of a dictionary can be a mixture of letters and numbers

---

## 15. Which of these about a set is not true? — ✅ 1/1

- Mutable data type
- Does not allow duplicate values
- Data type with unordered values
- **✅ Correct: Immutable data type**

---

## 16. Which of the following is not the correct syntax for creating a set? — ✅ 1/1

- **✅ Correct: `set([[1,2],[3,4]])`**
- `set([1,2,2,3,4])`
- `set((1,2,3,4))`
- `{1,2,3,4}`

---

## 17. Which of the following statements is used to create an empty set? — ✅ 0/1

- `{ }`
- **✅ Correct: `set()`**
- `[ ]`
- `( )`

---

## 18. What will be the output of the following Python code? — ✅ 1/1

```python
a = [5,5,6,7,7,7]
b = set(a)
def test(lst):
    if lst in b:
        return 1
    else:
        return 0
for i in filter(test, a):
    print(i,end=" ")
```

- 5 5 6
- 5 6 7
- **✅ Correct: 5 5 6 7 7 7**
- 5 6 7 7 7

---

## 19. If `a={5,6,7}`, what happens when `a.add(5)` is executed? — ✅ 1/1

- a={5,5,6,7}
- **✅ Correct: a={5,6,7}**
- Error as there is no add function for set data type
- Error as 5 already exists in the set

---

## 20. Which of the following statements create a dictionary? — ✅ 1/1

- `d = {}`
- `d = {"john":40, "peter":45}`
- `d = {40:"john", 45:"peter"}`
- **✅ Correct: All of the above**

---

## 21. Mathematical operations can be performed on a string. — ✅ 1/1

- True
- **✅ Correct: False**

---

## 22. Which of following uses the correct syntax for a python if statement? Choose all that apply — ✅ 1/1

- `if (x = y):` — 0%
- **✅ Correct: `if (x == y):` — 50%**
- `if !(x is not y):` — 0%
- `if x = y:` — 0%
- **✅ Correct: `if x == y:` — 50%**

---

## 23. Which of the following properly expresses the precedence of operators (using parentheses) in the following expression: `10 > y or x + y == 10 and x is not y`? — ❌ 0/1

- `(((10 > y) or (x + y == 10)) and (x is not y))` _(selected — incorrect)_
- `(10 > (y or x) + y == (10 and x) is not y)`
- `(10 > y or x + y == 10 and x is not y)`
- **✅ Correct: `((10 > y) or (((x + y) == 10) and (x is not y)))`**
- `(((10 > y) or ((x + y) == 10)) and (x is not y))`

---

## 24. Which of the following is the use of function in python? — ✅ 1/1

- **✅ Correct: Functions are reusable pieces of programs**
- Functions don't provide better modularity for your application
- you can't also create your own functions
- All of the above

---

## 25. What will be the output of the following Python code? — ✅ 1/1

```python
x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is now', x)
```

- **✅ Correct:**
  ```
  x is 50
  Changed local x to 2
  x is now 50
  ```
- ```
  x is 50
  Changed local x to 2
  x is now 2
  ```
- ```
  x is 50
  Changed local x to 2
  x is now 100
  ```
- None of the above

---

## 26. What are the two main types of functions? — ✅ 1/1

- Custom function
- **✅ Correct: Built-in function & User defined function**
- User function
- System Function

---

## 27. Which of the following can be used to open a file called myText.txt in write-only mode? — ✅ 1/1

- `outfile = open("myText.txt", w)`
- `outfile = open("myText.txt", "write")`
- **✅ Correct: `outfile = open("myText.txt", "w")`**
- `outfile = open("myText.txt")`

---

## 28. Which command below closes the already open file myText.txt if the following code has already been written? — ✅ 1/1

```python
ref_file = open("myText.txt", "r")
```

- `close()`
- **✅ Correct: `ref_file.close()`**
- `close(ref_file)`
- `close("myText")`

---

## 29. Which of the commands below is used to add the following string to the end of a file object filevar? — ✅ 1/1

```python
somestring = "my Sentence"
```

- `filevar.append(somestring)`
- `filevar.write("somestring")`
- **✅ Correct: `filevar.write(somestring)`**
- `somestring.write()`

---

## 30. The contents of names.txt is listed here: — ✅ 1/1

```
Moana
Cinderella
Tiana
```

**Which of the following code blocks will print all of the names in names.txt?**

- ```python
  names = open("names.txt", "r")
  for line in names:
      print(names)
  ```
- **✅ Correct:**
  ```python
  names = open("names.txt", "r")
  for line in names:
      print(line)
  ```
- ```python
  names = open("names.txt", "r")
  for line in names:
      print("line")
  ```
- None of the above

---

## 31. How many errors are in the code below? It should open the file in read-only mode, read each line and print each line and then close the file. — ✅ 1/1

```python
def print_contents(file)
    file_obj = open(file)
    for line in "file_obj":
        print(line_obj)
```

- 1
- 2
- 3
- **✅ Correct: 4**

---

## 32. **\_** represents an entity in the real world with its identity and behaviour. — ✅ 1/1

- A method
- **✅ Correct: An object**
- A class
- An operator

---

## 33. What will be the output of the following Python code? — ✅ 1/1

```python
class test:
    def __init__(self,a):
        self.a=a
    def display(self):
        print(self.a)
obj=test()
obj.display()
```

- Runs normally, doesn't display anything
- Displays 0, which is the automatic default value
- **✅ Correct: Error as one argument is required while creating the object**
- Error as display function requires additional argument

---

## 34. Which of the following Python code creates an empty class? — ✅ 1/1

- ```python
  class A:
      return
  ```
- **✅ Correct:**
  ```python
  class A:
      pass
  ```
- `class A:`
- It is not possible to create an empty class

---

## 35. Which of the following thing can be data in Pandas? — ✅ 10/10

- a python dict
- an ndarray
- a scalar value
- **✅ Correct: All of the above**

---

## 36. Point out the wrong statement. — ✅ 10/10

- **✅ Correct: A DataFrame is like a fixed-size dict in that you can get and set values by index label**
- Series can be passed into most NumPy methods expecting an ndarray
- A key difference between Series and ndarray is that operations between Series automatically align the data based on label
- None of the above

---

## 37. Series is a one-dimensional labeled array capable of holding any data type. — ✅ 10/10

- **✅ Correct: True**
- False

---

## 38. Which of the following operation works with the same syntax as the analogous dict operations? — ✅ 10/10

- Getting columns
- Setting columns
- Deleting columns
- **✅ Correct: All of the above**

---

## 39. The **\_\_\_\_** function returns its argument with a modified shape, whereas the **\_\_\_\_** method modifies the array itself. — ✅ 1/1

- **✅ Correct: reshape, resize**
- resize, reshape
- reshape2, resize
- All of the above

---

## 40. To create sequences of numbers, NumPy provides a function \***\*\_\_\*\*** analogous to range that returns arrays instead of lists. — ✅ 1/1

- **✅ Correct: arange**
- aspace
- aline
- All of the above

---

## 41. Which of the following method creates a new array object that looks at the same data? — ✅ 10/10

- **✅ Correct: view**
- copy
- paste
- All of the above

---

## 42. Which of the following returns an array of ones with the same shape and type as a given array? — ✅ 10/10

- all_like
- **✅ Correct: ones_like**
- one_alike
- All of the above

---

## 43. Point out the wrong statement. — ✅ 1/1

- Each universal function takes array inputs and produces array outputs
- Broadcasting is used throughout NumPy to decide how to handle disparately shaped arrays
- **✅ Correct: The output of the ufunc is necessarily an ndarray, if all input arguments are ndarrays**
- All of the above

---

## 44. In the process of fetching a web page from a server the HTTP request/response takes \***\*\_\_\*\*** RTTs. — ✅ 10/10

- 2
- **✅ Correct: 1**
- 4
- 3

---

## 45. The \***\*\_\_\*\*** method when used in the method field, leaves entity body empty. — ✅ 10/10

- POST
- SEND
- **✅ Correct: GET**
- PUT

---

## 46. The HTTP response message leaves out the requested object when \***\*\_\_\_\_\*\*** method is used. — ✅ 10/10

- GET
- POST
- **✅ Correct: HEAD**
- PUT

---

## 47. Which of the following is present in both an HTTP request line and a status line? — ✅ 10/10

- **✅ Correct: HTTP version number**
- URL
- Method
- None of the above

---

## 48. The default connection type used by HTTP is \***\*\_\*\*** — ✅ 10/10

- **✅ Correct: Persistent**
- Non-persistent
- Can be either persistent or non-persistent depending on connection request
- None of the above

---

## 49. The time taken by a packet to travel from client to server and then back to the client is — ✅ 1/1

- STT
- **✅ RTT**
- PTT
- JTT

## 50. The HTTP response message leaves out the requested object when \***\*\_\_\_\_\*\*** method is used. — ✅ 10/10

- GET
- **✅ Correct: HEAD**
- POST
- PUT
