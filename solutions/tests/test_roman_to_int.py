import unittest
from solutions.Roman_to_Int import romanToInt  # Correct import path


class TestRomanToInt(unittest.TestCase):
    def test_roman_to_int(self):
        # Test valid Roman numerals
        self.assertEqual(romanToInt("III"), 3)  # 3 in Roman numerals
        self.assertEqual(romanToInt("IV"), 4)  # 4 in Roman numerals
        self.assertEqual(romanToInt("IX"), 9)  # 9 in Roman numerals
        self.assertEqual(romanToInt("LVIII"), 58)  # 58 in Roman numerals
        self.assertEqual(romanToInt("MCMXCIV"), 1994)  # 1994 in Roman numerals

    def test_invalid_input(self):
        # Test invalid Roman numerals
        with self.assertRaises(ValueError):  # Expect ValueError for invalid inputs
            romanToInt("IIII")  # Invalid Roman numeral
        with self.assertRaises(ValueError):  # Expect ValueError for invalid inputs
            romanToInt("ABC")  # Non-Roman input


if __name__ == "__main__":
    unittest.main()
