#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the sum of the digits of an integer number

Module contents:
    - sum_of_digits: calculate the sum of the digits of an integer number .

Created on 25 Dec 2024
@author: Noorelsalam Almakki
"""

def sum_of_digits(number: int) -> int:
    """The sum_of_digits function takes an integer number and returns the sum of 
    its digits.

    Parameters: 
        - number (int): any integer number.
        
    Returns:
        - sum (int): the sum of the digits of the input number.

    Raises:
        - AssertionError: if the input number is not an integer.
            
    Example:
    >>> sum_of_digits(123)
    6

    >>> sum_of_digits(123456)
    21

    >>> sum_of_digits(-123)
    -6
    """
    sum = 0
    
    for digit in str(number):
        sum += int(digit)
    
    return sum
