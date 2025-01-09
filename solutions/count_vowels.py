"""
A module for counting vowels in a string.

Module contents:
    - count_vowels: Counts the number of vowels in a given string.
      It supports both uppercase and lowercase vowels.

Created on: 2025-07-06
@author: Fatima
"""


def count_vowels(text: str) -> int:
    """Returns the number of vowels (both uppercase and lowercase) in a string.

    Parameters:
        text: str, the input string to check

    Returns:
    int: Number of vowels in the text.

    Raises:
        AssertionError: if the argument is not a string

    >>> count_vowels("hello")
    2
    >>> count_vowels("APPLE")
    2
    >>> count_vowels("why")
    0
    """

    assert isinstance(text, str), "input must be a string"

    vowels = "aeiouAEIOU"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count
