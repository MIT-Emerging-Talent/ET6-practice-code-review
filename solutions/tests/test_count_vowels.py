#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the count_vowels function.

Created on 2024-12-27

@author: Yuri Spizhovyi
"""

import unittest
from vowel_counter import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_empty_string(self):
        """Test that an empty string returns 0 vowels."""
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """Test that a string with no vowels returns 0."""
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_only_vowels(self):
        """Test that a string with only vowels returns the correct count."""
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_mixed_characters(self):
        """Test that a string with mixed characters (letters, spaces,
        punctuation) correctly counts vowels"""
        self.assertEqual(count_vowels("Hello, World!"), 3)

    def test_numbers_and_symbols(self):
        """
        Test that a string with numbers and symbols returns 0 vowels.
        Ensures non-alphabetic characters are ignored.
        """
        self.assertEqual(count_vowels("12345!@#$%"), 0)

if __name__ == "__main__":
    unittest.main()
