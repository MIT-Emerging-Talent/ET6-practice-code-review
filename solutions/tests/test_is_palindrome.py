#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A test for module is_palindrome.

Test categories:
    - Standard cases: palindromic and non-palindromic strings
    - Edge cases: empty string, single character
    - Defensive tests: assertions, wrong input types

Created on 8 1 2025
@author: Dadi Ishimwe
"""

import unittest
from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test the is_palindrome function"""

    def test_palindrome(self):
        """Test if 'racecar' is a palindrome"""
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        """Test if 'hello' is not a palindrome"""
        self.assertFalse(is_palindrome("hello"))

    def test_complex_palindrome(self):
        """Test if 'A man, a plan, a canal, Panama' is a palindrome"""
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

    def test_empty_string(self):
        """Test if an empty string is a palindrome"""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """Test if a single character is a palindrome"""
        self.assertTrue(is_palindrome("a"))

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            is_palindrome(None)

    def test_non_string_input(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            is_palindrome(123)
