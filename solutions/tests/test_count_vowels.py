"""
Unit tests for validating the count_vowels function.

Test Categories:
    - Standard Cases: Regular words with varying vowel counts.
    - Edge Cases: Empty strings, repeated vowels, and mixed casing.
    - Special Cases: Strings with numbers, special characters, and whitespace.
    - Defensive Cases: Ensuring proper handling of non-string inputs.

Created on: 2025-07-06
@author: Fatima
"""

import unittest
from solutions.count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    """Test cases for count_vowels function."""

    # Standard Cases
    def test_typical_word(self):
        """It should count vowels in a regular word with both vowels and consonants."""
        self.assertEqual(count_vowels("hello"), 2)

    def test_no_vowels(self):
        """It should return 0 for a string with no vowels."""
        self.assertEqual(count_vowels("fly"), 0)

    def test_all_vowels(self):
        """It should handle all uppercase and lowercase vowels."""
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_uppercase_vowels(self):
        """It should count uppercase vowels in the string."""
        self.assertEqual(count_vowels("SMALL"), 1)

    def test_lowercase_vowels(self):
        """It should count lowercase vowels in the string."""
        self.assertEqual(count_vowels("small"), 1)

    # Edge Cases
    def test_empty_string(self):
        """It should return 0 for an empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_only_whitespace(self):
        """It should return 0 for strings with only whitespace.."""
        self.assertEqual(count_vowels("     "), 0)

    def test_mixed_case_vowels(self):
        """It should count both uppercase and lowercase vowels in a string."""
        self.assertEqual(count_vowels("hellOWorld"), 3)

    def test_repeated_vowels(self):
        """It should count all repeated vowels in a string."""
        self.assertEqual(count_vowels("aaeeiioouuAAEEIIOOUU"), 20)

    def test_long_string(self):
        """It should correctly count vowels in a long mixed-case string."""
        text = ("aAeEiIoOuU" * 500) + "bcdfghjklmnpqrstvwxyz" * 100
        self.assertEqual(count_vowels(text), 5000)

    # Special Cases
    def test_alphanumeric_string(self):
        """It should count vowels in alphanumeric strings, ignoring digits."""
        self.assertEqual(count_vowels("fatima123Malik"), 5)

    def test_special_characters(self):
        """It should ignore special characters and only count vowels."""
        self.assertEqual(count_vowels("!@#$%^&*()aeiOu"), 5)

    def test_string_with_whitespace(self):
        """It should count vowels even if the string contains spaces."""
        self.assertEqual(count_vowels("hello world"), 3)

    # Defensive Cases
    def test_invalid_input(self):
        """Test that raises assertion error for non-string input."""
        with self.assertRaises(AssertionError):
            count_vowels(None)


if __name__ == "__main__":
    unittest.main()
