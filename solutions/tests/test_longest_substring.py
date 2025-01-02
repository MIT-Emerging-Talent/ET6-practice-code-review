#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for long_substring function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: typical string inputs
    - Edge cases: empty strings, equal
    - Defensive tests: invalid inputs

Created on 2025-1-1
Author: Mohamed Saeed
"""

import unittest

from ..longest_substring import longest_substring


class TestFindLongest(unittest.TestCase):
    """
    Test class for the longest_substring function.
    """

    def test_standard_case(self):
        """
        Test the function with standard inputs.
        """
        self.assertEqual(longest_substring("abcabcbb"), "abc")

    def test_single_character(self):
        """
        Test the function with a single character.
        """
        self.assertEqual(longest_substring("a"), "a")

    def test_same_characters(self):
        """
        Test the function with a string of the same characters.
        """
        self.assertEqual(longest_substring("aaaaa"), "a")

    def test_unique_characters(self):
        """
        Test the function with a string of unique characters.
        """
        self.assertEqual(longest_substring("qwertyuiop"), "qwertyuiop")

    def test_long_string(self):
        """
        Test the function with a long string.
        """
        self.assertEqual(longest_substring("mohammedosmanmusasaeed"), "edosman")

    def test_numbers(self):
        """
        Test the function with numbers.
        """
        self.assertEqual(longest_substring("1234156789"), "234156789")

    def test_numbers_and_characters(self):
        """
        Test the function with numbers and characters.
        """
        self.assertEqual(longest_substring("1234ab14cd56789"), "ab14cd56789")

    def test_string_with_spaces(self):
        """
        Test the function with spaces.
        """
        self.assertEqual(longest_substring("a b c d e f g h i"), "abcdefghi")

    def test_empty_case(self):
        """
        Test the function with edge inputs.
        """
        with self.assertRaises(ValueError):
            longest_substring("")

    def test_special_characters(self):
        """
        Test the function with special characters.
        """
        self.assertEqual(longest_substring("!@#@$%&"), "#@$%&")

    def test_defensive_cases(self):
        """
        Test the function with invalid inputs.
        """
        with self.assertRaises(AssertionError):
            longest_substring(123)
