#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for is_palindrome function.

@author: Saad M. Ashour
"""

import unittest

from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """
    Unit tests for the is_palindrome function.

    These tests check various cases to ensure that the is_palindrome function correctly
    identifies palindromes, considering case insensitivity, non-alphanumeric characters,
    and other edge cases.
    """

    def test_palindrome(self):
        """
        Test cases where the string is a palindrome.
        """
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("Madam"))

    def test_non_palindrome(self):
        """
        Test cases where the string is not a palindrome.
        """
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    def test_empty_string(self):
        """
        Test case where the input is an empty string, which is considered a palindrome.
        """
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """
        Test case where the input is a single character, which is always a palindrome.
        """
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("1"))

    def test_only_non_alphanumeric(self):
        """
        Test case where the input contains only non-alphanumeric characters.
        The function should ignore them and return True for empty string.
        """
        self.assertTrue(is_palindrome("!@#$$@!"))


if __name__ == "__main__":
    unittest.main()
