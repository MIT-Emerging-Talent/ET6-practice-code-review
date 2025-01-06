#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5 1 2025

@author: omer dafaalla
"""

import unittest

from budget_calc import calculate_budget


class TestCalculateBudget(unittest.TestCase):
    """
    Unit test class for the calculate_budget function.
    """

    def test_valid_budget(self):
        """
        Test with valid budget values.
        """
        self.assertEqual(
            calculate_budget(3000),
            ["Rent: 1200.0", "Groceries: 900.0", "Savings: 600.0", "Others: 300.0"],
        )
        self.assertEqual(
            calculate_budget(1500),
            ["Rent: 600.0", "Groceries: 450.0", "Savings: 300.0", "Others: 150.0"],
        )

    def test_boundary_budget(self):
        """
        Test with a boundary value (e.g.,
          maximum allowed 3000).
        """
        self.assertEqual(
            calculate_budget(3000),
            ["Rent: 1200.0", "Groceries: 900.0", "Savings: 600.0", "Others: 300.0"],
        )

    def test_invalid_budget_negative(self):
        """
        Test with a negative budget value.
        """
        with self.assertRaises(AssertionError):
            calculate_budget(-500)

    def test_invalid_budget_exceeds_limit(self):
        """
        Test with a budget exceeding
          the upper limit.
        """
        with self.assertRaises(AssertionError):
            calculate_budget(3500)

    def test_invalid_budget_type(self):
        """
        Test with a non-numeric type as input.
        """
        with self.assertRaises(AssertionError):
            calculate_budget("Not a number")
