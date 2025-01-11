# **Solutions Folder Overview**

The **Solutions** folder contains implementations of coding challenges completed
by our group. Each solution file directly addresses a specific challenge,
while corresponding test files are maintained in the `tests` folder.

---

## **Folder Structure**

    └── solutions
        ├── README.md
        ├── __init__.py
        └── tests
            ├── README.md
            └── __init__.py

---

## **Solutions Summary**

| **Solution File**       | **Description**                   | **Author**|
|--------------------------|--------------------------------------------------------------|-------------------|
| `calculate_average.py`| Calculates the average of a list of numbers | Clement |
| `spiral_traverse.py` | Traverses a 2D matrix in spiral order | Fahed |
| `euler_totient.py` | Computes Euler's totient function (ϕ(n))| Fahed |
| `direction_to_degree.py` | Convert a cardinal direction to degree | Obay |
| `check_odd_or_even.py` | Checks if a number is odd or even | Clement |
| `grading_system.py`| Assigning letter grade to a numeric score.  | Razan |
| `kronecker_product.py` | Computes the Kronecker ⊗ product of 2 matrices | Fahed|
| `feet_to_meters.py` | Converting feet to meters| Obay |
| `volts_to_amperes.py` | Converting volts to amperes| Obay |
| `miles_to_kilometers.py` | Converting miles to kilometers| Obay |
| `greatest_number.py` | Finding greatest number in a list| Razan |

---

## **How to Update**

Whenever a new solution is added, the author (or a designated person) should
update the "Solutions Summary" section with a brief description of the new solution.
This keeps the README.md file comprehensive and useful for all group members

## **How to Use the Solutions Folder**

1. **Add a Solution**
   - Place your solution directly in the **solutions** folder,
   - following the naming convention: `solution_name.py`.
   - Ensure your solution file includes:
     - A Python docstring at the top describing: file's purpose, author, date & group.
     - Function-level DOCstrings explaining parameters, return values, and examples.
     - Clear and concise code adhering to Python best practices.

2. **Write Corresponding Tests**
   - Add a test file for your solution in the `tests` folder.
   - Use the naming convention: `test_solution_name.py`.
   - Write comprehensive test cases covering normal, edge, and error scenarios.

3. **Document Your Work**
   - Include a section in the **solutions/README.md** file briefly
   - summarizing the solution and its purpose.

4. **Submit Your Work**
   - Submit a pull request for your solution and its corresponding test file.
   - Ensure all tests pass before requesting a review.

---

## **Python Docstring Guidelines**

Each solution file should include proper Python DOCstrings
for better understanding and maintainability. Here's the recommended format:

### **Module-Level Docstring**

- Briefly describe the file's purpose.
- List the author, date, and group/project details.
- Provide a summary of the functions or classes in the module.

### **Function-Level Docstring**

- Describe the function’s purpose.
- Include:
  - Parameters and their types.
  - Return value and its type.
  - Any exceptions raised.
  - A usage example (optional but helpful).

---

## **Example Solution File: `add_numbers.py`**

    """
    add_numbers.py

    This module provides a function to add two numbers.

    Author: [Your Name]
    Date: [Date]
    Group: ET6-foundations-group-16

    Functions:
    - add_numbers(a, b): Adds two numbers and returns the result.
    """

    def add_numbers(a, b):
        """
        Add two numbers.

        Parameters:
        - a (int or float): The first number.
        - b (int or float): The second number.

        Returns:
        - int or float: The sum of the two numbers.

        Example:
        >>> add_numbers(3, 5)
        8
        """
        return a + b


    if __name__ == "__main__":
        # Example usage
        print("Example: add_numbers(3, 5) =", add_numbers(3, 5))
