"""
list_operations.py

This module contains a function `sum_of_squares` that calculates the sum of the squares
of all integers in a list. Non-integer elements are ignored.

The function:
- Handles empty lists gracefully.
- Excludes non-integer elements from calculations.
- Works with both positive and negative integers.

Created on 11 1 2025
@author: momtaz-yaqubi
"""


def sum_of_squares(input_list):
    """
    Computes the sum of squares of all integers in the input list.

    Args:
        input_list (list): A list of elements.

    Returns:
        int: The sum of the squares of integers in the list.
    """
    return sum(x**2 for x in input_list if isinstance(x, int))
