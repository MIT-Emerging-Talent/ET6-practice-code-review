#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6 1 2025

@author: omer dafaalla

"""

import unittest

from solutions.distance import calculate_distance


class TestCalculateDistance(unittest.TestCase):
    """Test cases for calculate_distance function."""

    def test_positive_coordinates(self):
        """Test with positive coordinates."""
        self.assertEqual(calculate_distance(0, 0, 3, 4), 5.0)
        self.assertEqual(calculate_distance(1, 1, 4, 5), 5.0)

    def test_negative_coordinates(self):
        """Test with negative coordinates."""
        self.assertEqual(calculate_distance(-1, -1, -4, -5), 5.0)

    def test_same_point(self):
        """Test when the points are the same."""
        self.assertEqual(calculate_distance(2, 3, 2, 3), 0.0)
