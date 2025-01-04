"""

This module provides a function to reverse the digits of an integer.

Author: Raed Eleyan.
Date: 01/04/2025
"""

def reversed_number(number: int) -> int:
    """
    Reverses the digits of a given non-negative integer.

    :param number: The integer to be reversed.
    :return: The reversed integer.
    :raises ValueError: If the number is negative.
    Doctests:
        >>> reversed_number(123)
        321
        >>> reversed_number(0)
        0
        >>> reversed_number(100)
        1

    Assumptions:
    - The input integer is non-negative.
    - The function removes leading zeros in the reversed number.
    """
    if number < 0:
        raise ValueError('The input integer is negative.')
    number_to_string = str(number)
    reverse_string = number_to_string[::-1]
    return int(reverse_string)
