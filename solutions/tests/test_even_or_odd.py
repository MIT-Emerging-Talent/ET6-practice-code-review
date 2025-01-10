#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides unit tests for the even_or_odd function.

Test Categories:
Regular Passing Cases - Tests with typical inputs
Rare or Edge Cases - Tests with empty lists, single elements, and duplicates
Defensive Cases - Tests that verify error handling for invalid inputs

Created on: 2025/8/6
Author: ZaidMazen1
"""

import unittest

from ..even_or_odd import even_or_odd


class TestEvenOrOdd(unittest.TestCase):
    """
    Unit tests for the even_or_odd function.
    """

    # Regular Passing Cases

    def test_even_number(self):
        """
        Tests with an even number.
        """
        self.assertEqual(even_or_odd(2), "Even")

    def test_odd_number(self):
        """
        Tests with an odd number.
        """
        self.assertEqual(even_or_odd(3), "Odd")

    def test_zero(self):
        """
        Tests with zero.
        """
        self.assertEqual(even_or_odd(0), "Even")

    # Rare or Edge Cases

    def test_large_even_number(self):
        """
        Tests with a large even number list.
        """
        self.assertEqual(even_or_odd(18325707324), "Even")

    def test_large_odd_number(self):
        """
        Tests with a large odd number.
        """
        self.assertEqual(even_or_odd(18325707325), "Odd")

    def test_negative_even_number(self):
        """
        Tests with a negative even number.
        """
        self.assertEqual(even_or_odd(-2), "Even")

    def test_negative_odd_number(self):
        """
        Tests with a negative odd number.
        """
        self.assertEqual(even_or_odd(-3), "Odd")

    # Defensive Cases

    def test_invalid_input(self):
        """
        Tests with an invalid input.
        """
        with self.assertRaises(AssertionError):
            even_or_odd("cat")

    def test_invalid_list_input(self):
        """
        Tests with an invalid list input.
        """
        with self.assertRaises(AssertionError):
            even_or_odd(["cat", "dog"])

    def test_invalid_list_element(self):
        """
        Tests with an invalid list element.
        """
        with self.assertRaises(AssertionError):
            even_or_odd([2, "dog"])
