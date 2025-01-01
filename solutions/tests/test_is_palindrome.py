#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Testing module for is_palindrome function
Contains tests for checking proper work of is_palindrome function

Created on 2024-12-30
Author Viktoriya Haiduk
"""

import unittest

from solutions.is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_level(self):
        self.assertTrue(is_palindrome("level"))

    def test_palindrome_radar(self):
        self.assertTrue(is_palindrome("radar"))

    def test_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))

    def test_not_palindrome_hello(self):
        self.assertFalse(is_palindrome("hello"))

    def test_not_palindrome_world(self):
        self.assertFalse(is_palindrome("world"))

    def test_single_character_a(self):
        self.assertTrue(is_palindrome("a"))

    def test_single_character_z(self):
        self.assertTrue(is_palindrome("z"))

    def test_case_insensitive_level(self):
        self.assertTrue(is_palindrome("Level"))

    def test_case_insensitive_python(self):
        self.assertFalse(is_palindrome("Python"))

    def test_whitespace_palindrome(self):
        processed_string = "A man a plan a canal Panama".replace(" ", "").lower()
        self.assertTrue(is_palindrome(processed_string))

    def test_whitespace_not_palindrome(self):
        self.assertFalse(is_palindrome("Not a palindrome"))


if __name__ == "__main__":
    unittest.main()
