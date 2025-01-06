#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for is_palindrome function.
Contains tests for checking palindrome functionality with spaces, punctuation, and other edge cases.

Test categories:
    - Callable check: confirming the function can be called
    - Functionality tests: checking if the function correctly identifies palindromes
    and non-palindromes
    - Palindrome tests: typical palindromes with various punctuations and spaces
    - Non-palindrome tests: strings that are not palindromes, even with punctuation and spaces
    - Edge cases: empty strings, strings with only spaces, single, double characters
    and and case insensitivity
    - Defensive tests: incorrect input types such as booleans and non-string values


Created on 2024-12-30
Author: Huda Alamassi
"""

import unittest

from solutions.is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test the is_palindrome function."""

    def test_palindrome_string(self):
        """it should return True if you pass a palindrome string."""
        actual = is_palindrome("radar")
        self.assertEqual(actual, True)

    def test_non_palindrome_string(self):
        """it should return False if you pass a non-palindrome string."""
        actual = is_palindrome("hello")
        self.assertEqual(actual, False)

    def test_ignore_spaces_and_punctuation(self):
        """Test that the function ignores spaces and punctuation."""
        actual = is_palindrome("A man, a plan, a canal, Panama!")
        self.assertEqual(actual, True)

    def test_ignore_spaces_and_punctuation_2(self):
        """Test that the function handles spaces and punctuation in a different phrase."""
        actual = is_palindrome(
            "Are we not pure? “No, sir!” Panama’s moody Noriega brags. "
            "“It is garbage!” Irony dooms a man—a prisoner up to new era."
        )
        self.assertEqual(actual, True)

    def test_empty_string(self):
        """it should return False if you pass an empty string"""
        actual = is_palindrome("")
        self.assertEqual(actual, False)

    def test_space_string(self):
        """it should return False if you pass a string containing space"""
        actual = is_palindrome(" ")
        self.assertEqual(actual, False)

    def test_single_character(self):
        """it should return True if you pass a single character"""
        actual = is_palindrome("a")
        self.assertEqual(actual, True)

    def test_two_identical_characters(self):
        """it should return True if you pass two-character string with identical characters"""
        actual = is_palindrome("aa")
        self.assertEqual(actual, True)

    def test_string_with_identical_punctuation(self):
        """it should return False if you pass two identical punctuation characters"""
        actual = is_palindrome("!!")
        self.assertEqual(actual, False)

    def test_string_with_different_punctuation(self):
        """it should return False if you pass strings with different punctuation marks."""
        actual = is_palindrome("!?")
        self.assertEqual(actual, False)

    def test_case_insensitivity(self):
        """it should be case insensitive when the text is upper"""
        actual = is_palindrome("Level")
        self.assertEqual(actual, True)

    # test defensive assertions
    def test_defensive_assertion_for_integer_input(self):
        """Test that an assertion is raised if the input is an integer."""
        with self.assertRaises(AssertionError):
            is_palindrome(123321)  # input must be a string
