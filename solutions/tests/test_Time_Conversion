"""
Test module for Time Conversion function.
Contains intentionally buggy tests for debugging practice.

Created on 2024-01-09
Author: Safaa Osman
"""

import unittest
from ..Time_Conversion import Time_Conversion


class TestTimeConversion(unittest.TestCase):
    """Test suite for the Time Conversion function - contains buggy tests!"""

    def test_not_string(self):
        """It should raise AssertionError for input not string"""
        with self.assertRaises(AssertionError):
            Time_Conversion(1230)

    def test_hours_out_of_range(self):
        """It should raise AssertionError for hours are out of range"""
        with self.assertRaises(AssertionError):
            Time_Conversion("25:30")

    def test_minutes_out_of_range(self):
        """It should raise AssertionError for minutes are out of range"""
        with self.assertRaises(AssertionError):
            Time_Conversion("12:69")

    def test_strings(self):
        """It should return the time conversion properly"""
        self.assertEqual(Time_Conversion("12:12"), "20:12")

    def test_empty_string(self):
        """It should raise AssertionError for string is empty"""
        with self.assertRaises(AssertionError):
            Time_Conversion("")

    def test_mix_types(self):
        """It should raise ValueError solutions\tests\test_Time_Conversion for string is empty"""
        with self.assertRaises(ValueError):
            Time_Conversion("hg:45")
