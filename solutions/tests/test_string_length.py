#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for string_length function.

Contains comprehensive tests to verify string length calculation.
Test categories:
    - Standard cases: typical strings (basic length functionality)
    - Edge cases: empty strings, single character strings
    - Defensive tests: invalid inputs (non-string types)

Created on Jan 05, 2025.

@author: Nada Hamza

"""

import unittest
from ..string_length import string_length


class TestStringLength(unittest.TestCase):
    """Tests for the string_length function."""

    # Standard test cases
    def test_normal_string(self):
        """It should return 5 for the string 'hello'."""
        actual = string_length("hello")
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_string(self):
        """It should return 18 for the string 'Python Programming'."""
        actual = string_length("Python Programming")
        expected = 18
        self.assertEqual(actual, expected)

    def test_with_numbers(self):
        """It should return 6 for the string '123456'."""
        actual = string_length("123456")
        expected = 6
        self.assertEqual(actual, expected)

    def test_with_special_chars(self):
        """It should return 6 for the string '!@#$%^'."""
        actual = string_length("!@#$%^")
        expected = 6
        self.assertEqual(actual, expected)

    # Edge cases
    def test_empty_string(self):
        """It should return 0 for an empty string."""
        actual = string_length("")
        expected = 0
        self.assertEqual(actual, expected)

    def test_single_character(self):
        """It should return 1 for a single character string."""
        actual = string_length("a")
        expected = 1
        self.assertEqual(actual, expected)

    def test_whitespace_string(self):
        """It should return 3 for three spaces."""
        actual = string_length("   ")
        expected = 3
        self.assertEqual(actual, expected)

    def test_unicode_string(self):
        """It should return 11 for unicode string 'héllo würld'."""
        actual = string_length("héllo würld")
        expected = 11
        self.assertEqual(actual, expected)

    # Defensive tests
    def test_none_input(self):
        """It should raise ValueError when input is None."""
        with self.assertRaises(ValueError):
            string_length(None)

    def test_non_string_input_number(self):
        """It should raise TypeError when input is a number."""
        with self.assertRaises(TypeError):
            string_length(12345)

    def test_non_string_input_boolean(self):
        """It should raise TypeError when input is a boolean."""
        with self.assertRaises(TypeError):
            string_length(True)

    def test_non_string_input_list(self):
        """It should raise TypeError when input is a list."""
        with self.assertRaises(TypeError):
            string_length(["a", "b", "c"])
