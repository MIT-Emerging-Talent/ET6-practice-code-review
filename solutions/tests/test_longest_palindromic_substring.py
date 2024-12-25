"""
Unit tests for the longest_palindromic_substring module.

This module contains unit tests for the Solution class's
longest_palindrome method. The tests cover various input
cases, including common scenarios, edge cases, and strings
with palindromes of different lengths.
"""

import unittest
from solutions.longest_palindromic_substring import Solution

class TestLongestPalindromicSubstring(unittest.TestCase):
    """
    Unit tests for the Solution class's longest_palindrome method.
    The tests verify the functionality of the method with various input strings,
    including common cases, edge cases, and strings with palindromes of different lengths.
    """

    def setUp(self):
        """Set up the Solution instance for testing."""
        self.solution = Solution()

    def test_example_1(self):
        """
        Test for the input 'babad'.
        The expected result is either 'bab' or 'aba' because both are valid palindromic substrings.
        """
        result = self.solution.longest_palindrome("babad")
        self.assertIn(result, ["bab", "aba"])  # "bab" or "aba" are valid results

    def test_example_2(self):
        """
        Test for the input 'cbbd'.
        The expected result is 'bb', as it's the longest palindromic substring.
        """
        result = self.solution.longest_palindrome("cbbd")
        self.assertEqual(result, "bb")

    def test_single_char(self):
        """
        Test for a string with a single character 'a'.
        A single character is always a palindrome, so the expected result is 'a'.
        """
        result = self.solution.longest_palindrome("a")
        self.assertEqual(result, "a")

    def test_empty_string(self):
        """
        Test for an empty string.
        An empty string has no palindromes, so the expected result is an empty string.
        """
        result = self.solution.longest_palindrome("")
        self.assertEqual(result, "")

    def test_no_palindrome(self):
        """
        Test for a string with no palindromes longer than a single character.
        Input: 'abcdef' where no substring is a palindrome longer than a single character.
        Expected result: 'a' (the first character is the longest palindrome).
        """
        result = self.solution.longest_palindrome("abcdef")
        self.assertEqual(result, "a")

    def test_all_palindrome(self):
        """
        Test for a string where the whole string is a palindrome.
        Input: 'racecar' (the entire string is a palindrome).
        Expected result: 'racecar'.
        """
        result = self.solution.longest_palindrome("racecar")
        self.assertEqual(result, "racecar")

    def test_palindrome_at_end(self):
        """
        Test for a string where the longest palindrome is at the end of the string.
        Input: 'abacdfgdcaba' (the longest palindrome is 'aba' at the start and end).
        Expected result: 'aba'.
        """
        result = self.solution.longest_palindrome("abacdfgdcaba")
        self.assertEqual(result, "aba")

    def test_palindrome_with_spaces(self):
        """
        Test for a string with spaces.
        Input: 'a man a plan a canal panama' (the longest palindrome is 'a man a plan a canal panama').
        Expected result: 'a man a plan a canal panama'.
        """
        result = self.solution.longest_palindrome("a man a plan a canal panama")
        self.assertEqual(result, "a man a plan a canal panama")

    def test_long_string(self):
        """
        Test for a long string with a palindromic substring in the middle.
        Input: A large string with 'abcd' in the middle and a palindrome 'abba' around it.
        Expected result: 'abba'.
        """
        result = self.solution.longest_palindrome("a" * 1000 + "abba" + "a" * 1000)
        self.assertEqual(result, "abba")

    def test_palindrome_with_duplicates(self):
        """
        Test for a string with duplicate characters but a non-obvious palindrome.
        Input: 'abccba' (the whole string is a palindrome).
        Expected result: 'abccba'.
        """
        result = self.solution.longest_palindrome("abccba")
        self.assertEqual(result, "abccba")

if __name__ == '__main__':
    unittest.main()
