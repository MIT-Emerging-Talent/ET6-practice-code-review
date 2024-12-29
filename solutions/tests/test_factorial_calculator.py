#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for factorial_calculator function.
Contains comprehensive tests to ensure correctness
of the factorial function.

Test categories:
    - Standard cases: Positive integers
    - Edge cases: zero factorial, one factorial, whole floats, large integers
    - Defensive tests: negative inputs, none-whole floats, non-integer input, none input

Created on 29-12-2024
Author: Linah Khayri
"""

import unittest

from ..factorial_calculator import factorial_calculator


class TestFactorialCalculator(unittest.TestCase):
    """Test suite for the factorial_calculator function that handle different cases"""

    # Standard Cases
    def test_factorial_2(self):
        """It should calculate the factorial of 2 as it's a positive integer"""
        self.assertEqual(factorial_calculator(2), 2)

    def test_factorial_3(self):
        """It should calculate the factorial of 3 as it's a positive integer"""
        self.assertEqual(factorial_calculator(3), 6)

    def test_factorial_4(self):
        """It should calculate the factorial of 4 as it's a positive integer"""
        self.assertEqual(factorial_calculator(4), 24)

    def test_factorial_5(self):
        """It should calculate the factorial of 5 as it's a positive integer"""
        self.assertEqual(factorial_calculator(5), 120)

    def test_factorial_6(self):
        """It should calculate the factorial of 6 as it's a positive integer"""
        self.assertEqual(factorial_calculator(6), 720)

    def test_factorial_8(self):
        """It should calculate the factorial of 8 as it's a positive integer"""
        self.assertEqual(factorial_calculator(8), 40320)

    def test_factorial_12(self):
        """It should calculate the factorial of 12 as it's a positive integer"""
        self.assertEqual(factorial_calculator(12), 479001600)

    # Edge cases
    def test_factorial_0(self):
        """It should return 1 as a base case of this function and special factorial case"""
        self.assertEqual(factorial_calculator(0), 1)

    def test_factorial_1(self):
        """It should return 1 as a base case of this function and special factorial case"""
        self.assertEqual(factorial_calculator(1), 1)

    def test_factorial_whole_float(self):
        """It should handle whole floats and return the factorial as an integer"""
        self.assertEqual(factorial_calculator(7.0), 5040)
