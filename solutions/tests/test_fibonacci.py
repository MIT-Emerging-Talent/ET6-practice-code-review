#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_fibonacci.py

This module contains unit tests for the `generate_fibonacci` function, which generates
the Fibonacci sequence up to a given number of terms.

Author: Fahed Daibes
Date:  Jan 12 2025
Group: ET6-foundations-group-16

Tests:
- Valid inputs for various sequence lengths.
- Edge cases, such as n=0 and n=1.
- Invalid inputs, such as negative numbers and non-integer types.
"""

import unittest

from solutions.fibonacci import generate_fibonacci


def assert_fibonacci(expected, n):
    """
    Custom assertion function to compare the result of generate_fibonacci with the expected value.

    Parameters:
    - expected (list): The expected Fibonacci sequence.
    - n (int): The input number of terms.

    Raises:
    - AssertionError: If the result of generate_fibonacci does not match the expected value.
    """
    result = generate_fibonacci(n)
    assert result == expected, f"Expected {expected} for {n}, but got {result}."


class TestFibonacci(unittest.TestCase):
    """
    This test class contains unit tests for the `generate_fibonacci` function.

    Each test uses only one assertion with the custom `assert_fibonacci` function.
    """

    def test_zero_terms(self):
        """Test case for zero terms."""
        assert_fibonacci([], 0)

    def test_one_term(self):
        """Test case for one term."""
        assert_fibonacci([0], 1)

    def test_five_terms(self):
        """Test case for five terms."""
        assert_fibonacci([0, 1, 1, 2, 3], 5)

    def test_large_sequence(self):
        """Test case for a larger sequence."""
        assert_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 10)

    def test_negative_input(self):
        """Test case for negative input."""
        with self.assertRaises(AssertionError):
            generate_fibonacci(-3)

    def test_invalid_string(self):
        """Test case for an invalid string input."""
        with self.assertRaises(AssertionError):
            generate_fibonacci("ten")

    def test_invalid_float(self):
        """Test case for an invalid float input."""
        with self.assertRaises(AssertionError):
            generate_fibonacci(3.5)


if __name__ == "__main__":
    unittest.main()
