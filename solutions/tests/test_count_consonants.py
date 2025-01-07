#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains tests for the `count_consonants` function.

The tests validate the function's ability to handle:
- Mixed cases of consonants and vowels.
- Special characters and numbers.
- Edge cases such as empty strings and non-string inputs.

Author: Norbert Ndayisenga
Date: 07 01 2025
"""

import unittest
from solutions.count_consonants import count_consonants


class TestCountConsonants(unittest.TestCase):
    def test_mixed_case_and_special_characters(self):
        """It should handle mixed cases of consonants, vowels, and special characters."""
        self.assertEqual(count_consonants("Hello, World!"), 7)

    def test_only_consonants(self):
        """It should correctly count consonants when the string contains only consonants."""
        self.assertEqual(count_consonants("bcdfghjklmnpqrstvwxyz"), 21)

    def test_only_vowels(self):
        """It should return 0 when the string contains only vowels."""
        self.assertEqual(count_consonants("aeiouAEIOU"), 0)

    def test_empty_string(self):
        """It should return 0 when the string is empty."""
        self.assertEqual(count_consonants(""), 0)

    def test_special_characters_and_numbers(self):
        """It should return 0 when the string contains only numbers and special characters."""
        self.assertEqual(count_consonants("123@#$"), 0)

    def test_invalid_input(self):
        """It should raise a TypeError when input is not a string."""
        with self.assertRaises(TypeError):
            count_consonants(12345)
        with self.assertRaises(TypeError):
            count_consonants(None)
