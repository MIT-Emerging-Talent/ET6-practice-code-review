#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for decimal_to_binary function.

@author: Heba Shaheen
"""

import unittest

from ..decimal_to_binary import decimal_to_binary


class TestDecimalToBinary(unittest.TestCase):
    """Unit tests for decimal_to_binary function."""

    def test_number_0(self):
        """It should return "0" as binary"""
        actual = decimal_to_binary(0)
        expected = "0"
        self.assertEqual(actual, expected)

    def test_number_2(self):
        """It should return "10" as binary"""
        actual = decimal_to_binary(2)
        expected = "10"
        self.assertEqual(actual, expected)

    def test_number_5(self):
        """It should return "101" as binary"""
        actual = decimal_to_binary(5)
        expected = "101"
        self.assertEqual(actual, expected)

    def test_number_15(self):
        """It should return "1111" as binary"""
        actual = decimal_to_binary(15)
        expected = "1111"
        self.assertEqual(actual, expected)

    def test_non_integer_input(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            decimal_to_binary("1")

    def test_negative_input(self):
        """It should raise an assertion error if the argument is negative"""
        with self.assertRaises(AssertionError):
            decimal_to_binary(-3)
