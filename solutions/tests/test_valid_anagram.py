"""
Unit tests for validating the valid_anagram function.

Test Categories:
    - Standard Cases: Basic anagram checking with various words
    - Edge Cases: Empty strings and repeated characters
    - Special Cases: Strings with numbers, spaces, and special characters
    - Defensive Cases: Invalid input handling

The tests verify that the function:
    - Correctly identifies anagrams
    - Handles case sensitivity
    - Processes special characters and numbers
    - Validates input types
    - Manages empty strings and spaces

Created on: 2025-01-11
@author: Fatima
"""

import unittest
from solutions.valid_anagram import valid_anagram


class Testvalidanagram(unittest.TestCase):
    """Test cases for valid_anagram function."""

    def test_basic_anagram(self):
        """It should identify basic anagrams correctly."""
        self.assertTrue(valid_anagram("listen", "silent"))

    def test_not_anagram(self):
        """It should return False for non-anagram strings."""
        self.assertFalse(valid_anagram("hello", "world"))

    def test_same_word(self):
        """It should identify same words as anagrams."""
        self.assertTrue(valid_anagram("word", "word"))

    def test_empty_string(self):
        """It should identify empty strings as amagrams."""
        self.assertTrue(valid_anagram("", ""))

    def test_case_sensitive(self):
        """It should be case sensitive in comparison"""
        self.assertFalse(valid_anagram("fatima", "Fatima"))

    def test_string_with_numbers(self):
        """It should identify numbers in a string as anagram"""
        self.assertTrue(valid_anagram("mad1ha", "aah1dm"))

    def test_repeated_characters(self):
        """It should handle strings with repeated characters."""
        self.assertTrue(valid_anagram("aaccbb", "ccaabb"))

    def test_special_characters(self):
        """It should handle special characters correctly."""
        self.assertTrue(valid_anagram("a!b@", "b@a!"))

    def test_spaces(self):
        """It should handle spaces as regular characters."""
        self.assertTrue(valid_anagram("a b", "b a"))

    def test_non_string_first_arg(self):
        """It should raise AssertionError for non-string first argument."""
        with self.assertRaises(AssertionError):
            valid_anagram(1998, "Jola")

    def test_non_string_second_arg(self):
        """It should raise AssertionError for non-string second argument."""
        with self.assertRaises(AssertionError):
            valid_anagram("Evan", None)


if __name__ == "__main__":
    unittest.main()
