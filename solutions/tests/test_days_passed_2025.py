#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-12-25
@author:Alemayehu Desta
"""

import unittest
from datetime import datetime

from solutions.days_passed_2025 import days_passed_2025


class TestDaysPassed2025(unittest.TestCase):
    """Unit tests for the time_elapsed_2025 function."""

    def test_time_at_start_of_year(self):
        """Test the calculation at the very start of 2025."""
        test_date = datetime(2025, 1, 1, 0, 0, 0)
        self.assertEqual(days_passed_2025(test_date), 1)  # Expected output: 1

    def test_time_after_one_week(self):
        """Test the calculation after one week into 2025."""
        test_date = datetime(2025, 1, 8, 0, 0, 0)
        self.assertEqual(days_passed_2025(test_date), 8)  # Expected output: 8

    def test_time_mid_year(self):
        """Test the calculation in the middle of the year 2025."""
        test_date = datetime(2025, 6, 30, 12, 0, 0)
        self.assertEqual(days_passed_2025(test_date), 181)  # Expected output: 181

    def test_time_end_of_june(self):
        """Test the calculation at the end of June 2025."""
        test_date = datetime(2025, 6, 30, 23, 59, 59)
        self.assertEqual(days_passed_2025(test_date), 181)  # Expected output: 181

    def test_time_end_of_year(self):
        """Test the calculation at the very end of 2025."""
        test_date = datetime(2025, 12, 31, 23, 59, 59)
        self.assertEqual(days_passed_2025(test_date), 365)  # Expected output: 365

    def test_error_outside_2025(self):
        """Test that the function raises a ValueError outside the year 2025."""
        test_date = datetime(2024, 12, 31, 23, 59, 59)
        with self.assertRaises(ValueError):
            days_passed_2025(test_date)


if __name__ == "__main__":
    unittest.main()
