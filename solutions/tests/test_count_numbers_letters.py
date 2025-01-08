#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides unit tests for the count_number_letters function.

Test Categories:
Regular Passing Cases - Tests with typical inputs
Rare or Edge Cases - Tests with empty lists, single elements, and duplicates
Defensive Cases - Tests that verify error handling for invalid inputs

Created on: 2025/1/6
Author: Hamidullah Rajabi
"""

import unittest
from ..count_numbers_letters import count_numbers_letters


class TestCountNumbersLetters(unittest.TestCase):
    """
    Unit tests for the count_numbers_letters function.
    """

    # Regular Passing Cases

    def test_mixed_characters(self):
        """
        Test input containing both numbers and letters.
        """
        self.assertEqual(
            count_numbers_letters("@Hello123"), {"Numbers": 3, "Letters": 5, "Others": 1}
        )
    
    def test_only_special_characters(self):
        """
        Test input containing special characters only.
        """
        self.assertEqual(
            count_numbers_letters("$$$#@!"), {"Numbers": 0, "Letters": 0, "Others": 6}
        )

    def test_only_letters(self):
        """
        Test input containing only letters.
        """
        self.assertEqual(
            count_numbers_letters("Python"), {"Numbers": 0, "Letters": 6, "Others": 0}
        )

    def test_only_numbers(self):
        """
        Test input containing only numbers.
        """
        self.assertEqual(
            count_numbers_letters("2025"), {"Numbers": 4, "Letters": 0, "Others": 0}
        )

    # Rare or Edge Cases

    def test_empty_string(self):
        """
        Test with an empty string input.
        """
        self.assertEqual(
            count_numbers_letters(""), {"Numbers": 0, "Letters": 0, "Others": 0}
        )

    def test_special_characters(self):
        """
        Test input containing special characters.
        """
        self.assertEqual(
            count_numbers_letters("@123!aB"), {"Numbers": 3, "Letters": 2, "Others": 2}
        )

    # Defensive Cases That Raises Error

    def test_with_none_input(self):
        """
        Test input with None.
        """
        with self.assertRaises(ValueError):
            count_numbers_letters(None)

    def test_with_non_string_input(self):
        """
        Test input with non-string types.
        """
        with self.assertRaises(AssertionError):
            count_numbers_letters(12345)

    def test_with_list_input(self):
        """
        Test input with a list instead of a string.
        """
        with self.assertRaises(ValueError):
            count_numbers_letters(["a", "b", "c"])

    def test_longer_than_max_length_input(self):
        """
        Test input exceeding the maximum length.
        """
        with self.assertRaises(AssertionError):
            count_numbers_letters("a" * 101)
