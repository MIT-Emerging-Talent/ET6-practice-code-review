#!/usr/bin/env python3
# -- coding: utf-8 --
def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the result.

    Args:
        a (float): The first number to be multiplied. 
        Must be a real number (no specific range constraints).
        b (float): The second number to be multiplied. 
        Must be a real number (no specific range constraints).

    Returns:
        float: The product of the two input numbers.

    Raises:
        TypeError: If either `a` or `b` is not a number.

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(-1.5, 2)
        -3.0
        >>> multiply(0, 5)
        0
    """
    if not isinstance(a, (int, float)):
        raise TypeError("The first argument must be a number.")
    if not isinstance(b, (int, float)):
        raise TypeError("The second argument must be a number.")
    
    return a * b
