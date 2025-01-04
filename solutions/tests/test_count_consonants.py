#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""

import unittest

# --- imports & test class before documenting and testing ---

# from ..count_consonants count_consonants

# class TestCountConsonants(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..count_consonants import count_consonants


class TestCountConsonants(unittest.TestCase):
    """Test the count_consonants function"""

    def test_empty_string(self):
        """It should evaluate an empty string to 0"""
        self.assertEqual(count_consonants(""), 0)

    def test_all_vowels(self):
        """It should evaluate a string of only vowels to 0"""
        self.assertEqual(count_consonants("aeiouAEIOU"), 0)

    def test_all_consonants(self):
        """It should evaluate a string of only consonants correctly"""
        self.assertEqual(count_consonants("bcdfghjklmnpqrstvwxyz"), 21)
        

    def test_mixed_characters(self):
        """It should handle mixed cases of vowels, consonants, and symbols"""
        self.assertEqual(count_consonants("Hello, World!"), 7)

    def test_whitespace(self):
        """It should ignore whitespace"""
        self.assertEqual(count_consonants("    "), 0)

    def test_non_alpha_characters(self):
        """It should ignore digits and special characters"""
        self.assertEqual(count_consonants("123@#$"), 0)

    def test_assert_non_string_input(self):
        """It should raise an assertion error for non-string inputs"""
        with self.assertRaises(AssertionError):
            count_consonants(123)


if __name__ == "__main__":
    unittest.main()
