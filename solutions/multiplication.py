"""
A module for multiplying multiple numbers.

@author: Rama Arafeh.
@date: 7/Jan/2025.
"""


def multiplication(first_num: int, sec_num: int, third_num: int) -> int:
    """
    multiplies multiple integer numbers.

    :param first_num: the first integer number.
    :param sec_num: the second integer number.
    :param third_num: the third integer number.
    :return: the multiplication result.
    :raises AssertionError: If the argument isn't a number.
    >>> multiplication(1,2,3)
    6
    >>> multiplication(10,20,30)
    6000
    >>> multiplication(1,-2,-3)
    6
    """
    assert isinstance(first_num, int), "The first number must be an integer."
    assert isinstance(sec_num, int), "The second number must be an integer."
    assert isinstance(third_num, int), "The third number must be an integer."
    result = first_num * sec_num * third_num
    return result
