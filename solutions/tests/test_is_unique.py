#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_unique function.
Contains tests for standard cases, edge cases, and defensive checks.

Test categories:
    - Standard cases: typical strings, single character, numbers in strings.
    - Edge cases: case-sensitivity, non-alphanumeric characters, single and multi spaces.
    - Defensive tests: wrong input types, empty string, NONE, assertions.

Created on 2025-01-01
Author: Ava Abdullah
"""

import unittest
from ..is_unique import is_unique


class TestIsUnique(unittest.TestCase):
    """Unit tests for the is_unique function."""

    # Standard test cases
    def test_all_unique_characters(self):
        """It should return True for a string with all unique characters."""
        self.assertTrue(is_unique("abcdefg"))

    def test_repeating_characters(self):
        """It should return False for a string with repeating characters."""
        self.assertFalse(is_unique("aabbcc"))

    def test_single_character(self):
        """It should return True for a string with a single character."""
        self.assertTrue(is_unique("a"))

    def test_numbers(self):
        """It should handle numbers in strings"""
        self.assertFalse(is_unique("548222"))

    # Edge cases
    def test_mixed_cases(self):
        """It should return True for a case-sensitive string with unique mixed-case characters."""
        self.assertTrue(is_unique("aAbBcC"))

    def test_special_characters(self):
        """It should return True for a string with special characters."""
        self.assertTrue(is_unique("!@#$%^&*()"))

    def test_multi_space_character(self):
        """It should handle white spaces"""
        self.assertFalse(is_unique("  "))

    def test_single_space_character(self):
        """It should return True for a string with a single space."""
        self.assertTrue(is_unique(" "))

    # Defensive tests
    def test_not_string_input(self):
        """It should raise AssertionError for non-string input."""
        with self.assertRaises(AssertionError):
            is_unique(123)

    def test_none_input(self):
        """It should raise AssertionError for None input."""
        with self.assertRaises(AssertionError):
            is_unique(None)

    def test_iterable_input(self):
        """It should raise AssertionError for an iterable input (not a string)."""
        with self.assertRaises(AssertionError):
            is_unique(["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
