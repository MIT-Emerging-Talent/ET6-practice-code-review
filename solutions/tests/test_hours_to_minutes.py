#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the hours_to_minutes function.

Created on 04 Jan 2025

@author: Tosan Okome
"""

import unittest

from ..hours_to_minutes import hours_to_minutes


class TestHoursToMinutes(unittest.TestCase):
    """Test hours_to_minutes function"""

    def test_positive_integer_hours(self):
        """It should return 120"""
        actual = hours_to_minutes(2)
        expected = 120
        self.assertEqual(actual, expected)

    def test_positive_float_hours(self):
        """It should return 150"""
        actual = hours_to_minutes(2.5)
        expected = 150
        self.assertEqual(actual, expected)

    def test_zero_hours(self):
        """It should return 0"""
        actual = hours_to_minutes(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_negative_hours(self):
        """Negative hours should raise ValueError"""
        with self.assertRaises(ValueError):
            hours_to_minutes(-1)

    def test_invalid_type_string(self):
        """Strings should raise TypeError"""
        with self.assertRaises(TypeError):
            hours_to_minutes("two")

    def test_invalid_type_list(self):
        """Lists should raise TypeError"""
        with self.assertRaises(TypeError):
            hours_to_minutes([1, 2])
