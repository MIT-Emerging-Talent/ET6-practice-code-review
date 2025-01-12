"""
A  module for multiplying two integers.

Modul contents:
     -multiply_two_numbers: A fnuction to multiply two integers.
created  2025-01-04
@author: Manezhah Mohmand
"""


def multiply_two_numbers(a: int, b: int) -> int:
    """Multiplies two integers and returns the product.

    parameters:
     a (int): The  first integer
     b (int):The second  integer

     Returns:
     int: The product of the two integers

     Raises:
         TypeError:If the input contains non-integer elements.
    Examples:
    >>> multiply_two_numbers(2, 3)
    6
    """
    return a * b
