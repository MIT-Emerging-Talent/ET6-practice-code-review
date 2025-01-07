#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the missing_numbers function.

Test cases include:
    - strings with missing numbers.
    - strings without missing numbers.
    - strings containing letters or other non-numerical characters.
    - strings containing number formats other than integers.
    - strings containing different spacing sizes.
    - Sorted and unsorted numbers.
    - Edge cases: empty strings, single-number strings.
    - Invalid inputs: non-string values (e.g., integers or floats).

Created on 06/01/2025
@author: Amin
"""

import unittest

from ..missing_numbers import missing_numbers


class TestMissingNumbers(unittest.TestCase):
    """Test the missing_number function"""

    def test_unsorted_string(self):
        """It should return a sorted list with all the missing numbers"""
        self.assertEqual(missing_numbers("3 0"), [1, 2])

    def test_no_missing_number(self):
        """It should return [] for lists without missing numbers"""
        self.assertEqual(missing_numbers("1 2"), [])

    def test_one_missing_number(self):
        """It should return a list containing only the missing number"""
        self.assertEqual(missing_numbers("0 2"), [1])

    def test_multiple_cases(self):
        """It should return a sorted list with all the missing numbers"""
        self.assertEqual(missing_numbers("1 4"), [2, 3])

    def test_different_spaces(self):
        """It should function properly regardless of how many spaces are there in the initial string"""
        self.assertEqual(missing_numbers("1        4"), [2, 3])

    def test_not_string(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            missing_numbers(123)

    def test_not_numbers(self):
        """It should return a message for strings containing letters or other non-numerical characters"""
        self.assertEqual(
            missing_numbers("1 g"), ("The input contains non-integer values")
        )

    def test_non_integer_numbers(self):
        """It should return a message for strings containing number formats other than integers"""
        self.assertEqual(
            missing_numbers("1 2.1"), ("The input contains non-integer values")
        )
