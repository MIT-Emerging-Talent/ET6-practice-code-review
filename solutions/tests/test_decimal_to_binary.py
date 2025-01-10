#!/usr/bin/env python3

"""
A module for unit testing the decimal to binary converter.

Module contents:
    - TestDecimalToBinary: Unit test for the decimal_to_binary function.

Author: Anas Ziadah
Created: 2025-01-07
"""

import unittest
import os
from solutions.decimal_to_binary import decimal_to_binary


# Debugging: Print current working directory to ensure proper location
print("Current working directory:", os.getcwd())


class TestDecimalToBinary(unittest.TestCase):
    """Unit tests for the decimal_to_binary function."""

    def test_conversion_10(self):
        """Test that decimal 10 is correctly converted to binary '1010'."""
        self.assertEqual(decimal_to_binary(10), "1010")

    def test_conversion_5(self):
        """Test that decimal 5 is correctly converted to binary '101'."""
        self.assertEqual(decimal_to_binary(5), "101")

    def test_conversion_0(self):
        """Test that decimal 0 is correctly converted to binary '0'."""
        self.assertEqual(decimal_to_binary(0), "0")

    def test_conversion_255(self):
        """Test that decimal 255 is correctly converted to binary '11111111'."""
        self.assertEqual(decimal_to_binary(255), "11111111")

    def test_conversion_large_number(self):
        """Test that a large decimal number is correctly converted to binary."""
        self.assertEqual(decimal_to_binary(1024), "10000000000")

    def test_extremely_large_number(self):
        """Test that an extremely large decimal number is correctly converted to binary."""
        self.assertEqual(decimal_to_binary(2**100), "1" + "0" * 100)

    def test_negative_number(self):
        """Test that a negative number raises an error (since negative numbers aren't supported)."""
        with self.assertRaises(ValueError):
            decimal_to_binary(-10)

    def test_non_integer_float(self):
        """Test that passing a float raises a TypeError."""
        with self.assertRaises(TypeError):
            decimal_to_binary(10.5)

    def test_non_integer_string(self):
        """Test that passing a string raises a TypeError."""
        with self.assertRaises(TypeError):
            decimal_to_binary("10")

    def test_non_integer_none(self):
        """Test that passing None raises a TypeError."""
        with self.assertRaises(TypeError):
            decimal_to_binary(None)


if __name__ == "__main__":
    unittest.main()
