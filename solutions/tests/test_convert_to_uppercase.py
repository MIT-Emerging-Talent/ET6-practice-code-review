"""
Unit tests for the `convert_to_uppercase` function.

Author: Tamara Saqer
Date: 2025-01-10
"""

import unittest
import sys
import os

# Add the parent directory to the Python path to avoid import issues
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from convert_to_uppercase import convert_to_uppercase


class TestConvertToUppercase(unittest.TestCase):
    """
    Test cases for the `convert_to_uppercase` function.
    """

    def test_valid_strings(self):
        """
        Test that valid strings are correctly converted to uppercase.
        """
        self.assertEqual(convert_to_uppercase("hello"), "HELLO")
        self.assertEqual(convert_to_uppercase("Tamara"), "TAMARA")
        self.assertEqual(convert_to_uppercase("123"), "123")  # Numbers remain unchanged

    def test_empty_string(self):
        """
        Test that an empty string returns an empty string.
        """
        self.assertEqual(convert_to_uppercase(""), "")

    def test_whitespace_string(self):
        """
        Test that a string with only whitespace remains unchanged.
        """
        self.assertEqual(convert_to_uppercase("   "), "   ")

    def test_non_string_input(self):
        """
        Test that a non-string input raises a ValueError.
        """
        with self.assertRaises(ValueError):
            convert_to_uppercase(123)

        with self.assertRaises(ValueError):
            convert_to_uppercase(None)


if __name__ == "__main__":
    unittest.main()
