#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Banu Ozyilmaz
Created on: 12-28-2024

This script contains unit tests for the factorial function using the unittest module.
"""

import unittest
from solutions.factorial import factorial

class TestFactorial(unittest.TestCase):
    """Unit tests for the factorial function"""

    # Standard test cases
    def test_base_case_0(self):
        """Test the base case: factorial(0) should return 1"""
        self.assertEqual(factorial(0), 1)

    # Small numbers test cases
    def test_small_numbers(self):
        """Test small positive numbers"""
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    # Medium numbers test cases
    def test_medium_numbers(self):
        """Test medium positive numbers"""
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(10), 3628800)

    # Edge test cases
    def test_edge_cases(self):
        """Test edge cases for large positive numbers"""
        self.assertEqual(factorial(12), 479001600)
        self.assertEqual(factorial(15), 1307674368000)
        self.assertEqual(factorial(20), 2432902008176640000)

    # Defensive test cases
    def test_negative_number(self):
        """Test negative number input: should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            factorial(-2)

    def test_non_integer_input(self):
        """Test non-integer input: should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            factorial(2.5)  # Testing with a float
        with self.assertRaises(AssertionError):
            factorial("string")  # Testing with a string
