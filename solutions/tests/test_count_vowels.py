"""Unit tests for the count_vowels function."""

import unittest
from solutions.count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    """Test cases for count_vowels function."""

    def test_empty_string(self):
        """It should return 0 for an empty string."""
        self.assertEqual(count_vowels(""), 0)

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

    def test_mixed_case_vowels(self):
        """It should count both uppercase and lowercase vowels in a string."""
        self.assertEqual(count_vowels("hellOWorld"), 3)

    def test_repeated_vowels(self):
        """It should count all repeated vowels in a string."""
        self.assertEqual(count_vowels("aaeeiioouuAAEEIIOOUU"), 20)

    def test_alphanumeric_string(self):
        """It should count vowels in alphanumeric strings, ignoring digits."""
        self.assertEqual(count_vowels("fatima123Malik"), 5)

    def test_special_characters(self):
        """It should ignore special characters and only count vowels."""
        self.assertEqual(count_vowels("!@#$%^&*()aeiOu"), 5)

    def test_string_with_whitespace(self):
        """It should count vowels even if the string contains spaces."""
        self.assertEqual(count_vowels("hello world"), 3)

    def test_invalid_input(self):
        """Test that raises assertion error for non-string input."""
        with self.assertRaises(AssertionError):
            count_vowels(None)

if __name__ == '__main__':
    unittest.main()
