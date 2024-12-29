#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for decimal_to_base function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: A set of typical numbers for regular testing.
    - Edge cases: zero, to binary, octal and hexadecimal.
    - Defensive tests: wrong input types, assertions

Created on Dec 29, 2024.

@author: AL-HASSEN SABEEH
"""

import unittest

from ..decimal_to_base import decimal_to_base


class TestDecimalToBase(unittest.TestCase):
    """Test the decimal_to_base function"""

    # Test Edge Cases
    def test_zero_to_binary(self):
        """It should evaluate '0' to 0b0"""
        self.assertEqual(decimal_to_base(0, 2), "0b0")

    def test_zero_to_octal(self):
        """It should evaluate '0' to 0o0"""
        self.assertEqual(decimal_to_base(0, 8), "0o0")

    def test_zero_to_hexadecimal(self):
        """It should evaluate '0' to 0"""
        self.assertEqual(decimal_to_base(0, 16), "0x0")

    # Test Standard Cases
    def test_9834_to_binary(self):
        """It should evaluate 9834 to what is returned by bin(3834)"""
        self.assertEqual(decimal_to_base(9834, 2), bin(9834))

    def test_9834_to_octal(self):
        """It should evaluate 9834 to what is returned by oct(3834)"""
        self.assertEqual(decimal_to_base(9834, 8), oct(9834))

    def test_45675678_to_hexadecimal(self):
        """It should evaluate 9834 to what is returned by hex(3834)"""
        self.assertEqual(decimal_to_base(45675678, 16), hex(45675678))

    # Test Defensive Assertions
    def test_defensive_check_decimal_is_not_int(self):
        """it should raise an error if the first argument is not an integer"""
        with self.assertRaises(AssertionError):
            decimal_to_base("5", 8)

    def test_defensive_check_base_is_not_int(self):
        """it should raise an error if the second argument is not an integer"""
        with self.assertRaises(AssertionError):
            decimal_to_base(20, "5")

    def test_defensive_check_for_negative_decimal_number(self):
        """it should raise an error if the input is less than 0"""
        with self.assertRaises(AssertionError):
            decimal_to_base(-4, 2)

    def test_defensive_check_base_is_not_2_or_8_or_16(self):
        """it should raise an error if the input is not an integer"""
        with self.assertRaises(AssertionError):
            decimal_to_base(5, 7)

    def test_none_input_for_first_argument(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            decimal_to_base(None, 2)

    def test_none_input_for_second_argument(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            decimal_to_base(6789, None)
