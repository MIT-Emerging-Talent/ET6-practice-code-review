#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
A module for counting vowels in a given string.

Module contents:
    - count_vowels: A function to count the number of vowels in a string (case-insensitive).

Created on 2026-07-01
Author: Rumiya Ismatova
"""


def count_vowels(text: str) -> int:
    """
    Count_vowels function takes a string and count
    all upper and lower case vowels.

    Arguments:
    text (str): The input string to check for vowels. This string can
                contain alphabetic characters.


    Input:
    text[str]: The input string to check for vowels. This string may
                contain alphabetic characters.

    Return:
    num[int]: the number of vowels in text
            The total count of vowels (a, e, i, o, u) in the input string.
            Both uppercase and lowercase vowels are counted, and
            non-alphabetic characters are ignored.
            Returns 0 if no vowels are found.

    >>> count_vowels("")
    0

    >>> count_vowels("0")
    0

    >>> count_vowels("what")
    1

    >>> count_vowels("Hello")
    2

    >>> count_vowels("Austria")
    4

    >>> count_vowels("Hello, World!")
    3
    """

    if not text:  # Handle empty strings
        return 0

    vowels = {"a", "e", "i", "o", "u", "y"}
    count = 0

    for char in text:
        if char.lower() in vowels:
            count += 1

    # Defensive assertion for input validation
    assert isinstance(text, str), "Input should be a string"

    list_vowels = ["a", "e", "i", "o", "u", "y"]
    count = sum(1 for char in text if char.lower() in list_vowels)
    return count
=======
A module for counting vowels in a string.

Module contents:
    - count_vowels: counts the number of vowels in a string.

Created on 01 01 2025
@author: Saliha Kalender
"""


def count_vowels(input_string: str) -> int:
    """
    Counts the number of vowels in a given string.

    Behavior Description:
    - The function identifies all vowels (a, e, i, o, u) in the input string,
    regardless of case.
    - It returns the total count of vowels found.

    Parameter Description:
    - input_string (str): The string to be processed.
      It can contain letters, numbers, spaces, and special characters.

    Return Value Description:
    - int: The total number of vowels in the input string.

    Assumptions:
    - Input is always a string.
    - Vowels are defined as 'a', 'e', 'i', 'o', 'u', both uppercase and lowercase.

    Raises:
    - AssertionError: If the input is not of type str.

    Doctests:
    >>> count_vowels("hello")
    2
    >>> count_vowels("HELLO")
    2
    >>> count_vowels("123 abc XYZ")
    1

    Use Cases:
    1. Counting vowels in a user-provided string input.
    2. Processing text data to analyze vowel frequency.
    """
    assert isinstance(input_string, str), "Input must be a string."

    vowels = (
        "aeiouAEIOU"  # A string containing all vowels (both uppercase and lowercase).
    )
    count = sum(
        1 for char in input_string if char in vowels
    )  # Counts how many characters in the input are vowels.
    return count


if __name__ == "__main__":
    # This block ensures the following code is executed only when this script
    # is run directly (not when imported as a module in another script).
    # It provides a simple demonstration of the `count_vowels` function.
    print(count_vowels("Programming is fun!"))  # Output: 5
    print(count_vowels("AEIOUaeiou"))  # Output: 10
>>>>>>> 6606a916b813f8e8654ecb37d7d88900f3109bf0
