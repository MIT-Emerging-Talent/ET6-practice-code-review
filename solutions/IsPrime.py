#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding if an integer is prime.

Module contents:
    - IsPrime: finds if an integer is prime.

Created on XX XX XX
@author: Mohammed Elfadil
"""


def IsPrime(a: int) -> str:
    """Checks if an integer is prime.
    Parameter:
        a: int
    Return -> str: whether a is prime or not
    Raises:
        AssertionError: if the argument is not an integer
    >>> IsPrime(0)
    not prime
    >>> IsPrime(1)
    not prime
    >>> IsPrime(2)
    prime
    >>> IsPrime(4)
    not prime
    >>> IsPrime(7)
    prime
    >>> IsPrime(2.5)
    invalid input
    """
    if not isinstance(a, int):
        return "invalid input"
    if a < 2:
        return "not prime"
    for i in range(2, a):
        if a % i == 0:
            return "not prime"
    return "prime"
