#!/usr/bin/env python3
"""
This is a function that filters a list of strings and returns a list with only your friend's name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
Otherwise, you can be sure they're not...

Examples:
    >>> friend(["Nimo", "Brian", "Joe", "Joan"])
    ['Nimo', 'Joan']
    >>> friend(["Ron", "Stephen", "Philip"])
    []
    >>> friend("Nimo")
    'Input should be a list of strings'

Raises:
    TypeError: If the input is not a list or contains non-string elements.

Created on 2025-01-04
Author: Cynthia Wairimu
"""

from typing import List, Union


def friend(x: Union[List[str], any]) -> List[str]:
    """
    Filters a list to return names with exactly 4 characters.

    Args:
        x (list[str]): A list of names as strings.

    Returns:
        list[str]: A list of names with 4 characters, or an error message for invalid input.
    """
    if not isinstance(x, list) or not all(isinstance(name, str) for name in x):
        raise TypeError("Input should be a list of strings")

    # Return a list of 4-character names
    return [name for name in x if len(name) == 4]
