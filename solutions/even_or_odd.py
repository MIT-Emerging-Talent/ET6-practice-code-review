#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This module provides a function that determines if a number is even or odd

Module contents:
  - even_or_odd: returns a string indicating if a number is even or odd

Created on 2025/08/06
@author: ZaidMazen1
"""


# defining the function
def even_or_odd(num: int) -> str:
    """Returns a string indicating if a number is even or odd

    Parameters:
      num (int): The number to be checked

    Returns:
      str: "Even" if the number is even, "Odd" if the number is odd

    Raises:
      AssertionError
        - If num is not an integer
        - If num is a list

    >>> even_or_odd(2)
    "Even"

    >>> even_or_odd(3)
    "Odd"

    >>> even_or_odd(0)
    "Even"

    >>> even_or_odd(-2)
    "Even"

    >>> even_or_odd(-3)
    "Odd"
    """

    # check if num is an integer
    assert isinstance(num, int), "The input must be an integer"

    # check if the number is even
    if num % 2 == 0:
        return "Even"
    # check if the number is odd
    else:
        return "Odd"
