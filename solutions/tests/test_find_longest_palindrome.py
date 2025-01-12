#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the longest palindrome finder functionality.

This module contains unittest test cases for the find_longest_palindrome and
is_palindrome functions, including edge cases and invalid inputs.

Created on 28 12 2024
@author: Mahdia Ahmadi
"""

import unittest

from solutions.find_longest_palindrome import find_longest_palindrome, is_palindrome


class TestPalindromeFinder(unittest.TestCase):
    """
    Test suite for palindrome finding functions.

    This class contains unit tests for both the main palindrome finding function
    and its helper function, covering normal cases, edge cases, and error conditions.
    """

    def test_empty_string(self):
        """
        Test that an empty string returns an empty string.
        """
        self.assertEqual(find_longest_palindrome(""), "")

    def test_single_character(self):
        """
        Test that a single character string returns that character.
        """
        self.assertEqual(find_longest_palindrome("a"), "a")

    def test_two_same_characters(self):
        """
        Test string with two identical characters.
        """
        self.assertEqual(find_longest_palindrome("aa"), "aa")

    def test_two_different_characters(self):
        """
        Test string with two different characters returns first character.
        """
        self.assertEqual(find_longest_palindrome("ab"), "a")

    def test_simple_odd_palindrome(self):
        """
        Test finding a simple odd-length palindrome.
        """
        self.assertEqual(find_longest_palindrome("racecar"), "racecar")

    def test_simple_even_palindrome(self):
        """
        Test finding a simple even-length palindrome.
        """
        self.assertEqual(find_longest_palindrome("abba"), "abba")

    def test_multiple_palindromes(self):
        """
        Test string containing multiple palindromes returns the longest.
        """
        self.assertEqual(find_longest_palindrome("abbaracecarxy"), "racecar")

    def test_overlapping_palindromes(self):
        """
        Test string with overlapping palindromes.
        """
        self.assertEqual(find_longest_palindrome("abababa"), "abababa")

    def test_no_long_palindrome(self):
        """
        Test string with no palindromes longer than one character.
        """
        self.assertEqual(find_longest_palindrome("python"), "p")

    def test_case_sensitive(self):
        """
        Test that the function is case-sensitive.
        """
        self.assertNotEqual(find_longest_palindrome("Racecar"), "Racecar")

    def test_with_spaces(self):
        """
        Test string containing spaces.
        """
        self.assertEqual(find_longest_palindrome("race car"), "r")

    def test_with_special_characters(self):
        """
        Test string containing special characters.
        """
        self.assertEqual(find_longest_palindrome("a!@#a"), "a")

    # defensive testcase
    def test_invalid_input_type(self):
        """
        Test that non-string input raises an AssertionError.
        """
        with self.assertRaises(AssertionError):
            find_longest_palindrome(123)


class TestIsPalindrome(unittest.TestCase):
    """
    Test suite for the is_palindrome helper function.
    """

    def test_empty_string_palindrome(self):
        """
        Test that an empty string is considered a palindrome.
        """
        self.assertEqual(is_palindrome(""), True, "Empty string should be a palindrome")

    def test_single_char_palindrome(self):
        """
        Test that a single character is a palindrome.
        """
        self.assertEqual(
            is_palindrome("x"), True, "Single character should be a palindrome"
        )

    def test_simple_palindrome(self):
        """
        Test a simple palindrome string.
        """
        self.assertEqual(
            is_palindrome("level"), True, "The word 'level' should be a palindrome"
        )

    def test_non_palindrome(self):
        """
        Test a non-palindrome string.
        """
        self.assertEqual(
            is_palindrome("python"),
            False,
            "The word 'python' should not be a palindrome",
        )

    def test_palindrome_with_spaces(self):
        """
        Test that spaces affect palindrome detection.
        """
        self.assertEqual(
            is_palindrome("race car"),
            False,
            "String with spaces should not be considered a palindrome",
        )


if __name__ == "__main__":
    unittest.main()
