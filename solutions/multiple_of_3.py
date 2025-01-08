"""
multiple_of_3.py

This module contains the implementation of the multiple_of_3 function where the function returns multiples of 3 for values under or equal to 15

"""


def multiple_of_3(start: int) -> list:
    """
    Returns the multiples of 3 in a list starting from a start amount provided

    parameter:
        an integer

    Returns:
        multiples of 3 less than or equal to 15

    Raises:
    AssertionError
        If the input 'start' is not an integer.

    Example:
    >>> multiple_of_3(3)
    [3, 6, 9, 12, 15]

    >>> multiple_of_3(-3)
    [-3, 0, 3, 6, 9, 12, 15]

    >>> multiple_of_3(0)
    [0, 3, 6, 9, 12, 15]

    >>> multiple_of_3(15)
    [15]

    """
    assert isinstance(start, int)  # raises assertionerror when input is not integer

    result = []  # List to store the multiples of 3

    number = start  # Start from the given number

    while number <= 15:  # Keep going until 15
        result.append(number)  # Add the number to the list
        number += 3  # Move to the next multiple of 3
    return result  # Return the list
