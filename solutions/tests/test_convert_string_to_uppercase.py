#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the convert_string_to_uppercase function

Created on 29 Dec 2024
@author: Noorelsalam Almakki
"""

import unittest

from ..convert_string_to_uppercase import convert_string_to_uppercase


class TestConvertStringToUppercase(unittest.TestCase):
    """A class for testing the convert_string_to_uppercase function"""

    def test_empty_string(self):
        """Test the convert_string_to_uppercase function with an empty string"""
        self.assertEqual(convert_string_to_uppercase(""), "")

    def test_lowercase_string(self):
        """Test the convert_string_to_uppercase function with a lowercase string"""
        self.assertEqual(convert_string_to_uppercase("hello"), "HELLO")

    def test_uppercase_string(self):
        """Test the convert_string_to_uppercase function with an uppercase string"""
        self.assertEqual(convert_string_to_uppercase("WORLD"), "WORLD")

    def test_mixedcase_string(self):
        """Test the convert_string_to_uppercase function with a mixed case string"""
        self.assertEqual(convert_string_to_uppercase("HeLlO"), "HELLO")

    def test_multiple_lowercase_words_string(self):
        """Test the convert_string_to_uppercase function with a multiple words string"""
        self.assertEqual(
            convert_string_to_uppercase("emerging talent"), "EMERGING TALENT"
        )

    def test_multiple_uppercase_words_string(self):
        """Test the convert_string_to_uppercase function with a multiple words string"""
        self.assertEqual(
            convert_string_to_uppercase("EMERGING TALENT"), "EMERGING TALENT"
        )

    def test_multiple_mixedcase_words_string(self):
        """Test the convert_string_to_uppercase function with a multiple words string"""
        self.assertEqual(
            convert_string_to_uppercase("EmERGing TaLEnt PrOgrAm"),
            "EMERGING TALENT PROGRAM",
        )

    def test_string_with_numbers(self):
        """Test the convert_string_to_uppercase function with a string containing numbers"""
        self.assertEqual(convert_string_to_uppercase("hello123"), "HELLO123")

    def test_string_with_special_characters(self):
        """Test the convert_string_to_uppercase function with a string containing special characters"""
        self.assertEqual(
            convert_string_to_uppercase("hello!@#$%^&*()"), "HELLO!@#$%^&*()"
        )

    def test_string_with_whitespace(self):
        """Test the convert_string_to_uppercase function with a string containing whitespace"""
        self.assertEqual(convert_string_to_uppercase(" hello "), " HELLO ")

    def test_digits_string(self):
        """Test the convert_string_to_uppercase function with a string containing digits"""
        self.assertEqual(convert_string_to_uppercase("123456"), "123456")

    def test_string_with_newline(self):
        """Test the convert_string_to_uppercase function with a string containing a newline character"""
        self.assertEqual(convert_string_to_uppercase("hello\nworld"), "HELLO\nWORLD")

    def test_string_with_only_whitespace(self):
        """Test the convert_string_to_uppercase function with a string with only whitespace"""
        self.assertEqual(convert_string_to_uppercase("   "), "   ")
