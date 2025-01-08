"""
This module contains unit tests for the vowel_counter module.
It includes test cases for the following function:
- count_vowels: Test the function that counts vowels in a string.

Tests cover various cases including normal strings, empty strings, and case insensitivity.

Usage:
    Run tests using unittest framework:
    >>> python -m unittest test_vowel_counter.py
"""

import unittest

from ..vowel_counter import count_vowels


class TestVowelCounter(unittest.TestCase):
    """
    Test suite for the vowel_counter module.
    """

    def test_count_vowels(self):
        """
        Test the count_vowels function.
        """
        # Test for different cases
        self.assertEqual(count_vowels("Hello World"), 3)  # 'e', 'o', 'o'
        self.assertEqual(count_vowels("Python"), 1)  # 'o'
        self.assertEqual(count_vowels("aeiou"), 5)  # all vowels
        self.assertEqual(count_vowels("XYZ"), 0)  # no vowels
        self.assertEqual(count_vowels("HELLO WORLD!"), 3)  # 'E', 'O', 'O'

    def test_count_vowels_empty(self):
        """
        Test count_vowels for empty string.
        """
        self.assertEqual(count_vowels(""), 0)  # No vowels in an empty string

    def test_count_vowels_case_sensitive(self):
        """
        Test that the count_vowels function is case-insensitive.
        """
        self.assertEqual(count_vowels("AaEeIiOoUu"), 10)  # All vowels, case-insensitive


if __name__ == "__main__":
    unittest.main()
