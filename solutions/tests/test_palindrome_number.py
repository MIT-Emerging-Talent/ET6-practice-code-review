#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/01/2025
@author: Dorcas Wanja Njeri
"""

import unittest
from ..Palindrome_Number import is_Palindrome_Number


class TestPalindromeNumber(unittest.TestCase):
    """Test the is_palindrome_number function"""

    def test_palindrome_number(self):
        """Should return True for a number that is a palindrome"""
        actual = is_Palindrome_Number(121)
        expected = True
        self.assertEqual(actual, expected)

    def test_negative_palindrome(self):
        """Should return False for a negative number (never a palindrome)"""
        actual = is_Palindrome_Number(-121)
        expected = False
        self.assertEqual(actual, expected)

    def test_non_palindrome_number(self):
        """Should return False for a number that is not a palindrome"""
        actual = is_Palindrome_Number(123)
        expected = False
        self.assertEqual(actual, expected)

    def test_single_digit_number(self):
        """Should return True for a single digit number (always a palindrome)"""
        actual = is_Palindrome_Number(5)
        expected = True
        self.assertEqual(actual, expected)

    def test_large_palindrome(self):
        """Should return True for a large palindrome number"""
        actual = is_Palindrome_Number(12321)
        expected = True
        self.assertEqual(actual, expected)

    def test_large_non_palindrome(self):
        """Should return False for a large non-palindrome number"""
        actual = is_Palindrome_Number(12345)
        expected = False
        self.assertEqual(actual, expected)

    def test_zero(self):
        """Should return True for zero (considered a palindrome)"""
        actual = is_Palindrome_Number(0)
        expected = True
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
