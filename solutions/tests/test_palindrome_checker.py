#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for palindrome_checker function.

Created on 08 01 2025

@author : Osei Agyemang Sarfo
"""

import unittest

from solutions.palindrome_checker import palindrome_checker


class TestPalindromeChecker(unittest.TestCase):
    def test_positive_palindrome(self):
        """Test positive integers that are palindromes."""
        self.assertTrue(palindrome_checker(12321), "12321 should be a palindrome")

    def test_positive_non_palindrome(self):
        """Test positive integers that are not palindromes."""
        self.assertFalse(palindrome_checker(12345), "12345 should not be a palindrome")

    def test_negative_number(self):
        """Test negative numbers, which should raise an AssertionError."""
        with self.assertRaises(AssertionError):
            palindrome_checker(-121)

    def test_non_integer_input(self):
        """Test inputs that are not integers"""
        with self.assertRaises(AssertionError):
            palindrome_checker("121")

    def test_zero_input(self):
        """Test zero as input."""
        with self.assertRaises(AssertionError):
            palindrome_checker(0)

    def test_single_digit(self):
        """Test single-digit numbers, which are always palindromes by definition."""
        for i in range(1, 10):
            self.assertTrue(palindrome_checker(i), f"{i} should be a palindrome")


if __name__ == "__main__":
    unittest.main()
