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

    def test_small_numbers(self):
        """Test small positive numbers"""
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_medium_numbers(self):
        """Test medium positive numbers"""
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(10), 3628800)

    def test_large_numbers(self):
        """Test large positive numbers"""
        self.assertEqual(factorial(12), 479001600)
        self.assertEqual(factorial(15), 1307674368000)
        self.assertEqual(factorial(20), 2432902008176640000)

    # Edge cases
    def test_edge_cases(self):
        """Test edge cases for very large positive numbers"""
        self.assertEqual(factorial(30), 265252859812191058636308480000000)
        self.assertEqual(
            factorial(50),
            30414093201713378043612608166064768844377641568960512000000000000,
        )

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


if __name__ == "__main__":
    unittest.main()
