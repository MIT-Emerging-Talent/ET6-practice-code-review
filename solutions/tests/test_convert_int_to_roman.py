#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 04/01/2025
@author: Peter Ngugi

Unit test for convert_int_to_roman function.

Module contents:
    - TestConvertIntToRoman: Unit test class for the convert_int_to_roman function.
"""

import unittest

from solutions.convert_int_to_roman import convert_int_to_roman


class TestConvertIntToRoman(unittest.TestCase):
    """Test the Convert_int_to_roman function"""

    def test_single_digit_int(self):
        """ "Should return a roman numeral
        representation for a single digit integer"""
        actual = convert_int_to_roman(7)
        expected = "VII"
        self.assertEqual(actual, expected)

    def test_double_digit_int(self):
        """Should return a roman numeral
        representation for a double-digit integer"""
        actual = convert_int_to_roman(42)
        expected = "XLII"
        self.assertEqual(actual, expected)

    def test_triple_digit_int(self):
        """Should return a roman numeral
        representation for a triple-digit integer"""
        actual = convert_int_to_roman(387)
        expected = "CCCLXXXVII"
        self.assertEqual(actual, expected)

    def test_boundary_value(self):
        """Should return a roman numeral
        representation for the maximum input of 3999"""
        actual = convert_int_to_roman(3999)
        expected = "MMMCMXCIX"
        self.assertEqual(actual, expected)

    def test_invalid_input_zero(self):
        """Should raise a ValueError for input less than 1"""
        with self.assertRaises(ValueError):
            convert_int_to_roman(0)

    def test_invalid_input_large(self):
        """Should raise a ValueError for input greater than 3999"""
        with self.assertRaises(ValueError):
            convert_int_to_roman(4000)


if __name__ == "__main__":
    unittest.main()
