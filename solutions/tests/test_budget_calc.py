#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" "
 created on 5 1 2025

@author: omer dafaalla
"""

import unittest

from solutions.budget_calc import (
    calculate_budget,
)  # Import the function from the budget module


class TestBudgetCalculation(unittest.TestCase):
    """
    Unit tests for the `calculate_budget` function.
    """

    def test_budget_3000(self):
        result = calculate_budget(3000)
        expected = [
            "Rent: 1200.00",
            "Groceries: 900.00",
            "Savings: 600.00",
            "Others: 300.00",
        ]
        self.assertEqual(result, expected)

    def test_budget_1500(self):
        result = calculate_budget(1500)
        expected = [
            "Rent: 600.00",
            "Groceries: 450.00",
            "Savings: 300.00",
            "Others: 150.00",
        ]
        self.assertEqual(result, expected)

    def test_budget_0(self):
        with self.assertRaises(ValueError):
            calculate_budget(0)

    def test_budget_3500(self):
        with self.assertRaises(ValueError):
            calculate_budget(3500)

    def test_budget_negative(self):
        with self.assertRaises(ValueError):
            calculate_budget(-1000)


if __name__ == "__main__":
    unittest.main()
