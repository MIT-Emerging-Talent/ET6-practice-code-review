#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the count_character_occurrences function.

Created on 2024-12-30

@author: Sukhrob Muborakshoev
"""

import unittest

from solutions.count_character_occurrences import count_character_occurrences


class TestCharacterOccurrences(unittest.TestCase):
    """
    This class contains unit tests for the count_character_occurrences function.
    The function receives a string as an input and counts character occurrences that is provided as a second parameter.
    """

    def test_one_occurrence(self):
        """It should return 1 occurrence"""
        self.assertEqual(count_character_occurrences("pacific", "c"), 1)

    def test_several_occurrences(self):
        """It should return 2 occurrences"""
        self.assertEqual(count_character_occurrences("pacific", "i"), 2)

    def test_different_several_occurrences(self):
        """It should return 4 occurrences"""
        self.assertEqual(count_character_occurrences("mississippi", "s"), 4)

    def test_char_as_number(self):
        """It should return 4 occurrences"""
        self.assertEqual(count_character_occurrences("california", 3), 0)


if __name__ == "__main__":
    unittest.main()
