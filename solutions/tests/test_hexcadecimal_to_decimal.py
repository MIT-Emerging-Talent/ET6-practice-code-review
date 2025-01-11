#!/usr/bin/env python3
"""
Test module for hex_to_decimal function.

Test categories:
    - Standard cases: typical hexadecimal inputs
    - Defensive tests: invalid input types
"""

import unittest
from ..hexcadecimal_to_decimal import hex_to_decimal


"""Test suite for the hex_to_decimal function."""


# Standard test cases
def test_standard_hex(self):
    self.assertEqual(hex_to_decimal("1A"), 26)


def test_uppercase_hex(self):
    self.assertEqual(hex_to_decimal("FF"), 255)


def test_zero(self):
    self.assertEqual(hex_to_decimal("0"), 0)


# Defensive tests
def test_non_string_input(self):
    with self.assertRaises(AssertionError):
        hex_to_decimal(123)


def test_invalid_hex_input(self):
    with self.assertRaises(AssertionError):
        hex_to_decimal("G1")


if __name__ == "__main__":
    unittest.main()
