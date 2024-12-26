#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for calculate percentage function

Created on 26.12.2024
@author: Yevheniia Rudenko
"""
import unittest

from ..calculate_percentage import calculate_percentage


class TestCalculatePercentage(unittest.TestCase):
    """Test the calculate_percentage function."""

    def test_positive_numbers(self):
        """It should return percentage for positive numbers"""
        self.assertEqual(calculate_percentage(50, 200), 25.0)

    def test_zero_part(self):
        """It should return 0% when the first number is zero"""
        self.assertEqual(calculate_percentage(0, 100), 0.0)

    def test_whole_zero(self):
        """It should raise ZeroDivisionError if the second number is zero"""
        with self.assertRaises(ZeroDivisionError):
            calculate_percentage(50, 0)

    def test_not_numbers(self):
        """It should raise AssertionError for non-numeric input"""
        with self.assertRaises(AssertionError):
            calculate_percentage("50", 100)
