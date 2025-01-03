#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains unit tests to validate the functionality of the
`length_longest_substring` function.
It checks the length of the longest substring without repeating characters in a string.

Created on: 2025-01-03
Author: Jola-Moses
"""

import unittest
from solutions.length_longest_substring import length_longest_substring

class TestLengthLongestSubstring(unittest.TestCase):
    """Tests for length_longest_substring"""

    def test_basic_case(self):
        """Should return 3 for 'abcabcbb'."""
        self.assertEqual(length_longest_substring('abcabcbb'), 3)
