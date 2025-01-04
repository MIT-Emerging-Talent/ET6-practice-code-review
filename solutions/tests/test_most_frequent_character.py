#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for most_frequent_character function.
Contains tests for standard cases, edge cases, and defensive checks.

Test categories:
    - Standard cases: typical strings, tie cases, single character.
    - Edge cases: case-sensitivity,
Created on 2025-01-04
Author: Ava Abdullah
"""

import unittest
from ..most_frequent_character import most_frequent_character


class TestMostFrequentCharacter(unittest.TestCase):
    """Unit tests for most_frequent_character function"""

    # Standard test cases
    def test_single_most_frequent(self):
        """It should return the most frequent character in a typical string"""
        self.assertEqual(most_frequent_character("aabbbcc"), "b")

    def test_frequency_tie(self):
        """It should return the first character in case of a frequency tie"""
        self.assertEqual(most_frequent_character("abab"), "a")

    def test_single_character(self):
        """It should return the character itself for a single-character string"""
        self.assertEqual(most_frequent_character("z"), "z")
