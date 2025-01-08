"""
This module contains unit tests for the `is_palindrome` function in `palindrome_checker.py`.

The `is_palindrome` function determines whether a string is a palindrome, ignoring spaces,
punctuation, and capitalization.
"""

import unittest

from ..palindrome_checker import is_palindrome


class TestPalindromeChecker(unittest.TestCase):
    """
    Unit tests for the `is_palindrome` function.
    """

    def test_palindromes(self):
        """
        Test cases where the input string is a palindrome.
        """
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome(""))

    def test_non_palindromes(self):
        """
        Test cases where the input string is not a palindrome.
        """
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Not a palindrome"))
        self.assertFalse(is_palindrome("Python Programming"))

    def test_edge_cases(self):
        """
        Test edge cases including single characters and strings with special characters.
        """
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("!!"))
        self.assertTrue(is_palindrome("Able , was I saw eLba"))


if __name__ == "__main__":
    unittest.main()
