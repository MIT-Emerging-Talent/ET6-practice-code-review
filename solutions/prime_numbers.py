#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A module that determines whether a given number is a prime number.

Module contents:
    - is_prime: checks if the given number is a prime number.

created on 04/01/2025
@author: Alaa Mohamed

"""


def is_prime(N: int) -> bool:
    """
    Checks if the given number is a prime number.
    A number is considered prime if it's only divisible by one and itself.


    Parameters:
        N: input must be an integer.

    Returns -> bool: True if the number is prime, False otherwise.

    Raises:
        AssertionError: if the inout is not an integer.

    Examples:
    >>> is_prime("1")
    False
    >>> is_prime("2")
    True
    >>> is_prime("3")
    True
    """
    assert isinstance(N, int), "input must be an integer"

    if N <= 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
        return True


number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
