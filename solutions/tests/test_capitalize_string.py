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


class TestCapitalizeString(unittest.TestCase):
    def test_all_lowercase(self):
        self.assertEqual(capitalize_string("hello"), "HELLO")

    def test_mixed_case(self):
        self.assertEqual(capitalize_string("HeLLo"), "HELLO")

    def test_numbers_and_symbols(self):
        self.assertEqual(capitalize_string("Python 123!"), "PYTHON 123!")

    def test_empty_string(self):
        self.assertEqual(capitalize_string(""), "")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            capitalize_string(123)
        with self.assertRaises(TypeError):
            capitalize_string(["hello", "world"])


if __name__ == "__main__":
    unittest.main()
