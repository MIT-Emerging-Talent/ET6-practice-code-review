#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for format_phone_number function.
Contains correct tests to help identify bugs in the implementation

Test categories:
    - Standard cases: Valid inputs with different digit combinations
    - Edge cases: Boundary conditions (empty list, out-of-range digits)
    - Defensive cases: Invalid inputs (wrong types, wrong lengths)

Created on 2025-01-04
Author: KarimMakki
"""

import unittest

from ..format_phone_number import format_phone_number


class TestFormatPhoneNumber(unittest.TestCase):
    """Tests for format phone number function"""

    # Standard test cases
    def test_format_phone_number_mixed_digits(self):
        """It should format mixed digits as a phone number string"""
        actual = format_phone_number([0, 5, 6, 2, 3, 1, 7, 6, 5, 0])
        expected = "(056) 231-7650"
        self.assertEqual(actual, expected)

    def test_format_phone_number_single_digit(self):
        """It should format single digit as a phone number string"""
        actual = format_phone_number([9, 9, 9, 9, 9, 9, 9, 9, 9, 9])
        expected = "(999) 999-9999"
        self.assertEqual(actual, expected)

    def test_format_phone_number_ascending_digits(self):
        """It should format sequential ascending digits as a phone number string"""
        actual = format_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = "(012) 345-6789"
        self.assertEqual(actual, expected)

    # Edge Cases
    def test_phone_number_empty(self):
        """It should raise ValueError if the input list is empty."""
        with self.assertRaises(ValueError):
            format_phone_number([])

    def test_input_contains_double_digit(self):
        """it should raise ValueError for input with double digit"""
        with self.assertRaises(ValueError):
            format_phone_number([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_input_with_negative_digit(self):
        """it should raise ValueError for input with negative digit"""
        with self.assertRaises(ValueError):
            format_phone_number([-1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    # Defensive tests cases
    def test_non_list_input(self):
        """It should raise AssertionError for non-list input"""
        with self.assertRaises(AssertionError):
            format_phone_number("0123456789")

    def test_phone_number_less_than_ten_digits(self):
        """It should raise ValueError for phone number less than ten digits"""
        with self.assertRaises(ValueError):
            format_phone_number([0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_phone_number_greater_than_ten_digits(self):
        """It should raise ValueError for phone number greater than ten digits"""
        with self.assertRaises(ValueError):
            format_phone_number([1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_input_not_integer(self):
        """It should raise AssertionError for input not integer"""
        with self.assertRaises(AssertionError):
            format_phone_number(["0", 1, 2, 3, 4, 5, 6, 7, 8, 9])
