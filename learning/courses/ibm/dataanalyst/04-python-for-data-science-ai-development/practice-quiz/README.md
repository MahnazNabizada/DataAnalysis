# Practice Quiz - Questions and Answers

## Module 1 - Types

1. **What is the data type of the entity 43?**
   - [x] int
   - [ ] float
   - [ ] bool
   - [ ] complex

   Anwer: Correct! Int or integer types are numbers that contain no decimals. They can be positive or negative.

2. **What data type does 3.12323 represent?**
   - [ ] bool
   - [ ] int
   - [x] float
   - [ ] str

   Answer: Correct! As the number contains decimal values, it belongs to the category of floating-point numbers.

3. **What is the result of the following: `int(3.99)`?**
   - [x] 3
   - [ ] 3.99
   - [ ] 4

   Answer: Correct! When a number is a typecast, only the integral part is retained, discarding the fractional part.

## Module 1 - Expressions and Variables

1. **What is the result of the operation: `11//2`**
   - [x] 5
   - [ ] 5.5
   - [ ] 11/2
   - [ ] 0.18

   Answer: Correct! The // symbol represents integer division, removing decimal values.

2. **What is the value of x after the following is run:**

   ```python
   x = 4
   x = x/2
   ```

   - [x] 2.0
   - [ ] 0.5
   - [ ] 1.0
   - [ ] 4.0

   Answer: Correct! The first expression assigns a value to a variable, while the second expression modifies the same variable. The result is in float because division in python using '/' returns a float.

3. **Which line of code will perform the action as required for implementing the following equation?**

   ```python
   y = 2x^2 - 3
   ```

   - [ ] `y = 2x*x – 3`
   - [x] `y = 2*x*x – 3`
   - [ ] `y = 2x/2 – 3`
   - [ ] `y = 2*x*2 – 3`

   Answer: Correct! Valid implementation. In python x\*x is used to represent the expression x^2

## Module 1 - String Operations

1. **What is the result of the following?** `Name[-1]`

   ![Image of the string Michael Jackson represented in array](./images/i1.png)
   - [ ] "n"
   - [ ] "i"
   - [ ] "M"
   - [x] "o"

   **Answer:** The index having a value of -1 denotes the final position within a cyclic sequence.

2. **What is the result of the following?** `print("AB\nC\nDE")`
   - [ ] AB CD E
   - [ ] ABC DE
   - [x] AB / C / DE
   - [ ] AB\nC\nDE

   **Answer:** When the `print` function comes across the `\n` character, it displays a new line.

3. **What is the output of the following?** `"helloMike".find("Mike")`
   - [ ] 6
   - [x] 5
   - [ ] 6,7,8
   - [ ] 2

   **Answer:** The method helps you locate the position of the first character in a given string that matches the first character of a specified substring.

## Module 2 - Lists and Tuples

1. **Consider the following tuple:**

   ```python
      say_what = ('say', 'what', 'you', 'will')
   ```

   **What is the result of the following?** `say_what[-1]`
   - [ ] 'what!'
   - [ ] say_what '
   - [x] 'will'
   - [ ] 'you!'

   **Answer:** An index of −1 corresponds to the last item of a tuple, such as the string 'will'.

2. **Consider the following tuple** `A = (1, 2, 3, 4, 5)`. **What is the outcome of the following?** `A[1:4]`
   - [x] (2, 3, 4)
   - [ ] (1, 2, 3, 4)
   - [ ] (3, 4, 5)
   - [ ] (2, 3, 4, 5)

   **Answer:** The indexes 1, 2, and 3 of the tuple correspond to these elements.

3. **Consider the following list** `B = [1, 2, [3, 'a'], [4, 'b']]`. **What is the result of** `B[3][1]`**?**
   - [ ] 2
   - [x] 'b'
   - [ ] [4, 'b']
   - [ ] 'a'

   **Answer:** The list that follows relates to the index of nested list B[3].

4. **What is the outcome of the following operation?**

   ```python
      [1, 2, 3] + [1, 1, 1]
   ```

   - [ ] [1, 2, 3; 1, 1, 1]
   - [x] [1, 2, 3, 1, 1, 1]
   - [ ] TypeError
   - [ ] [2, 3, 4]

   **Answer:** The addition operator combines lists through concatenation.

5. **What will be the length of the list A after executing the following code:**

   ```python
      A = [1]
      A.append([2, 3, 4, 5])
   ```

   - [ ] 10
   - [x] 2
   - [ ] 5
   - [ ] 6

   **Answer:** Append adds the entire list [2, 3, 4, 5] as a single element.
