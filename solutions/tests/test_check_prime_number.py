#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit Test for check_prime_number Function

This script contains a unit test for the `check_prime_number` function,
which checks whether a given number
is prime or not.
A prime number is a number greater than 1 that has no divisors other than 1 and itself.

The test class `TestIsPrime` includes various test cases to verify that the function works correctly
for different types of inputs:
- Prime numbers
- Non-prime numbers
- Edge cases (such as 0, 1, and negative numbers)
- Larger prime numbers

Test cases include:
- Testing prime numbers like 2, 3, 5, 7, 13.
- Testing non-prime numbers like 1, 4, 6, 8, 9, 10, 14.
- Checking edge cases such as 0 and negative numbers.

To run the tests, use the Python `unittest` framework.
The tests will provide feedback on the correctness
of the `check_prime_number` function.

Author: Özgür ÖZBEK
Date: 11th January 2025
Group: ET6-foundations-group-16

"""

import unittest
from ..check_prime_number import check_prime_number


class TestCheckPrimeNumber(unittest.TestCase):
    """Test case for the check_prime_number function."""

    def test_prime(self):
        """Test prime number 2."""
        self.assertTrue(check_prime_number(2))

    def test_prime_3(self):
        """Test prime number 3."""
        self.assertTrue(check_prime_number(3))

    def test_prime_5(self):
        """Test prime number 5."""
        self.assertTrue(check_prime_number(5))

    def test_prime_7(self):
        """Test prime number 7."""
        self.assertTrue(check_prime_number(7))

    def test_prime_13(self):
        """Test prime number 13."""
        self.assertTrue(check_prime_number(13))

    def test_non_prime_4(self):
        """Test non-prime number 4."""
        self.assertFalse(check_prime_number(4))

    def test_non_prime_6(self):
        """Test non-prime number 6."""
        self.assertFalse(check_prime_number(6))

    def test_non_prime_8(self):
        """Test non-prime number 8."""
        self.assertFalse(check_prime_number(8))

    def test_non_prime_9(self):
        """Test non-prime number 9."""
        self.assertFalse(check_prime_number(9))

    def test_non_prime_10(self):
        """Test non-prime number 10."""
        self.assertFalse(check_prime_number(10))

    def test_non_prime_14(self):
        """Test non-prime number 14."""
        self.assertFalse(check_prime_number(14))

    def test_edge_case_0(self):
        """Test edge case 0."""
        with self.assertRaises(AssertionError):
            check_prime_number(0)

    def test_edge_case_negative(self):
        """Test edge case negative number."""
        with self.assertRaises(AssertionError):
            check_prime_number(-1)

    def test_non_prime_1(self):
        """Test non-prime number 1."""
        with self.assertRaises(AssertionError):
            check_prime_number(1)

    def test_edge_case_large_prime(self):
        """Test edge case with large prime."""
        self.assertTrue(check_prime_number(97))


if __name__ == "__main__":
    unittest.main()
