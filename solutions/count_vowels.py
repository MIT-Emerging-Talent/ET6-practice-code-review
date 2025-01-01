#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting vowels in a string.

Module contents:
    - count_vowels: counts the number of vowels in a string.

Created on XX XX XX
@author: Saliha Kalender
"""

def count_vowels(input_string):
    """
    Counts the number of vowels in a given string.

    Behavior Description:
    - The function identifies all vowels (a, e, i, o, u) in the input string, regardless of case.
    - It returns the total count of vowels found.

    Parameter Description:
    - input_string (str): The string to be processed. It can contain letters, numbers, spaces, and special characters.

    Return Value Description:
    - int: The total number of vowels in the input string.

    Assumptions:
    - Input is always a string.
    - Vowels are defined as 'a', 'e', 'i', 'o', 'u', both uppercase and lowercase.

    Doctests:
    >>> count_vowels("hello")
    2
    >>> count_vowels("HELLO")
    2
    >>> count_vowels("123 abc XYZ")
    1

    Assertions:
    - Asserts that the input is of type str.

    Use Cases:
    1. Counting vowels in a user-provided string input.
    2. Processing text data to analyze vowel frequency.
    """
    assert isinstance(input_string, str), "Input must be a string."

    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count

# Example usage:
if __name__ == "__main__":
    example1 = "Programming is fun!"
    example2 = "AEIOUaeiou"

    print(f"Vowels in '{example1}': {count_vowels(example1)}")  # Output: 5
    print(f"Vowels in '{example2}': {count_vowels(example2)}")  # Output: 10
