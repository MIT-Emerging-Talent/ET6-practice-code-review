#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for factorial function

Module contents:
     to calculate the factorial of input numbers

Created on 02-01-2025
@author:Samir Ahmed Shaifta
"""

import unittest

from ..factorial import factorial


class TestFactorialFunction(unittest.TestCase):
    """Unit tests for the factorial function."""

    def test_factorial_of_5(self):
        """It should return 120 when the input is 5."""
        actual = factorial(5)
        expected = 120
        self.assertEqual(actual, expected)

    def test_factorial_of_0(self):
        """It should return 1 when the input is 0."""
        actual = factorial(0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_of_1(self):
        """It should return 1 when the input is 1."""
        actual = factorial(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_invalid_type(self):
        """It should raise TypeError when the input is not an integer."""
        with self.assertRaises(AssertionError):
            factorial(3.5)
        with self.assertRaises(AssertionError):
            factorial("string")
        with self.assertRaises(AssertionError):
            factorial([1, 2, 3])

    def test_factorial_negative(self):
        """It should raise ValueError when the input is negative."""
        with self.assertRaises(AssertionError):
            factorial(-1)
        with self.assertRaises(AssertionError):
            factorial(-10)
