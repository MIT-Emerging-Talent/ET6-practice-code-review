
"""
Test module for Roman numeral to integer conversion.

Created on 2025-01-12

@author: Karina
"""

import unittest
from roman_to_int import roman_to_int


class TestRomanToInt(unittest.TestCase):
    """Test the roman_to_int function"""

    def test_single_numeral(self):
        """Test basic single Roman numerals"""
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('L'), 50)
        self.assertEqual(roman_to_int('C'), 100)
        self.assertEqual(roman_to_int('D'), 500)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_simple_addition(self):
        """Test simple additive combinations"""
        self.assertEqual(roman_to_int('II'), 2)
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('VI'), 6)
        self.assertEqual(roman_to_int('VII'), 7)
        self.assertEqual(roman_to_int('XIII'), 13)

    def test_subtraction_cases(self):
        """Test subtractive combinations"""
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)

    def test_complex_numbers(self):
        """Test complex Roman numerals"""
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)
        self.assertEqual(roman_to_int('MMXXIII'), 2023)

    def test_case_insensitive(self):
        """Test case insensitivity"""
        self.assertEqual(roman_to_int('iv'), 4)
        self.assertEqual(roman_to_int('xL'), 40)
        self.assertEqual(roman_to_int('McMxCiV'), 1994)

    def test_invalid_input(self):
        """Test invalid inputs"""
        with self.assertRaises(AssertionError):
            roman_to_int('')  # Empty string
        with self.assertRaises(AssertionError):
            roman_to_int('ABC')  # Invalid characters
        with self.assertRaises(AssertionError):
            roman_to_int(123)  # Non-string input


if __name__ == '__main__':
    unittest.main()