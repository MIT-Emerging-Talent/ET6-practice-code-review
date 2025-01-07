#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for longest_substring function.

Test categories:
    - Standard cases: Covers typical inputs with varying character repetitions.
    - Performance tests: Large inputs to ensure the function performs efficiently with high input sizes.
    - Edge cases: .
    - Defensive tests: .

Created on 2025-01-07
@author: Gennadii Ershov
"""

import unittest

from ..longest_substring import longest_substring


class TestLongestSubstring(unittest.TestCase):
    """Test the longest_substring function"""

    # Standard test cases
    def test_case_1(self):
        """Test with input 'abcabcbb', expecting output 3."""
        self.assertEqual(longest_substring("abcabcbb"), 3)

    def test_case_2(self):
        """Test with input 'bbbbb', expecting output 1."""
        self.assertEqual(longest_substring("bbbbb"), 1)

    def test_case_3(self):
        """Test with input 'pwwkew', expecting output 3."""
        self.assertEqual(longest_substring("pwwkew"), 3)

    def test_empty_string(self):
        """Test with an empty string, expecting output 0."""
        self.assertEqual(longest_substring(""), 0)

    def test_single_character(self):
        """Test with a single character string, expecting output 1."""
        self.assertEqual(longest_substring("a"), 1)

    def test_all_unique_characters(self):
        """Test with all unique characters, expecting output equal to string length."""
        self.assertEqual(longest_substring("abcdef"), 6)

    def test_long_repeating_sequence(self):
        """Test with a long repeating sequence, expecting output 3."""
        self.assertEqual(longest_substring("aabcc"), 3)

    # Performance tests
    def test_large_input(self):
        """Test with a long input string, expecting output equal to unique characters."""
        large_input = (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
            * 10  # Repeating the pattern to make the string longer
        )
        expected_output = len(set(large_input))  # Unique characters in the input
        self.assertEqual(longest_substring(large_input), expected_output)

    def test_large_non_repeating_string(self):
        """Performance test with a very long string of unique characters, expecting the length of the string as output."""
        test_case = "a" * (10**5 - 1) + "b"
        expected_output = 100000
        self.assertEqual(longest_substring(test_case), expected_output)
