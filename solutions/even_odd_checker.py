"""
Author: @msrak
Created on: January 8, 2024.
"""


def check_even_or_odd(number):
    """
    The check_even_or_odd function takes a number
    as input and determines whether it is even or odd.
    It returns a string indicating the result.

    PARAMETERS:
    number (int): The number to be checked for even or odd.

    RETURN VALUES:
    str: "even" if the number is divisible by 2, "odd" if it is not.
    """
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
