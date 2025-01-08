"""
A module for testing the functions decimal_to_binary and binary_to_decimal.

Tests included:
    - decimal_to_binary: tested the cases when the input is a positive random number,
    input is a negative integer, input is zero, and when the input is a string.
    - binary_to_decimal: tested the cases when the input is a random binary number,
    input is a zero, and when the input is a string.

Created on 31 12 24
@author: Abdallah Alnajjar
"""

import unittest

from ..num_converter import binary_to_decimal, decimal_to_binary


class TestBinaryDecimalConversion(unittest.TestCase):
    """
    Tests both functions in num_converter, binary_to_decimal and decimal_to_binary.
    """

    def test_decimal_to_binary_247(self):
        """
        It should return a binary representation of 11110111
        """
        actual = decimal_to_binary(247)
        expected = 11110111
        self.assertEqual(actual, expected)

    def test_decimal_to_binary_zero(self):
        """
        It should return a binary representation of 11110111
        """
        actual = decimal_to_binary(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_decimal_to_binary_string(self):
        """
        It should raise an assertion error if the input is a non-integer
        """
        with self.assertRaises(AssertionError):
            decimal_to_binary("Abdallah")

    def test_decimal_to_binary_negative(self):
        """
        It should raise an assertion error if the input is a negative integer
        """
        with self.assertRaises(AssertionError):
            decimal_to_binary(-255)

    def test_binary_to_decimal_1111(self):
        """
        It should return 15 if the input is 1111
        """
        actual = binary_to_decimal(1111)
        expected = 15
        self.assertEqual(actual, expected)

    def test_binary_to_decimal_zeros(self):
        """
        It should return 0 if the input is zero
        """
        actual = binary_to_decimal(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_binary_to_decimal_non_binary(self):
        """
        It should raise an assertion error if the input contains digits other than 0 and 1
        """
        with self.assertRaises(AssertionError):
            binary_to_decimal(20105140)

    def test_binary_to_decimal_non_integer(self):
        """
        It should raise an assertion error if the input is a non-integer
        """
        with self.assertRaises(AssertionError):
            binary_to_decimal("Aboodi")
