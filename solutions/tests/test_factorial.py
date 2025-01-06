#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the factorial function.
Contains comprehensive tests to verify the factorial calculation.

Test categories:
    - Standard cases: typical values for factorial calculation
    - Edge cases: factorial of 10
    - Defensive tests: invalid inputs (non-integer types)

Created: 05/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Shaima Mohamed
"""

import unittest
from ..factorial import factorial


class TestFactorial(unittest.TestCase):
    """
    Unit tests for the factorial function.
    This module contains a collection of unit tests for the factorial function,
    which calculates the factorial of a given non-negative integer.
    """

    # Test Standard Cases
    def test_factorial_5(self):
        """It should calculate 5! as 120"""
        self.assertEqual(factorial(5), 120)

    def test_factorial_3(self):
        """It should calculate 3! as 6"""
        self.assertEqual(factorial(3), 6)

    def test_factorial_1(self):
        """It should calculate 1! as 1"""
        self.assertEqual(factorial(1), 1)

    def test_factorial_0(self):
        """It should calculate 0! as 1"""
        self.assertEqual(factorial(0), 1)

    # Test Edge Cases
    def test_large_factorial(self):
        """It should calculate the factorial of a large number"""
        self.assertEqual(factorial(10), 3628800)

    # Test Defensive Assertions
    def test_non_integer_input(self):
        """It should raise an assertion error if input is a string"""
        with self.assertRaises(AssertionError):
            factorial("5")

    def test_negative_integer(self):
        """It should raise an assertion error for negative integers"""
        with self.assertRaises(AssertionError):
            factorial(-5)

    def test_invalid_type_list(self):
        """It should raise an assertion error for list input"""
        with self.assertRaises(AssertionError):
            factorial([5])


if __name__ == "__main__":
    unittest.main()
