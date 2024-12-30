"""Testing module for is_palindrome function
Contains tests for checking proper work of is_palindrome function

Created on 2024-12-30
Author Viktoriya Haiduk
"""

import unittest

from solutions.is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome(""))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("z"))

    def test_case_insensitive(self):
        self.assertTrue(is_palindrome("Level"))
        self.assertFalse(is_palindrome("Python"))

    def test_whitespace(self):
        processed_string = "A man a plan a canal Panama".replace(" ", "").lower()
        self.assertTrue(is_palindrome(processed_string))
        self.assertFalse(is_palindrome("Not a palindrome"))


if __name__ == "__main__":
    unittest.main()
