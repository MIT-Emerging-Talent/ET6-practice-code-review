#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for convert_bin_dec_hex function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: simple conversion, leading zeros, zero
    - Boundary test cases: large lists
    - Defensive tests: invalid inputs, assertions

Created on 3/1/2025
Author: Aziz Azizi
"""

import unittest

from ..convert_bin_dec_hex import convert_bin_dec_hex


class TestConvertBinDecHex(unittest.TestCase):
    """Test suite for the convert_bin_dec_hex function"""

    # Standard test cases
    def test_binary_to_decimal(self):
        """It should convert binary to decimal"""
        self.assertEqual(convert_bin_dec_hex(1010, 2, 10), "10")

    def test_binary_to_hex(self):
        """It should convert binary to hexadecimal"""
        self.assertEqual(convert_bin_dec_hex(1010, 2, 16), "A")

    def test_decimal_to_binary(self):
        """It should convert decimal to binary"""
        self.assertEqual(convert_bin_dec_hex(10, 10, 2), "1010")

    def test_hex_to_decimal(self):
        """It should convert hexadecimal to decimal"""
        self.assertEqual(convert_bin_dec_hex("A", 16, 10), "10")

    # Edge test cases
    def test_hex_to_decimal2(self):
        """It should convert hexadecimal to decimal"""
        self.assertEqual(convert_bin_dec_hex(10, 16, 10), "16")

    def test_hex_with_leading_zeros(self):
        """It should handle hexadecimal with leading zeros correctly"""
        self.assertEqual(convert_bin_dec_hex("0001", 16, 10), "1")

    def test_zero(self):
        """It should convert 0 to 0"""
        self.assertEqual(convert_bin_dec_hex(0, 16, 10), "0")

    # Boundary test cases
    def test_large_binary_to_decimal(self):
        """It should handle large binary numbers."""
        self.assertEqual(convert_bin_dec_hex(1111111111111111, 2, 10), "65535")

    def test_large_decimal_to_hexadecimal(self):
        """It should handle large decimal numbers."""
        self.assertEqual(convert_bin_dec_hex(1000000, 10, 16), "F4240")

    def test_large_hex_to_binary(self):
        """It should handle large hexadecimal numbers."""
        self.assertEqual(
            convert_bin_dec_hex("FFFFFF", 16, 2), "111111111111111111111111"
        )

    # Defensive test cases
    def test_no_argument_to_convert(self):
        """It should handle no argument to convert."""
        with self.assertRaises(ValueError):
            convert_bin_dec_hex()

    def test_invalid_digit(self):
        """It should handle invalid digits gracefully"""
        with self.assertRaises(ValueError):
            convert_bin_dec_hex(102, 2, 10)

    def test_invalid_target_base(self):
        """It should handle invalid target base gracefully"""
        with self.assertRaises(ValueError):
            convert_bin_dec_hex(10, 10, 20)

    def test_invalid_digit2(self):
        """It should handle invalid digits gracefully"""
        with self.assertRaises(ValueError):
            convert_bin_dec_hex("G", 16, 10)

    def test_invalid_source_base(self):
        """It should handle invalid source base gracefully"""
        with self.assertRaises(ValueError):
            convert_bin_dec_hex(10, "B", 16)

    def test_invalid_target_base2(self):
        """It should handle invalid target base gracefully"""
        with self.assertRaises(ValueError):
            convert_bin_dec_hex(10, 16, "A")
