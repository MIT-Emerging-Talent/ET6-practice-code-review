#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test for word_counter function.
Test categories:
    - Standard cases: typical words, sentences
    - Edge cases: empty input, empty string
    - Defensive tests: wrong input types, assertions
Created on 2025-01-07
@author: Collins Ochieng
"""

import unittest

from ..word_counter import word_counter


class TestWordCounter(unittest.TestCase):
    """Unit test for word_counter function."""

    # Standard test cases
    def test_regular_sentence(self):
        """It should return the number of words in a regular sentence."""
        self.assertEqual(word_counter("MIT emerging talent"), 3)
        self.assertEqual(word_counter("Python is awesome!"), 3)

    # Edge cases
    def test_empty_input(self):
        """It should return 0 for empty input."""
        self.assertEqual(word_counter(""), 0)

    def test_extra_spaces(self):
        """It should return 0 for empty input."""
        self.assertEqual(word_counter("     I love    Programming   in Python   "), 5)

    # Defensive tests
    def test_integer_input(self):
        """It should raise an AssertionError for wrong input types."""
        with self.assertRaises(AssertionError):
            word_counter(123)

    def test_list_input(self):
        """It should raise an AssertionError for wrong input types."""
        with self.assertRaises(AssertionError):
            word_counter(["Collins", "Ochieng", "Python"])

    def test_dict_input(self):
        """It should raise an AssertionError for wrong input types."""
        with self.assertRaises(AssertionError):
            word_counter({"Name": "Collins", "Language": "Python"})
