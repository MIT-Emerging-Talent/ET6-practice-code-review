#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
Test module for only_even_numbers function

Created on 01.01.2025

@author: Anna Shumylina

"""

import unittest

from ..only_even_numbers import only_even_numbers


class TestOnlyNumbers(unittest.TestCase):
    """Test module for only_even_numbers function"""

    # Defensive test case
    def validate_input(text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")

    # Empty string test case
    def test_empty_string(self):
        self.assertEqual(only_even_numbers(""), [])

    # No numbers string test case
    def test_only_characters(self):
        self.assertEqual(only_even_numbers("Hello world!"), [])

    # Basic string test case
    def test_basic(self):
        self.assertEqual(
            only_even_numbers("22 kids and 7 dogs were packed into 2 vans."),
            ["22", "2"],
        )

    # Only odd numbers string test case
    def test_only_odd_numbers(self):
        self.assertEqual(only_even_numbers("11 dogs have 11 tails"), [])

    # Big numbers string test case
    def test_big_numbers(self):
        self.assertEqual(
            only_even_numbers("123467637823487234 and 57653264 and 5653482987"),
            ["123467637823487234", "57653264"],
        )
