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
def prime_finder(start: int, end: int) -> list[int]:
    """Returns a list of primes from a range of 2 integers

    Parameters:
      start (int): The start of the range (inclusive)
      end (int): The end of the range (inclusive)

    Returns:
      list[int]: a list of all the primes between the two integers

    Raises:
      AssertionError
        - If start and end are not integers
      ValueError:
        - If either element is negative
        - If end is smaller than start

    >>> prime_finder(1,5)
    [2,3,5]

    >>> prime_finder(2,10)
    [2,3,5,7]

    >>> prime_finder(7,2)
    ValueError

    >>> prime_finder('cat','dog')
    AssertionError
    """

    # check if start and end are integers
    assert isinstance(start, int) and isinstance(
        end, int
    ), "Both start and end must be integers"

    # check if start and end are positive
    if start < 0 or end < 0:
        raise ValueError("Integers must be positive")

    # check if start is smaller than end
    if start > end:
        raise ValueError(
            "The start of the range must be smaller than or equal to the end"
        )

    # initialize the list of primes
    primes = []

    # iterate through the range of numbers
    for num in range(start, end + 1):
        # check if the number is prime
        if num > 1:
            for factor in range(2, round(num**0.5) + 1):
                if (num % factor) == 0:
                    break
            else:
                primes.append(num)

    return primes
