"""
A module for summing the digits of an integer number.

@author: Raed Eleyan.
@date: 01/04/2025.
"""

def sum_digits_of_positive_number(number: int) -> int:
    """
    Sum the digits of an integer number.

    :param number: the integer number to sum its digits.
    :return: the sum of the digits of an integer number.
    :raises ValueError: If the number is negative.
    :raises AssertionError: If the argument isn't a number.
    >>> sum_digits_of_positive_number(11)
    2
    >>> sum_digits_of_positive_number(1234)
    10
    >>> sum_digits_of_positive_number(222)
    6
    """
    assert isinstance(number, int), "The argument must be an integer."
    if number < 0:
        raise ValueError("The input integer is negative.")
    return sum(int(digit) for digit in str(number))