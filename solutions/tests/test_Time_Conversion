"""
Test module for alternate_elements function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2024-12-06
Author: Claude AI
"""

import unittest
from ..Time_Conversion import Time_Conversion


class TestTimeConversion(unittest.TestCase):
    """Test suite for the Time Conversion function - contains buggy tests!"""

    # Standard test cases
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
