#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for reverse_string function

Test categories:
 -Standard cases: typical inputs
 -Edge cases: extreme inputs and boundaries
 -Defensive tests: wrong input types, assertions

Created on 5/1/2025
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)
"""

import unittest

from ..reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    """Test suite for the reverse_string function for reversing an input string"""

    # Standard cases
    def test_lower_case_letters_string(self):
        """it should return a string with the letters in reversed order"""
        self.assertEqual(reverse_string("abcde"), "edcba")

    def test_numbers_only_string(self):
        """it should return a string with the numbers in reversed order"""
        self.assertEqual(reverse_string("123456"), "654321")

    def test_string_capital_and_small_letters_mixed(self):
        """it should reverse the string without affecting capitalization"""
        self.assertEqual(reverse_string("AbscEfgh"), "hgfEcsbA")

    def test_string_with_mixed_numbers_and_letters(self):
        """it should return a string with the numbers and letters in reversed order"""
        self.assertEqual(reverse_string("1a2b3c4d5e6f"), "f6e5d4c3b2a1")

    def test_string_with_blank_spaces(self):
        """it should reverse the input string and treat each space as a separate character"""
        self.assertEqual(reverse_string("ab c  de"), "ed  c ba")

    # Edge cases

    def test_long_input(self):
        """it should reverse the input string even if the input is long"""
        self.assertEqual(
            reverse_string("12345678910111213141516171819"),
            "91817161514131211101987654321",
        )

    def test_empty_string(self):
        """it should return an empty string"""
        self.assertEqual(reverse_string(""), "")

    # Defensive tests
    def test_non_string_input(self):
        """It should raise AssertionError if input is not a string"""
        with self.assertRaises(AssertionError):
            reverse_string([1, 2, 3, 4, 5, 6])
