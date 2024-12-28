#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for explaining FizzBuzz functionality.

This module includes the function fizzbuzz(n) that returns:
- 'Fizz' for numbers divisible by 3.
- 'Buzz' for numbers divisible by 5.
- 'FizzBuzz' for numbers divisible by both 3 and 5.
- The number itself as a string for all other cases.


"""

def fizz_buzz(n: int) -> str :
    """
    Returns 'Fizz' for multiples of 3, 'Buzz' for multiples of 5,
    'FizzBuzz' for multiples of both 3 and 5, and the number itself for others.
    
    parameters:
        n (int): The number to evaluate.
        
    Returns:
        str: 'Fizz', 'Buzz', 'FizzBuzz', or the string representation of the number.
    >>> fizzbuzz(15)
    FizzBuzz
    >>> fizzbuzz(5)
    Buzz
    >>> fizzbuzz(7)
    7
    >>> fizzbuzz(3)
    Fizz

    """
    assert isinstance(n, int), "Input must be an integer"
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
