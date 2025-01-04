"""
A module for reversing the digits of an integer number.

@author: Raed Eleyan.
@date: 01/04/2025.
"""

def reversed_positive_number(number: int) -> int:
    """
    Reverses the digits of a givin positive integer.

    :param number: the integer to be reversed. Must be non-negative.
    :return: the reversed integer.
    :raises ValueError: If the number is negative.
    :raises AssertionError: If the argument isn't a number.
    >>> reversed_positive_number(123)
    321
    >>> reversed_positive_number(0)
    0
    >>> reversed_positive_number(100)
    1
    """
    assert isinstance(number, int), 'The argument must be an integer.'
    if number < 0:
        raise ValueError('The input integer is negative.')
    return int(str(number)[::-1])
