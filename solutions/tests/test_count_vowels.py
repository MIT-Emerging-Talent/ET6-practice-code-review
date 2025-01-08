#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit test for count_vowels function.

Module contents:
    - TestCountVowels: Unit test class for the count_vowels function.

Created on 8 1 2025
@author: Nour Elhuda Haidar
"""

import unittest
from ..count_vowels import count_vowels 

class TestCountVowels(unittest.TestCase):
    """Unit test for count_vowels function."""

    def test_regular_sentence(self):
        """Test for a regular sentence."""
        self.assertEqual(count_vowels("python is awesome"), 6)

    def test_empty_string(self):
        """Test for an empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """Test for a string with no vowels."""
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_only_vowels(self):
        """Test for a string with only vowels."""
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_numeric_and_text(self):
        """Test for numeric and text combination."""
        self.assertEqual(count_vowels("123abc"), 1)

    def test_invalid_input_int(self):
        """Test for invalid input (integer)."""
        with self.assertRaises(AssertionError):
            count_vowels(123)