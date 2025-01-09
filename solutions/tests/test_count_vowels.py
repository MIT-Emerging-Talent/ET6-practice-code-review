#!/usr/bin/env python3
# -*- coding: utf-8 -*-
<<<<<<< HEAD
"""
Unit tests for the count_vowels function.

Created on 2025-01-07

@author: Rumiya Ismatova
"""

import unittest
from solutions.count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    """
    Unit test class for testing the functionality of the count_vowels function.

    The count_vowels function calculates the number of vowels in a given string.
    This test class includes multiple test cases to ensure the function behaves
    correctly for various input scenarios, including edge cases and typical use cases.
    """

    def test_empty_string(self):
        """Test that an empty string returns 0 vowels."""
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """Test that a string with no vowels returns 0."""
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_only_vowels(self):
        """Test that a string with only vowels returns the correct count."""
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_mixed_characters(self):
        """Test that a string with mixed characters (letters, spaces,
        punctuation) correctly counts vowels"""
        self.assertEqual(count_vowels("Hello, World!"), 3)

    def test_numbers_and_symbols(self):
        """
        Test that a string with numbers and symbols returns 0 vowels.
        Ensures non-alphabetic characters are ignored.
        """
        self.assertEqual(count_vowels("12345!@#$%"), 0)


# Run all the test cases
if __name__ == "__main__":
=======

# Unit tests for the count_vowels function.


import unittest
from ..count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    # Unit tests for the count_vowels function.

    def test_basic_vowels(self):
        # Test that vowels are correctly counted in a basic string.

        self.assertEqual(count_vowels("hello"), 2)

    def test_uppercase_vowels(self):
        # Test that uppercase vowels are correctly counted.

        self.assertEqual(count_vowels("HELLO"), 2)

    def test_mixed_content(self):
        # Test that vowels are counted in a string with mixed content.

        self.assertEqual(count_vowels("123 abc XYZ"), 1)

    def test_no_vowels(self):
        # Test that a string with no vowels returns 0.

        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_all_vowels(self):
        # Test that a string with only vowels returns the correct count.

        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_empty_string(self):
        # Test that an empty string returns 0.

        self.assertEqual(count_vowels(""), 0)

    def test_special_characters(self):
        # Test that a string with special characters only returns 0.

        self.assertEqual(count_vowels("!@#$%^&*()"), 0)

    def test_assertion_error(self):
        # Test to ensure the function raises an AssertionError for non-string inputs.
        with self.assertRaises(AssertionError):
            count_vowels(12345)


if __name__ == "__main__":
    # This ensures that the unittest framework runs the test cases in this file
>>>>>>> 6606a916b813f8e8654ecb37d7d88900f3109bf0
    unittest.main()
