"""
Unit tests for the `convert_to_uppercase` function.

Author: Tamara Saqer
Date: 2025-01-10
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from convert_to_uppercase import convert_to_uppercase


class TestConvertToUppercase(unittest.TestCase):
    """
    Test cases for the `convert_to_uppercase` function.
    """

    def test_valid_lowercase_string(self):
        """
        Test that a lowercase string is converted to uppercase.
        """
        self.assertEqual(convert_to_uppercase("hello"), "HELLO")

    def test_valid_mixed_case_string(self):
        """
        Test that a mixed-case string is converted to uppercase.
        """
        self.assertEqual(convert_to_uppercase("Tamara"), "TAMARA")

    def test_string_with_numbers(self):
        """
        Test that a string with numbers remains unchanged for numeric parts.
        """
        self.assertEqual(convert_to_uppercase("123"), "123")

    def test_empty_string(self):
        """
        Test that an empty string returns an empty string.
        """
        self.assertEqual(convert_to_uppercase(""), "")

    def test_whitespace_only_string(self):
        """
        Test that a string with only whitespace remains unchanged.
        """
        self.assertEqual(convert_to_uppercase("   "), "   ")

    def test_non_string_input_integer(self):
        """
        Test that an integer input raises a ValueError.
        """
        with self.assertRaises(ValueError):
            convert_to_uppercase(123)

    def test_non_string_input_none(self):
        """
        Test that a None input raises a ValueError.
        """
        with self.assertRaises(ValueError):
            convert_to_uppercase(None)


if __name__ == "__main__":
    unittest.main()
