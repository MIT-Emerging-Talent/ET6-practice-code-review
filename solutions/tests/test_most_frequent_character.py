#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for most_frequent_character function.
Contains tests for standard cases, edge cases, and defensive checks.

Test categories:
    - Standard cases: typical strings, tie cases, single character.
    - Edge cases: case-sensitivity, spaces, non-alphanumeric, numbers in strings
    - Defensive tests: wrong input types, empty string, NONE, assertions.

Created on 2025-01-04
Author: Ava Abdullah
"""

import unittest
from ..most_frequent_character import most_frequent_character


class TestMostFrequentCharacter(unittest.TestCase):
    """Unit tests for most_frequent_character function"""

    # Standard test cases
    def test_single_most_frequent(self):
        """It should return the most frequent character in a typical string"""
        self.assertEqual(most_frequent_character("aabbbcc"), "b")

    def test_frequency_tie(self):
        """It should return the first character in case of a frequency tie"""
        self.assertEqual(most_frequent_character("abab"), "a")

    def test_single_character(self):
        """It should return the character itself for a single-character string"""
        self.assertEqual(most_frequent_character("z"), "z")

    # Edge cases
    def test_mixed_cases(self):
        """It should distinguish between uppercase and lowercase characters"""
        self.assertEqual(most_frequent_character("aAAbBB"), "A")

    def test_spaces(self):
        """It should handle spaces as valid"""
        self.assertEqual(most_frequent_character("! ab  !"), " ")

    def test_non_alphanumeric_characters(self):
        """It should handle non-alphanumeric characters"""
        self.assertEqual(most_frequent_character("!!$$@@!!"), "!")

    def test_numbers(self):
        """It should handle numbers in strings"""
        self.assertEqual(most_frequent_character("548222"), "2")

    # Defensive tests
    def test_not_string_input(self):
        """It should raise AssertionError for non-string input."""
        with self.assertRaises(AssertionError):
            most_frequent_character(123)

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            most_frequent_character(None)

    def test_empty_string(self):
        """It should raise AssertionError for an empty string"""
        with self.assertRaises(AssertionError):
            most_frequent_character("")
