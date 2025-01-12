#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-01-01

@author: Hiba Daffallah
"""

import unittest

from ..longest_substring import longest_substring


class TestLongestSubstring(unittest.TestCase):
    """Test the longest_substring function"""

    def test_empty_string(self):
        """Checks what will happen if the input is an empty
        string"""
        self.assertEqual(longest_substring(""), "")

    def test_one_char_repeated(self):
        """Checks what will happen if the input is a repeated
        character"""
        self.assertEqual(longest_substring("bbbbbb"), "b")

    def test_no_repitition(self):
        """Checks what will happen if the input didn't have
        repeated characters"""
        self.assertEqual(longest_substring("abcdef"), "abcdef")

    def test_repeated_substring(self):
        """Checks what will happen if the input conatins a
        repeated substring"""
        self.assertEqual(longest_substring("pwwkew"), "wke")

    def test_multiple_substring(self):
        """Checks what will happen if the input contains multiple
        substrings"""
        self.assertEqual(longest_substring("celelocceli"), "eloc")

    def test_input_numbers(self):
        """Checks what will happen if the input contains numbers"""
        self.assertEqual(longest_substring("991215888"), "2158")

    def test_input_conatins_numbers(self):
        """Checks what will happen if the input contains numbers"""
        self.assertEqual(longest_substring("9cort9kl9m"), "cort9kl")

    def test_input_non_string(self):
        """Checks what will happen if the input is not a string"""
        with self.assertRaises(AssertionError):
            longest_substring(["abc"])
