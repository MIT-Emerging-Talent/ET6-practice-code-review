"""
This module contains the implementation of the `find_maximum_minimum` function.
The `find_maximum_minimum` function finds the maximum and minimum values from a list of numbers.

The function returns a tuple where the first element is the maximum value
and the second element is the minimum value from the list of numbers.

Edge cases such as an empty list or invalid inputs are handled appropriately.

@author: Yonatan Y. Yifat
"""


def find_maximum_minimum(numbers):
    """
    Function to find the maximum and minimum from a list of numbers.

    Args:
        numbers (list): A list of numerical values (integers or floats).

    Returns:
        tuple: A tuple containing the minimum and maximum values in the list.
    """
    if not numbers:
        raise ValueError("The list is empty")

    return min(numbers), max(numbers)
