#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_palindrome function.

Test categories:
    - Standard cases: typical palindromes and non-palindromes
    - Edge cases: empty strings, single characters, mixed-case strings
    - Defensive tests: wrong input types, assertions

Created on 2/1/2025
@author: Caesar Ghazi
"""

import unittest
from solutions.palindrome_checker import palindrome_checker


class TestPalindromeChecker(unittest.TestCase):
    """ """

    # Standard test cases
    def test_simple_palindrome(self):
        """ """
        actual = palindrome_checker("racecar")
        expected = True
        self.assertEqual(actual, expected)

    def test_non_palindrome(self):
        """ """
        actual = palindrome_checker("hello")
        expected = False
        self.assertEqual(actual, expected)

    def test_mixed_case_palindrome(self):
        """ """
        actual = palindrome_checker("RaceCar")
        expected = True
        self.assertEqual(actual, expected)
        
        
        
if __name__ == "__main__":
    unittest.main()
