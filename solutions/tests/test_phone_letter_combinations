#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for phone_letter_combinations function.

Created on 2024-12-30
Author: Hiba Daffallah
"""

import unittest

from solutions.phone_letter_combinations import phone_letter_combinations


class TestPhoneLetterCombinations(unittest.TestCase):
    """Test phone_letter_combinations function"""

    def test_numbers_within_range(self):
        """It should return all the possible letter combinations for 2,3"""
        self.assertEqual(
            phone_letter_combinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )

    def test_empty(self):
        """It should return empty list"""
        self.assertEqual(phone_letter_combinations(""), [])

    def test_single_number(self):
        """It should return all the  letters for 2"""
        self.assertEqual(phone_letter_combinations("2"), ["a", "b", "c"])

    def test_numbers_out_of_range(self):
        """It should return a message"""
        with self.assertRaises(AssertionError) as context:
            phone_letter_combinations("1")
        self.assertEqual(
            str(context.exception), "Input must only contain digits from 2 to 9."
        )

    def test_contains_numbers_out_of_range(self):
        """It should return a message"""
        with self.assertRaises(AssertionError) as context:
            phone_letter_combinations("12")
            self.assertEqual(
                str(context.exception), "Input must only contain digits from 2 to 9."
            )

    # Defensive tests
    def test_none_input(self):
        """It should raise AssertionError for non-integer input"""
        with self.assertRaises(AssertionError):
            phone_letter_combinations("b")


if __name__ == "__main__":
    unittest.main()
