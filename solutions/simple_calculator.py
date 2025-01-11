#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for performing multiplication, division, summation, or subtraction
operations between two numbers.

Created on 5/1/2024
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)

Module contents:
    - simple_calculator: performs basic operations on two integers .

"""


def simple_calculator(operation: str, operand1: int, operand2: int):
    """
    Performs simple arithmetic operations on two input integers passed to it.
    Parameters:
        operation (str): this is the type of operation we want to perform
                        it should be ('+', '-', '*', or '/')
        operand1 (int): the first number we want to perform the operation on
        operand2 (int): the second number we want
        to perform the operation on, should'nt be zero in division


    Returns-> int or float: the result of the operation on the
                two numbers rounded to three digits if it is a fraction.



    Raises:
    TypeError: if operation isn't a string
    TypeError: if any of the operands is not an integer
    ZeroDivisionError: If the second argument in division is zero
    ValueError: if the operation is not supported


    >>> simple_calculator('+', 3, 8)
    11

    >>> simple_calculator('-', 8, 7)
    1

    >>> simple_calculator('/', 7, 2)
    3.5
    """
    # Ensure inputs are correct
    if not isinstance(operation, str):
        raise TypeError("operation must be a string")
    if not isinstance(operand1, int) or not isinstance(operand2, int):
        raise TypeError("operands must be integers")

    # Handle the operations
    if operation == "+":
        return operand1 + operand2

    elif operation == "-":
        return operand1 - operand2

    elif operation == "*":
        return operand1 * operand2

    elif operation == "/":
        # We can't divide by zero
        if operand2 == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return round(operand1 / operand2, 3)

    # Unsupported operations raise an error
    else:
        raise ValueError(f"Unsupported operation: {operation}")
