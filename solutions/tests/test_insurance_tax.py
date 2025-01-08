#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for insurance_tax function.
Contains correct tests to help identify bugs in the implementation

Test categories:
- Standard cases: Different valid inputs.
- Edge cases: Boundary & Extreme conditions
- Defensive cases: Invalid inputs (types, values)

Created on 2025-01-04
Author: Nay Win Hlaing
"""

import unittest
from ..insurance_tax import insurance_tax


class Test_Insurance_tax(unittest.TestCase):
    """Test the insurance_tax function."""

    # Standard Cases
    def test_no_salary(self):
        """No salary should evaluate to no tax."""
        actual = insurance_tax(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_threshold(self):
        """Earnings of 183 and below should evaluate to 0 tax."""
        actual = insurance_tax(183)
        expected = 0
        self.assertEqual(actual, expected)

    def test_second_threshold(self):
        """Earnings between 183 and 962(inclusive) should
        evaluate to 12% tax on the salary in that portion."""
        actual = insurance_tax(962)
        expected = 93.48
        self.assertEqual(actual, expected)

    def test__third_threshold(self):
        """Earnings above 962 should evaluate to
        2% tax on the salary in that portion in addition to
        the 12% tax on the salary between 183 and 962(inclusive)"""
        actual = insurance_tax(963)
        expected = 93.5
        self.assertEqual(actual, expected)

    def test_round_down(self):
        """Function should work with float inputs.
        96.4536 should round down to 96.45"""
        actual = insurance_tax(961.78)
        expected = 93.45
        self.assertEqual(actual, expected)

    def test__round_up(self):
        """Function should work with float inputs.
        57.346 should round up to 57.35"""
        actual = insurance_tax(660.89)
        expected = 57.35
        self.assertEqual(actual, expected)

    # Edge Cases
    def test_edge_1(self):
        """0.01 should evaluate to 0 tax."""
        actual = insurance_tax(0.01)
        expected = 0
        self.assertEqual(actual, expected)

    def test_edge_2(self):
        """183.001 is in second threshold but the round up should result in 0.00"""
        actual = insurance_tax(183.001)
        expected = 0
        self.assertEqual(actual, expected)

    def test_edge_3(self):
        """183.001 is in second threshold and the round up should result in 0.01"""
        actual = insurance_tax(183.05)
        expected = 0.01
        self.assertEqual(actual, expected)

    def test_edge_4(self):
        """1 billion of salary should result in 20000074.24 tax"""
        actual = insurance_tax(1000000000)
        expected = 20000074.24
        self.assertEqual(actual, expected)

    # Defensive cases
    def test_non_float_input(self):
        """Non-float input raises a value error."""
        with self.assertRaises(ValueError):
            insurance_tax("100")

    def test_list_input(self):
        """List input raises a value error."""
        with self.assertRaises(ValueError):
            insurance_tax([100])

    def test_negative_number(self):
        """Negative number input raises a value error."""
        with self.assertRaises(ValueError):
            insurance_tax(-100)
