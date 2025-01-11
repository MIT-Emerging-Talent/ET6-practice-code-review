#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A test for module int_to_binary.

Test categories:
    - Standard cases: small positive numbers
    - Edge cases: 0, 1
    - Defensive tests: assertions, wrong input types

Created on 9 1 2025
@author: Dadi Ishimwe
"""

import unittest
from ..int_to_binary import int_to_binary


class TestIntToBinary(unittest.TestCase):
    """Test the int_to_binary function"""

    def test_zero(self):
        """Test the binary representation of 0 is '0'"""
        self.assertEqual(int_to_binary(0), "0")

    def test_one(self):
        """Test the binary representation of 1 is '1'"""
        self.assertEqual(int_to_binary(1), "1")

    def test_small_number(self):
        """Test the binary representation of 2 is '10'"""
        self.assertEqual(int_to_binary(2), "10")

    def test_two_digits_number(self):
        """Test the binary representation of 10 is '1010'"""
        self.assertEqual(int_to_binary(10), "1010")

    def test_large_number(self):
        """Test the binary representation of 42 is '101010'"""
        self.assertEqual(int_to_binary(42), "101010")

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            int_to_binary(None)

    def test_non_integer_input(self):
        """It should raise AssertionError for non-integer input"""
        with self.assertRaises(AssertionError):
            int_to_binary("10")

    def test_negative_number(self):
        """It should raise ValueError for negative integer"""
        with self.assertRaises(ValueError):
            int_to_binary(-1)
