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
