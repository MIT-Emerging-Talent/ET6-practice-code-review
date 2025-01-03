#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains unit tests to validate the functionality of the
`length_longest_substring` function.
It checks the length of the longest substring without repeating characters in a string.

Test categories:
    - Standard cases: Typical strings with and without repeating characters.
    - Edge cases: Empty strings, single-character strings, and strings with special characters.
    - Defensive tests: Non-string inputs to ensure proper assertion handling.

Created on: 2025-01-03
Author: Jola-Moses
"""

import unittest
from solutions.length_longest_substring import length_longest_substring

class TestLengthLongestSubstring(unittest.TestCase):
    """Tests for length_longest_substring"""

    def test_basic_case(self):
        """It should return 3 for 'abcabcbb'."""
        self.assertEqual(length_longest_substring('abcabcbb'), 3)

    def test_all_unique_characters(self):
        """It should return the length of the string with all unique characters."""    
        self.assertEqual(length_longest_substring('abcdef'), 6)

    def test_all_identical_characters(self):
        """It should return 1 for strings with all identical characters."""    
        self.assertEqual(length_longest_substring('aaaaaa'), 1)

    def test_single_character(self):
        """lt should return 1 for a string with a single character."""
        self.assertEqual(length_longest_substring('a'), 1)

    def test_alternating_characters(self):
        """lt should return 2 for 'abababab'."""
        self.assertEqual(length_longest_substring('abababab'), 2)

    def test_substring_at_the_end(self):
        """lt should return 5 for 'abcdabcde'."""
        self.assertEqual(length_longest_substring('abcdabcde'), 5)

    def test_substring_at_the_beginning(self):
        """lt should return 5 for 'abcdeabcd'."""
        self.assertEqual(length_longest_substring('abcdeabcd'), 5)

    def test_repeating_characters_in_between(self):
        """lt should return 3 for 'abccba'."""    
        self.assertEqual(length_longest_substring('abccba'), 3)

    def test_leading_repeated_characters(self):
        """lt should return 6 for 'aaabcdef'.""" 
        self.assertEqual(length_longest_substring('aaabcdef'), 6)

    def test_long_string_with_single_repeated_character(self):
        """lt should return 6 for 'abcdeeeeeeeefghij'."""
        self.assertEqual(length_longest_substring('abcdeeeeeeeefghij'), 6)

    def test_mixed_case_sensitivity(self):
        """lt should handle characters with different cases uniquely."""
        self.assertEqual(length_longest_substring('AaBbCcDd'), 8)

    def test_numeric_string(self):
        """lt should handle numeric-string characters."""
        self.assertEqual(length_longest_substring('123412345'), 5)

    def test_special_characters(self):
        """lt should handle symbols as characters."""
        self.assertEqual(length_longest_substring('!@#$%^&*()'), 10)

    def test_mixed_characters(self):
        """It should handle strings containing alphanumeric and symbol characters."""
        self.assertEqual(length_longest_substring('a1b#2c$3d4'), 10)

    def test_spaces_included(self):
        """lt should handle spaces as characters."""
        self.assertEqual(length_longest_substring('abc abc'), 4)

    def test_empty_string(self):
        """It should return 0 for an empty string."""  
        self.assertEqual(length_longest_substring(''), 0)

    def test_long_string(self):
        """lt should return 1 for 'a' repeated 1 million times."""
        self.assertEqual(length_longest_substring('a' * 10**6), 1)

    def test_invalid_input_integer(self):
        """lt should raise an error for non-string input."""
        with self.assertRaises(AssertionError):
            length_longest_substring(30)

    def test_invalid_input_none(self):
        """lt should raise an error for non-string input."""    
        with self.assertRaises(AssertionError):
            length_longest_substring(None)

# if __name__ == "__main__":
#     unittest.main()
