"""
This module contains unit tests for the vowel_counter module.
It includes test cases for the following function:
- vowel_counter: Test the function that counts vowels in a string.

Tests cover various cases including normal strings, empty strings, and case insensitivity.

Usage:
    Run tests using unittest framework:
    >>> python -m unittest test_vowel_counter.py
"""

import unittest

from ..vowel_counter import vowel_counter


class TestVowelCounter(unittest.TestCase):
    """
    Test suite for the vowel_counter module.
    """

    def test_vowel_counter(self):
        """
        Test the vowel_counter function.
        """
        # Test for different cases
        self.assertEqual(vowel_counter("Hello World"), 3)  # 'e', 'o', 'o'
        self.assertEqual(vowel_counter("Python"), 1)  # 'o'
        self.assertEqual(vowel_counter("aeiou"), 5)  # all vowels
        self.assertEqual(vowel_counter("XYZ"), 0)  # no vowels
        self.assertEqual(vowel_counter("HELLO WORLD!"), 3)  # 'E', 'O', 'O'

    def test_vowel_counter_empty(self):
        """
        Test vowel_counter for empty string.
        """
        self.assertEqual(vowel_counter(""), 0)  # No vowels in an empty string

    def test_vowel_counter_case_sensitive(self):
        """
        Test that the vowel_counter function is case-insensitive.
        """
        self.assertEqual(
            vowel_counter("AaEeIiOoUu"), 10
        )  # All vowels, case-insensitive


if __name__ == "__main__":
    unittest.main()
