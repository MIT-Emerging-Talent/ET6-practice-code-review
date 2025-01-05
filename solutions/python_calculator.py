"""
Module: python_calculator

This module contains a single function `calculate` that performs basic mathematical operations
(addition, subtraction, multiplication, and division) based on the provided operator.
"""

from typing import Union


def calculate(
    a: Union[int, float], b: Union[int, float], operator: str
) -> Union[int, float]:
    """
    Perform a basic mathematical operation on two numbers based on the operator provided.

    Args:
        a (int | float): The first operand.
        b (int | float): The second operand.
        operator (str): The operator specifying the operation. Must be one of: '+', '-', '*', '/'.

    Returns:
        int | float: The result of the operation.

    Raises:
        ValueError: If the operator is not one of the allowed operations.
        ZeroDivisionError: If the operator is '/' and the second operand is zero.

    Examples:
        >>> calculate(2, 3, '+')
        5
        >>> calculate(10, 4, '-')
        6
        >>> calculate(6, 3, '*')
        18
        >>> calculate(9, 3, '/')
        3.0
    """
    # Defensive assertions
    if not isinstance(a, (int, float)):
        raise TypeError("The first operand (a) must be an integer or a float.")
    if not isinstance(b, (int, float)):
        raise TypeError("The second operand (b) must be an integer or a float.")
    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Operator must be one of '+', '-', '*', '/'.")

    if operator == "/" and b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    # Perform the operation
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
