#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the count_vowels function.

Created on 2025-01-07

@author: Rumiya Ismatova
"""

import unittest
from solutions.count_vowels1 import count_vowels


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
    unittest.main()
