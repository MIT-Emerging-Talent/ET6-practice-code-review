#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for reverse_a_string function.
Contains comprehensive tests to verify string reversal functionality.

Test categories:
    - Standard cases: typical strings (basic reversal functionality)
    - Edge cases: empty strings, palindromes, large strings
    - Defensive tests: invalid inputs (non-string types)

"""
import unittest

from ..reverse_a_string import reverse_a_string



class TestReverseAString(unittest.TestCase):
    def test_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_a_string(""), "")

    def test_single_character(self):
        """Test reversing a string with a single character."""
        self.assertEqual(reverse_a_string("a"), "a")

    def test_multiple_characters(self):
        """Test reversing a string with multiple characters."""
        self.assertEqual(reverse_a_string("welcome"), "emoclew")

    def test_palindrome(self):
        """Test reversing a palindrome."""
        #Edge case: Palindrome should equal itself when reversed.
        self.assertEqual(reverse_a_string("repaper"), "repaper")

    def test_numbers_and_special_characters(self):
        """Test reversing a string containing numbers and special characters."""
        self.assertEqual(reverse_a_string("789!@#"), "#@!987")

    def test_mixed_case(self):
        """Test reversing a string with mixed case characters."""
        self.assertEqual(reverse_a_string("TryAgain!"), "!niagAyrT")

    def test_whitespace(self):
        """Test reversing a string with multiple spaces."""
        # Verifies whitespace preservation and positioning.
        self.assertEqual(reverse_a_string("  move forward  "), "  drawrof evom  ")

    def test_large_string(self):
        """Test reversing a very large string."""
        large_string = "a" * 10
        self.assertEqual(reverse_a_string(large_string), large_string[::-1])

    def test_only_whitespace(self):
        """Test reversing a string that contains only whitespace."""
        #Edge case: Verifies handling of strings with only spaces.
        self.assertEqual(reverse_a_string("    "), "    ")

    def test_non_string_input(self):
        """Test handling of non-string input."""
        with self.assertRaises(TypeError):
            reverse_a_string(12345)

    def test_none_input(self):
        """Test handling of None as input."""
        with self.assertRaises(TypeError):
            reverse_a_string(None)

    def test_boolean_input(self):
        """Test handling of boolean input."""
        with self.assertRaises(TypeError):
            reverse_a_string(True)
