#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A module containing a function to determine if a number is odd or even.
Module contents:
odd_or_even: Determines if a number is odd or even.

Created on 2025-01-03
Author: Solara Hamza
    """
def odd_or_even(number: int) -> str:
    """Determines if a number is odd or even.
    This function takes a number as input and returns whether the number is odd or even.
    
    Parameters:
        number: int, the number to determine if it is odd or even.
    
    Returns -> str: 'odd' if the number is odd, 'even' if the number is even.
    
    Examples:
        >>> odd_or_even(1)
        'odd'
        >>> odd_or_even(2)
        'even'
        >>> odd_or_even(3)
        'odd'
        >>> odd_or_even(4)
        'even'
    """
    if number % 2 == 0:
        return 'even'
    return 'odd'