#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_power_of_two function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2024-12-31
@author: Gennadii Ershov
"""

import unittest

from ..is_power_of_two import is_power_of_two


class TestIsPowerOfTwo(unittest.TestCase):
    """Test the is_power_of_two function"""

    # Standard test cases
    def test_single_is_power_of_two(self):
        """Test if n = 1 is correctly identified as a power of two."""
        self.assertTrue(is_power_of_two(1), "Expected True for n = 1 (2^0 = 1)")

    def test_large_power_of_two(self):
        """Test if n = 16 is correctly identified as a power of two."""
        self.assertTrue(is_power_of_two(16), "Expected True for n = 16 (2^4 = 16)")

    def test_non_power_of_two(self):
        """Test if n = 3 is correctly identified as not a power of two."""
        self.assertFalse(
            is_power_of_two(3), "Expected False for n = 3 (not a power of two)"
        )

    # Edge cases
    def test_zero(self):
        """Test if n = 0 is correctly identified as not a power of two."""
        self.assertFalse(is_power_of_two(0), "Expected False for n = 0")

    def test_negative_number(self):
        """Test if n = -2 is correctly identified as not a power of two."""
        self.assertFalse(is_power_of_two(-2), "Expected False for n = -2")

    def test_float_power_of_two(self):
        """Test if n = 16.0 is correctly identified as a power of two."""
        self.assertTrue(is_power_of_two(16.0), "Expected True for n = 16.0")

    def test_float_non_power_of_two(self):
        """Test if n = 3.5 is correctly identified as not a power of two."""
        self.assertFalse(is_power_of_two(3.5), "Expected False for n = 3.5")
