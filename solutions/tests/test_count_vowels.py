#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: test_count_vowels
Description: This module contains unit tests for the `count_vowels` function.

The `count_vowels` function takes a string as input and counts the number of vowels
(a, e, i, o, u) in the string, including both uppercase and lowercase vowels.

This module uses the `unittest` framework to test various cases for correctness.

Author: <Your Name>
Created on: <Date>
"""

import unittest
from solutions.count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    """A class to test the number of vowels in a given string."""

    def test_empty_string(self):
        """Test that an empty string returns 0."""
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """Test a string with no vowels."""
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_all_vowels(self):
        """Test a string with all vowels (lowercase and uppercase)."""
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_mixed_string(self):
        """Test a string with a mix of vowels and consonants."""
        self.assertEqual(count_vowels("Hello, World!"), 3)

    def test_numeric_and_special_characters(self):
        """Test a string with numbers and special characters."""
        self.assertEqual(count_vowels("12345!@#$%^&*()"), 0)

    def test_vowels_in_words(self):
        """Test a string with words containing vowels."""
        self.assertEqual(count_vowels("Python programming is fun!"), 6)
        
    if __name__ == "__main__":
        unittest.main()