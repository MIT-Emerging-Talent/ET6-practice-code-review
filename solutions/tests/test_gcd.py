# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_gcd.py

This module contains unit tests for the `gcd` function, which calculates the
greatest common divisor (GCD) of two integers.

Author: Fahed Daibes
Date: Jan 12 2025
Group: ET6-foundations-group-16

Tests:
- Valid inputs, including positive, negative, and zero values.
- Invalid inputs, such as non-integer types.
"""

import unittest

from solutions.gcd import gcd


def assert_gcd(expected, a, b):
    """
    Custom assertion function to compare the result of gcd with the expected value.

    Parameters:
    - expected (int): The expected GCD.
    - a (int): The first input integer.
    - b (int): The second input integer.

    Raises:
    - AssertionError: If the result of gcd does not match the expected value.
    """
    result = gcd(a, b)
    assert result == expected, (
        f"Expected {expected} for gcd({a}, {b}), but got {result}."
    )


class TestGCD(unittest.TestCase):
    """
    This test class contains unit tests for the `gcd` function.

    Each test uses only one assertion with the custom `assert_gcd` function.
    """

    def test_gcd_positive_numbers(self):
        """Test case for two positive numbers."""
        assert_gcd(6, 48, 18)

    def test_gcd_coprime_numbers(self):
        """Test case for two coprime numbers."""
        assert_gcd(1, 101, 103)

    def test_gcd_one_zero(self):
        """Test case for one number being zero."""
        assert_gcd(25, 0, 25)

    def test_gcd_both_zero(self):
        """Test case for both numbers being zero."""
        assert_gcd(0, 0, 0)

    def test_gcd_negative_numbers(self):
        """Test case for negative numbers."""
        assert_gcd(6, -48, -18)

    def test_gcd_mixed_signs(self):
        """Test case for one positive and one negative number."""
        assert_gcd(6, 48, -18)

    def test_invalid_string_input(self):
        """Test case for a string input."""
        with self.assertRaises(AssertionError):
            gcd("forty-eight", 18)

    def test_invalid_float_input(self):
        """Test case for a float input."""
        with self.assertRaises(AssertionError):
            gcd(48.5, 18)


if __name__ == "__main__":
    unittest.main()
