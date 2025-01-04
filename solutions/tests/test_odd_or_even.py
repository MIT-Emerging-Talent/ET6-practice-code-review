#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test module for odd_or_even function.
Test categories:
-Standards cases: typical odd numbers, even numbers
-Edge cases: 0, negative numbers
-Defensive tests: wrong input types, assertions
Created on 2025-01-03
Author: Solara Hamza
"""
import unittest
from ..odd_or_even import odd_or_even


class TestOddOrEven(unittest.TestCase):
    """Test suite for the odd_or_even function."""

    # Standard test cases
    def test_odd_number(self):
        """It should return 'odd' for odd numbers."""
        self.assertEqual(odd_or_even(1), "odd")
        self.assertEqual(odd_or_even(3), "odd")

    def test_even_number(self):
        """It should return 'even' for even numbers."""
        self.assertEqual(odd_or_even(2), "even")
        self.assertEqual(odd_or_even(4), "even")

    # Defensive tests
    def test_wrong_input(self):
        """It should raise TypeError for wrong input types."""
        with self.assertRaises(TypeError):
            odd_or_even("string")

    # Edge cases
    def test_zero(self):
        """It should return 'even' for 0."""
        self.assertEqual(odd_or_even(0), "even")

    def test_negative_number(self):
        """It should return 'odd' for negative numbers."""
        self.assertEqual(odd_or_even(-1), "odd")
        self.assertEqual(odd_or_even(-2), "even")
