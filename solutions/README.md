# Solutions

---

## **Solutions Summary**

| **Solution File**          | **Description**                        | **Author**|
|----------------------------|---------------------------------------|-----------|
|`add_binary.py`         |Add binary strings and return result.       |Said  |
|`bubble_sort.py`        |performing bubble sort on an array          |Tomas |
|`caesar_encryption.py`  |encrypting using caesar's cypher            |Caser |
|`convert_temperature.py`|Convert Celsius to Fahrenheit and Kelvin    |Amro  |
|`count_vowels.py`       |counting vowels in a string                 |Aseel |
|`fizz_buzz.py`          |Check divisibility with FizzBuzz logic      |Nada  |
|`happy_number.py`       |Check if a number is happy                  |Omina |
|`insertion_sort.py`     |Perform insertion sort on an array          |Tomas |
|`majority_element.py`   | Find majority element in an array          |Aseel |
|`palindrome_checker.py` |Check if a string is palindrome             |Ceaser|
|`percentage_letter.py`  |Calculate percentage of specific character  |Heba  |
|`reverse_integer.py`    |Reverse digits of a signed integer          |Said  |
|`reverse_string.py`     |Reverse strings using a utility function    |Nada  |
|`search_insert_position.py`|Find position to insert a value             |Omaina|
|`steps_to_floor.py`     |Calculate steps to reach a floor            |Amro  |
|`two_sum.py`            |Solve the two-sum problem                   |Heba  |

---

## How to Update

Whenever a new solution is added, ensure to:

1. **Add the Solution File**: Place your solution directly in the `solutions` folder,
following the naming convention: `solution_name.py`.
2. **Update the Summary**: Add an entry for your solution in the
3. "Solutions Summary" section, including:
   - File name.
   - Brief description.
   - Author name.
4. **Write Tests**: Add a corresponding test file in the `tests` folder using the
naming convention: `test_solution_name.py`.

---

## How to Use the Solutions Folder

### Add a Solution

1. **File Structure**:  
   - Place your solution in the `solutions` folder.
   - Include proper Python docstrings describing:
     - The file's purpose.
     - Author and project details.
     - Function-level docstrings explaining parameters, return values, and examples.
   - Adhere to Python best practices for clean and readable code.

2. **Write Corresponding Tests**:  
   - Add a test file for your solution in the `tests` folder.
   - Use the naming convention: `test_solution_name.py`.
   - Write comprehensive test cases covering normal, and error scenarios.

3. **Submit Your Work**:  
   - Submit a pull request including:
     - Solution file.
     - Corresponding test file.
     - Updates to this README file.
   - Ensure all tests pass before requesting a review.

---

## Python Docstring Guidelines

Each solution file should include proper Python docstrings for
better understanding and maintainability.
Below is a recommended format:

### Module-Level Docstring

- Briefly describe the file's purpose.
- List the author, date .
- Summarize the functions or classes in the module.

### Function-Level Docstring

- Describe the function’s purpose.
- Include:
  - **Parameters** and their types.
  - **Return value** and its type.
  - Any exceptions raised.
  - A usage example .

---

### Example Solution File: `add_numbers.py`

```python
"""
multiply_numbers.py

This module provides a function to multiply two numbers.

Author: [Your Name]
Date: [Date]   


Functions:
- multiply_numbers(a, b): Multiplies two numbers and returns the result.
"""

def multiply_numbers(a, b):
    """
    Multiply two numbers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    - int or float: The product of the two numbers.

    Example:
    >>> multiply_numbers(4, 2)
    8
    """
    return a * b
