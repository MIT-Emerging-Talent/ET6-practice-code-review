#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This module provides a function that returns a list of all primes
within a given range

Module contents:
  - prime_finder: returns a list of all primes from a list of 2 integers

Created on 2025/01/06
@author: ZaidMazen1
"""


# defining the function
def prime_finder(a: int, b: int) -> list[int]:
    """Returns a list of primes from a range of 2 integers

    Parameters:
      a (int): The start of the range (inclusive)
      b (int): The end of the range (inclusive)

    Returns:
      list[int]: a list of all the primes between the two integers

    Raises:
      AssertionError
        - If a and b are not integers
      ValueError:
        - If either element is negative
        - If b is smaller than a

    >>> prime_finder(1,5)
    [2,3,5]

    >>> prime_finder(2,10)
    [2,3,5,7]

    >>> prime_finder(7,2)
    ValueError

    >>> prime_finder('cat','dog')
    AssertionError
    """

    # check if a and b are integers
    assert isinstance(a, int) and isinstance(b, int), "Both a and b must be integers"

    # check if a and b are positive
    if a < 0 or b < 0:
        raise ValueError("Integers must be positive")

    # check if a is smaller than b
    if a > b:
        raise ValueError("The first integer must be smaller than the second input")

    # initialize the list of primes
    primes = []

    # iterate through the range of numbers
    for num in range(a, b + 1):
        # check if the number is prime
        if num > 1:
            for factor in range(2, round(num**0.5) + 1):
                if (num % factor) == 0:
                    break
            else:
                primes.append(num)

    return primes
