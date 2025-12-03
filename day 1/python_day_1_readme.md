# Python Learning Day 1

This document provides a structured, professional guide for learning Python fundamentals, core data structures, advanced concepts, OOP, and hands-on problem-solving. It includes explanations and practical exercises to ensure active learning.

---

## Python Fundamentals

### Variables
- Variables store data values.
- Python uses dynamic typing.
- Naming rules: must start with a letter or underscore; case-sensitive.

**Exercise:**
1. Create variables for your name, age, height, and whether you are a student.
2. Print all variables in a formatted sentence.

---

### Data Types
- int, float, str
- bool
- list, tuple, dict, set
- NoneType

**Exercise:**
1. Declare one variable of each data type and print its type using `type()`.

---

### Loops (for, while)
- Use loops to iterate over sequences or repeat actions.

**Exercise:**
1. Write a `for` loop that prints numbers 1 to 20.
2. Write a `while` loop that counts down from 10 to 1.

---

### Conditionals
- Use `if`, `elif`, and `else`.

**Exercise:**
1. Write a program that asks for a number and prints whether it is positive, negative, or zero.

---

### Functions
- Functions allow reuse and organization of code.

**Exercise:**
1. Create a function that greets a user by name.
2. Create a function that returns the square of a number.

---

## Hands-on Mini Programs (10 Programs)

### FizzBuzz
Print numbers 1 to 100, but:
- If divisible by 3: print Fizz
- If divisible by 5: print Buzz
- If divisible by both: print FizzBuzz

### Prime Check
Write a function that checks if a number is prime.

### Factorial
Compute factorial using both loop and recursion.

### Sorting Without Built-in Sort
Implement bubble sort manually.

### Reverse String
Take a string and reverse it manually.

### Word Frequency Counter
Given a sentence, count how many times each word appears.

### Sum of Digits
Input a number and compute the sum of its digits.

### Max/Min Manually
Find max and min in a list without using built-ins.

### Pattern Printing
Print patterns such as:
```
*
**
***
****
```

### Palindrome Check
Check if a string reads the same forward and backward.

---

## Core Data Structures in Python

### Lists
- Indexing, slicing
- List comprehension

**Exercise:**
1. Create a list of numbers 1 to 10.
2. Use slicing to get first 3 elements.
3. Create a list comprehension that squares each number.

### Dictionaries
- CRUD operations: Create, Read, Update, Delete

**Exercise:**
1. Create a dictionary with three users and their ages.
2. Add a new key.
3. Update one value.
4. Delete a key.

### Tuples and Sets
- Tuples: immutable sequences
- Sets: unique unordered elements

**Exercise:**
1. Convert a list with duplicates into a set.

### JSON Parsing
Use the `json` module to parse JSON.

**Exercise:**
1. Load JSON data into a dict.
2. Filter values based on a condition.

---

## Python Advanced Concepts

### File I/O
- Use `open()` to read and write files.

**Exercise:**
1. Write three lines to a text file.
2. Read the file and print contents.

### Exception Handling
- Use `try`, `except`, `finally`.

**Exercise:**
1. Handle invalid input from a user.

### Modules and Packages
- Import modules
- Create your own module

**Exercise:**
1. Create a module with a simple function and import it.

### __name__ == "__main__"
- Ensures certain code runs only when the script is executed directly.

### Virtual Environments
Brief introduction to `venv`.

---

## Project: Password Manager (CLI)

### Requirements
- Master password prompt
- Store credentials in JSON
- Add, view, and delete passwords
- Optional basic encryption

### Components
- PasswordManager class
- Methods:
  - add_password()
  - view_passwords()
  - delete_password()
- Error handling
- JSON persistence

---

## Object-Oriented Programming

### Concepts
- Classes and objects
- Methods and constructors
- Inheritance
- Encapsulation
- Polymorphism

**Exercises:**
1. Create a `Car` class and extend it to `ElectricCar`.
2. Create `Animal`, then subclasses `Dog` and `Cat`.
3. Create a `BankAccount` class with deposit and withdrawal.
4. Create an `Employee` class with a raise method.

---

## LeetCode Arrays and Strings Practice
Recommended problems:
- Two Sum
- Best Time to Buy and Sell Stock
- Contains Duplicate
- Valid Anagram
- Valid Palindrome
- Move Zeroes
- Remove Duplicates from Sorted Array
- Merge Sorted Array
- Longest Common Prefix
- Plus One

Goal: Solve 10 to 12 problems.

---

End of document.

