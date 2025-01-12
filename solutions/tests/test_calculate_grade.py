#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for calculate_grade function.

Created on 2025-01-08
@author: Karina
"""

import unittest
from calculate_grade import calculate_grade


class TestCalculateGrade(unittest.TestCase):
    """Test suite for the calculate_grade function."""

    # Test valid grades at boundaries
    def test_perfect_score(self):
        """Test perfect score of 100."""
        self.assertEqual(calculate_grade(100), "A")

    def test_minimum_a(self):
        """Test minimum A grade."""
        self.assertEqual(calculate_grade(90), "A")

    def test_maximum_b(self):
        """Test maximum B grade."""
        self.assertEqual(calculate_grade(89.9), "B")

    def test_minimum_b(self):
        """Test minimum B grade."""
        self.assertEqual(calculate_grade(80), "B")

    def test_maximum_c(self):
        """Test maximum C grade."""
        self.assertEqual(calculate_grade(79.9), "C")

    def test_minimum_c(self):
        """Test minimum C grade."""
        self.assertEqual(calculate_grade(70), "C")

    def test_maximum_d(self):
        """Test maximum D grade."""
        self.assertEqual(calculate_grade(69.9), "D")

    def test_minimum_d(self):
        """Test minimum D grade."""
        self.assertEqual(calculate_grade(60), "D")

    def test_maximum_f(self):
        """Test maximum F grade."""
        self.assertEqual(calculate_grade(59.9), "F")

    def test_zero_score(self):
        """Test score of zero."""
        self.assertEqual(calculate_grade(0), "F")

    # Test invalid inputs
    def test_negative_score(self):
        """Test that negative scores raise ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_grade(-1)
        self.assertEqual(str(context.exception), "Score must be between 0 and 100")

    def test_score_above_100(self):
        """Test that scores above 100 raise ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate_grade(101)
        self.assertEqual(str(context.exception), "Score must be between 0 and 100")

    def test_string_input(self):
        """Test that string input raises AssertionError."""
        with self.assertRaises(AssertionError) as context:
            calculate_grade("90")
        self.assertEqual(str(context.exception), "Score must be a number")

    def test_none_input(self):
        """Test that None input raises AssertionError."""
        with self.assertRaises(AssertionError) as context:
            calculate_grade(None)
        self.assertEqual(str(context.exception), "Score must be a number")

    # Test edge cases
    def test_float_score(self):
        """Test that float scores are handled correctly."""
        self.assertEqual(calculate_grade(89.99), "B")

    def test_dict_input(self):
    """Test that dict input raises AssertionError."""
    with self.assertRaises(AssertionError) as context:
        calculate_grade({"score": 90})
    self.assertEqual(str(context.exception), "Score must be a number")


if __name__ == "__main__":
    unittest.main()
