#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in_one function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2/1/2025
Author: Aziz Azizi
"""

import unittest

from ..repeat_character import repeat_character


class TestRepeatCharacter(unittest.TestCase):
    """Test suite for the repeat_character function"""

    # Standard test cases
    def test_aziz_z(self):
        """It should repeat z 3 times in Aziz"""
        self.assertEqual(repeat_character("Aziz", "z", 3), "Azzzizzz")
        # actual = repeat_character("Aziz", "z", 3)
        # expected = "Azzzizzz"

    def test_gray_r(self):
        """It should repeat r 5 times in Gray"""
        self.assertEqual(repeat_character("Gray", "r", 5), "Grrrrray")

    def test_repeat_char_upper(self):
        """It should repeat D 3 times in Hand and lower the D"""
        self.assertEqual(repeat_character("Hand", "D", 3), "Handdd")

    def test_repeat_char_lower(self):
        """It should repeat H 5 times in Hand and upper the h"""
        self.assertEqual(repeat_character("Hand", "h", 5), "HHHHHand")

    # Edge test cases
    def test_remove_char(self):
        """It should remove x from Azxxizxx"""
        self.assertEqual(repeat_character("Azxxizxx", "x", 0), "Aziz")

    def test_empty_argument(self):
        """It should return the original string"""
        self.assertEqual(repeat_character(), "")

    def test_empty_string(self):
        """It should return an empty string"""
        self.assertEqual(repeat_character("", "a", 2), "")

    def test_empty_repeat_char(self):
        """It should return the original string"""
        self.assertEqual(repeat_character("a", "", 6), "a")

    # Boundary test cases
    def test_goat_d(self):
        """It should not repeat d in Goat"""
        self.assertEqual(repeat_character("Goat", "d", 20), "Goat")

    def test_aziz_z_long(self):
        """It should repeat z 16 times in Aziz"""
        self.assertEqual(
            repeat_character("Aziz", "z", 16), "Azzzzzzzzzzzzzzzzizzzzzzzzzzzzzzzz"
        )

    # Defensive test cases
    def test_negative_input_n(self):
        """It should raise an error for negative n"""
        with self.assertRaises(AssertionError):
            repeat_character("Aziz", "z", -1)

    def test_invalid_input_type3(self):
        """It should raise an error for repeat char not being a single character"""
        with self.assertRaises(AssertionError):
            repeat_character("text", "long", 3)

    def test_invalid_input_type(self):
        """It should raise an error for text not being string"""
        with self.assertRaises(TypeError):
            repeat_character(123, "a", 3)

    def test_invalid_input_type2(self):
        """It should raise an error for repeat_char not being string"""
        with self.assertRaises(TypeError):
            repeat_character("text", 4, 6)

    def test_invalid_input_type4(self):
        """It should raise an error for n not being an integer"""
        with self.assertRaises(TypeError):
            repeat_character("Earth", "t", "g")
