#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the count_letters_and_digits function.
Contains comprehensive tests to verify the functionality of letter and digit counting.

Test categories:
    - Standard cases: typical sentences with letters and digits
    - Edge cases: sentences with special characters, empty strings
    - Defensive tests: invalid inputs (non-string types)

Created: 05/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Shaima Mohamed
"""

import unittest
from ..count_letters_and_digits import count_letters_and_digits


class TestLetterDigitCounter(unittest.TestCase):
    """Test the count_letters_and_digits function"""

    # Test Standard Cases
    def test_letters_and_digits(self):
        """It should count letters and digits correctly"""
        self.assertEqual(
            count_letters_and_digits("hello world! 123"), {"LETTERS": 10, "DIGITS": 3}
        )

    def test_only_letters(self):
        """It should count only letters correctly"""
        self.assertEqual(
            count_letters_and_digits("abcxyz"), {"LETTERS": 6, "DIGITS": 0}
        )

    def test_only_digits(self):
        """It should count only digits correctly"""
        self.assertEqual(count_letters_and_digits("12345"), {"LETTERS": 0, "DIGITS": 5})

    def test_special_characters(self):
        """It should return 0 for both letters and digits in special characters"""
        self.assertEqual(
            count_letters_and_digits("!@#$%^&*()"), {"LETTERS": 0, "DIGITS": 0}
        )

    # Test Edge Cases
    def test_empty_string(self):
        """It should return 0 for both letters and digits in an empty string"""
        self.assertEqual(count_letters_and_digits(""), {"LETTERS": 0, "DIGITS": 0})

    def test_mixed_special_chars_and_numbers(self):
        """It should count only letters and digits, ignoring special characters"""
        self.assertEqual(
            count_letters_and_digits("abc 123 !@#"), {"LETTERS": 3, "DIGITS": 3}
        )

    # Test Defensive Assertions
    def test_non_string_input(self):
        """It should raise an assertion error if input is not a string"""
        with self.assertRaises(AssertionError):
            count_letters_and_digits(123)

    def test_invalid_type_list(self):
        """It should raise AssertionError for list input"""
        with self.assertRaises(AssertionError):
            count_letters_and_digits([30])

    def test_invalid_type_none(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            count_letters_and_digits(None)


if __name__ == "__main__":
    unittest.main()
