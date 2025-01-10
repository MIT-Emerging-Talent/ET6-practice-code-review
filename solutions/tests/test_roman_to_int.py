"""
Test suite for the roman_to_int function.

This module provides a series of unit tests for the roman_to_int function 
to ensure it correctly converts Roman numerals to integers and handles 
invalid inputs appropriately.
"""

import sys

sys.path.insert(0, "/Users/mushtary/ET6-foundations-group-03/solutions")
import unittest
from solutions.roman_to_int import roman_to_int  # Correct import path


class TestRomanToInt(unittest.TestCase):
    """
    Test class for the roman_to_int function.

    This class contains unit tests for the roman_to_int function, covering both
    valid and invalid Roman numeral inputs.
    """

    def test_roman_to_int_III(self):
        """Test Roman numeral 'III'."""
        self.assertEqual(roman_to_int("III"), 3)

    def test_roman_to_int_IV(self):
        """Test Roman numeral 'IV'."""
        self.assertEqual(roman_to_int("IV"), 4)

    def test_roman_to_int_IX(self):
        """Test Roman numeral 'IX'."""
        self.assertEqual(roman_to_int("IX"), 9)

    def test_roman_to_int_LVIII(self):
        """Test Roman numeral 'LVIII'."""
        self.assertEqual(roman_to_int("LVIII"), 58)

    def test_roman_to_int_MCMXCIV(self):
        """Test Roman numeral 'MCMXCIV'."""
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)

    def test_roman_to_int_invalid_IIII(self):
        """Test invalid Roman numeral 'IIII'."""
        with self.assertRaises(ValueError):
            roman_to_int("IIII")

    def test_roman_to_int_invalid_ABC(self):
        """Test invalid non-Roman input 'ABC'."""
        with self.assertRaises(ValueError):
            roman_to_int("ABC")


if __name__ == "__main__":
    unittest.main()
