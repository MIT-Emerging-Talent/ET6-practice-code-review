#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This module provides a function to determine the length of a given string.
The implementation uses Python's built-in capabilities while adding
type checking and input validation.

Created on Jan 05, 2025.
Team Number: 28
Team Name: MIT Alpha
@author: Nada Hamza
"""

def string_length(s: str) -> int:
    """Calculates and returns the total number of characters in the input string.
    
    Args:
        s (str): The input string to measure.
        Must be a valid string object, cannot be None.
        
    Returns:
        int: The number of characters in the string.
        Always non-negative.
        
    Raises:
    TypeError: If input is not a string
    ValueError: If input is None.
        
    Examples:
    >>> string_length("")
    0
    >>> string_length("Hello")
    5
    >>> string_length("1234")
    4
    >>> string_length("Test string")
    11
    >>> string_length("Python!")
    7

    """
    # Validate input type
    if s is None:
        raise ValueError("Input string cannot be None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Return the length of the string
    return len(s)
