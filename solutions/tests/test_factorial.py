#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for factorial function.

@author: Saad M. Ashour
"""

import unittest
from solutions.factorial import factorial


class TestFactorial(unittest.TestCase):
    """
    Unit tests for the factorial function.

    The factorial function computes the factorial of a non-negative integer using recursion.
    These tests verify its correctness for various inputs,
    including edge cases, valid cases, and invalid cases.
    """


def test_factorial_zero(self):
    """It should evaluate 0 to 1"""
    actual = factorial(0)
    expected = 1
    self.assertEqual(actual, expected)


def test_factorial_one(self):
    """It should evaluate 1 to 1"""
    actual = factorial(1)
    expected = 1
    self.assertEqual(actual, expected)


def test_factorial_positive(self):
    """It should evaluate 5 to 120"""
    actual = factorial(5)
    expected = 120
    self.assertEqual(actual, expected)


def test_factorial_negative(self):
    """factorial of negative integer will raise Error"""
    with self.assertRaises(ValueError):
        factorial(-1)


def test_factorial_non_integer(self):
    """factorial of non integer will raise Error"""
    with self.assertRaises(TypeError):
        factorial(3.5)
    with self.assertRaises(TypeError):
        factorial("string")


if __name__ == "__main__":
    unittest.main()
