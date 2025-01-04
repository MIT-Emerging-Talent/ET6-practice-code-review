"""
This module implements a simple calculator that can perform basic arithmetic operations
such as addition, subtraction, multiplication, and division.

It takes two numbers and the desired operation, performs the operation, and returns the result.
"""


def calculate(num1, num2, operation):
    """
    Performs basic arithmetic operations (addition, subtraction, multiplication, division)
    on two numbers based on the specified operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float: The result of the operation.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(
            "Invalid operation. Choose from 'add', 'subtract', 'multiply', 'divide'."
        )


# Test the function in this script:
if __name__ == "__main__":
    result = calculate(10, 5, "add")
    print(f"Result of addition: {result}")
