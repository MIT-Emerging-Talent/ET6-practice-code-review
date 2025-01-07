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
        self.assertEqual(word_counter("Hello, World!"), 2)
        self.assertEqual(word_counter("Python is awesome!"), 3)
        self.assertEqual(word_counter("I love programming in Python."), 5)

    # Edge cases
    def test_empty_input(self):
        """It should return 0 for empty input."""
        self.assertEqual(word_counter(""), 0)

    # Defensive tests
    def test_wrong_input(self):
        """It should raise an AssertionError for wrong input types."""
        with self.assertRaises(AssertionError):
            word_counter(123)
        with self.assertRaises(AssertionError):
            word_counter(7.98)
