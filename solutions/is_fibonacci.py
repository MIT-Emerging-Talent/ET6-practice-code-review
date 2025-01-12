"""
A module that that generates an arithmetic progression (AP).

Module contents:
  - generate_arithmetic_progression generates an arithmetic progression

Created on 01/09/2025
@author: Anik Kumar Adhikary
"""

import math


def is_fibonacci_number(n: int) -> bool:
    """
    Checks whether a given number is a Fibonacci number.

    A number is a Fibonacci number if and only if one or both of
    (5 * n^2 + 4) or (5 * n^2 - 4) is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a Fibonacci number, False otherwise.
    """
    if n < 0:
        return False

    def is_perfect_square(x: int) -> bool:
        s = int(math.sqrt(x))
        return s * s == x

    # Check both conditions
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
