#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 03 01 2024

@author: Norbert Ndayisenga
"""

def count_consonants(s: str) -> int:
    """Counts the number of consonants in a given string.

    Parameters:
        s: str, the input string

    Returns:
        int: the number of consonants in the string

    >>> count_consonants("Hello, World!")
    7

    >>> count_consonants("123@#$")
    0

    >>> count_consonants("bcdfghjklmnpqrstvwxyz")
    21
    """
    # Ensure input is a string
    assert isinstance(s, str), "Input must be a string"

    # Define consonants
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    # Count consonants in the string
    return sum(1 for char in s.lower() if char in consonants)
