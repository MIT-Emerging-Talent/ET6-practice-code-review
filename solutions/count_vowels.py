#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the <description of the behavior of the function>

Module contents:
    - <function name>: <description of the behavior of the function>.

Created on <date created>
@author: <Your Name>
"""
    """
    Counts the number of vowels in a given string.

    Args:
        input_string (str): The string to analyze for vowels.

    Returns:
        int: The total number of vowels (a, e, i, o, u) in the string,
             including both uppercase and lowercase vowels.

    Example:
        >>> count_vowels("Hello, World!")
        3
        >>> count_vowels("Python")
        1
    """
    vowels = "aeiouAEIOU"  # List of vowels (both uppercase and lowercase)
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count


# Example usage
if __name__ == "__main__":
    input_string = "Hello, how many vowels are here?"
    print("Number of vowels:", count_vowels(input_string))
