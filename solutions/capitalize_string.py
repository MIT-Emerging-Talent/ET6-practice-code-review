""" "
Created on 0084/01/2025
@author: Arwa Mohamed

"""

import unittest


def capitalize_string(s):
    """
    Converts all letters in a given string to uppercase.

    Args:
        s (str): The input string to be capitalized.

    Returns:
        str: A new string with all letters converted to uppercase.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> capitalize_string("hello")
        'HELLO'
        >>> capitalize_string("Python 123!")
        'PYTHON 123!'
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s.upper()


if __name__ == "__main__":
    unittest.main()
