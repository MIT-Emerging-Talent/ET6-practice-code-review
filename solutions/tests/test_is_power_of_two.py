#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-31
@author: Gennadii Ershov
"""

import unittest

from ..is_power_of_two import is_power_of_two


class TestIsPowerOfTwo(unittest.TestCase):
    """Test the is_power_of_two function"""

    def test_single_is_power_of_two(self):
        """Test if n = 1 is correctly identified as a power of two."""
        self.assertTrue(is_power_of_two(1), "Expected True for n = 1 (2^0 = 1)")
