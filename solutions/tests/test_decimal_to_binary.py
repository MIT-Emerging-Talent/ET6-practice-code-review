#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for decimal_to_binary function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: A set of typical numbers for regular testing.
    - Edge cases: zero, one and a large number.
    - Defensive tests: wrong input types, assertions

Created on Dec 25, 2024.

@author: AL-HASSEN SABEEH
"""

import unittest

from ..decimal_to_binary import decimal_to_binary


class TestDecimalToBinary(unittest.TestCase):
    """Test the decimal_to_binary function"""

    def test_zero(self):
        """It should evaluate 0 to '0'"""
        actual = decimal_to_binary(0)  # call function with test arguments
        expected = "0"  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_number_one(self):
        """It should evaluate 1 to '1'"""
        actual = decimal_to_binary(1)
        expected = "1"
        self.assertEqual(actual, expected)

    def test_number_two(self):
        """It should evaluate 2 to '10'"""
        actual = decimal_to_binary(2)
        self.assertEqual(actual, "10")

    def test_number_three(self):
        """It should evaluate 3 to '11'"""
        expected = "11"
        self.assertEqual(decimal_to_binary(3), expected)

    def test_number_four(self):
        """It should evaluate 4 to '100'"""
        actual = decimal_to_binary(4)
        expected = "100"
        self.assertEqual(actual, expected)

    def test_number_five(self):
        """It should evaluate 5 to '101"""
        self.assertEqual(decimal_to_binary(5), "101")

    def test_number_nine(self):
        """It should evaluate 9 to '1001"""
        self.assertEqual(decimal_to_binary(9), "1001")

    def test_a_big_number(self):
        """It should evaluate 7429742 to"""
        self.assertEqual(decimal_to_binary(1023), "1111111111")
    #test defensive assertions
    def test_defensive_check_repetitions_is_not_int(self):
        """it should raise an error if the input is not an integer"""
        with self.assertRaises(AssertionError):
            decimal_to_binary("5")

    def test_defensive_check_for_negative_decimal_number(self):
        """it should raise an error if the input is less than 0"""
        with self.assertRaises(AssertionError):
            decimal_to_binary(-4)
        
    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            decimal_to_binary(None)
    