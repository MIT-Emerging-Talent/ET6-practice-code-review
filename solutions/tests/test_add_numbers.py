#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Test module for adding two numbers.

Created on 2025-01-07

Author: Martha Yelademe Nyekanga
"""

import unittest
from ..add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    """This class contains tests for the add_numbers function."""

    def test_add_two_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_positive_and_negative_numbers(self):
        """Test adding a positive and a negative number."""
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_add_zeros(self):
        """Test adding two zeros."""
        self.assertEqual(add_numbers(0, 0), 0)

    def test_add_two_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_numbers_string(self):
        """Test adding a string and a number."""
        with self.assertRaises(AssertionError):
            add_numbers("2", 3)
