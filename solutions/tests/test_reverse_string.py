#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on 2025-01-01

@author: Jeffery Offei Darko
"""

import unittest

from ..reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    """Test the reverse_string function"""

    def test_empty_string(self):
        """It should return an empty string for an empty string"""
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        """It should return the same character for a single character"""
        self.assertEqual(reverse_string("a"), "a")

    def test_two_characters(self):
        """It should reverse two characters"""
        self.assertEqual(reverse_string("ab"), "ba")

    def test_palindrome(self):
        """It should return the same string for a palindrome"""
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_spaces_only(self):
        """It should return the same string for spaces only"""
        self.assertEqual(reverse_string("   "), "   ")

    def test_string_with_spaces(self):
        """It should reverse a string containing spaces"""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_numeric_string(self):
        """It should reverse a numeric string"""
        self.assertEqual(reverse_string("12345"), "54321")

    def test_mixed_case(self):
        """It should reverse a string with mixed case"""
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_special_characters(self):
        """It should reverse a string with special characters"""
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")

    def test_alphanumeric_string(self):
        """It should reverse an alphanumeric string"""
        self.assertEqual(reverse_string("abc123"), "321cba")

    def test_unicode_characters(self):
        """It should reverse a string with Unicode characters"""
        self.assertEqual(
            reverse_string("\u3053\u3093\u306b\u3061\u306f"),
            "\u306f\u3061\u306b\u3093\u3053",
        )

    def test_leading_and_trailing_spaces(self):
        """It should reverse a string with leading and trailing spaces"""
        self.assertEqual(reverse_string("  hello  "), "  olleh  ")

    def test_string_with_numbers_and_spaces(self):
        """It should reverse a string containing numbers and spaces"""
        self.assertEqual(reverse_string("12 34 56"), "65 43 21")

    def test_long_string(self):
        """It should reverse a very long string"""
        long_string = "a" * 1000
        self.assertEqual(reverse_string(long_string), "a" * 1000)

    def test_string_with_whitespaces_in_front_of_string(self):
        """It should reverse a string with whitespaces in front of the string"""
        self.assertEqual(reverse_string(" hello"), "olleh ")

    def test_string_with_whitespaces_in_middle_of_string(self):
        """It should reverse a string with whitespaces in the middle of the string"""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_string_with_whitespaces_at_the_end_of_string(self):
        """It should reverse a string with whitespaces at the end of the string"""
        self.assertEqual(reverse_string(" hello "), " olleh ")

    def test_string_with_special_characters(self):
        """It should reverse a string with special characters"""
        self.assertEqual(reverse_string("a!b@c#d$e^f&g*j(h)"), ")h(j*g&f^e$d#c@b!a")

    def test_string_with_unicode_characters(self):
        """It should reverse a string with Unicode characters"""
        self.assertEqual(reverse_string("こんにちは"), "はちにんこ")

    def test_assertion_error_on_non_string(self):
        """It should raise an AssertionError for non-string inputs"""
        with self.assertRaises(AssertionError):
            reverse_string(12345)
