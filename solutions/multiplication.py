#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for multiplying two numbers.
Module contents:
    - multiply_numbers: Multiplies two numbers and returns the product.
"""


def multiply_numbers(num1, num2):
    """Returns the product of two numbers.
    Takes two numbers (integers or floats) and returns their product.
    The output type will match the input types (i.e., if both inputs are integers,
    the output will be an integer; if both are floats, the output will be a float).
    If the inputs are not both integers or floats, an AssertionError is raised.
    Parameters:
        num1: int or float, the first number to multiply
        num2: int or float, the second number to multiply
    Returns -> int or float: the product of num1 and num2
    Raises:
        AssertionError: if inputs are not both int or float
    Examples:
        >>> multiply_numbers(5, 3)
        15
        >>> multiply_numbers(4.5, 2.0)
        9.0
        >>> multiply_numbers(-7, 6)
        -42
    """
    assert isinstance(num1, (int, float)), "num1 must be an int or float"
    assert isinstance(num2, (int, float)), "num2 must be an int or float"
    return num1 * num2
