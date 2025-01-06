"""
Module: cat_dog
This module contains a function to check if the number of occurrences
of the substrings "cat" and "dog" are the same in a given string.
"""


def cat_dog(s: str) -> bool:
    """
    Check if the string "cat" and "dog" appear the same number of times in the given string.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if "cat" and "dog" appear the same number of times, otherwise False.

    Raises:
        TypeError: If the input is not a string.

    Doctests:
        >>> cat_dog("catdog")
        True
        >>> cat_dog("catcat")
        False
        >>> cat_dog("1cat1cadodog")
        True
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    return s.count("cat") == s.count("dog")
