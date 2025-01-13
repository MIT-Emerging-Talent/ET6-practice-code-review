#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6 1 2025

@author: omer dafaalla

"""

import unittest

from solutions.distance import calculate_distance


class TestCalculateDistance(unittest.TestCase):
    """
    Test cases for the `calculate_distance` function.

    This class contains unit tests
      for the `calculate_distance` function,
    testing various scenarios
      including positive coordinates, negative coordinates,
    and identical points. The tests
      also include checks for invalid arguments
    to ensure defensive handling of edge cases.
    """

    def test_positive_coordinates(self):
        """Test the function with positive coordinates."""
        self.assertEqual(
            calculate_distance(0, 0, 3, 4),
            5.0,
            "Distance between (0, 0) and (3, 4) should be 5.0",
        )
        self.assertEqual(
            calculate_distance(1, 1, 4, 5),
            5.0,
            "Distance between (1, 1) and (4, 5) should be 5.0",
        )

    def test_negative_coordinates(self):
        """Test the function with negative coordinates."""
        self.assertEqual(
            calculate_distance(-1, -1, -4, -5),
            5.0,
            "Distance between (-1, -1) and (-4, -5) should be 5.0",
        )
        self.assertEqual(
            calculate_distance(-2, -3, -2, -3),
            0.0,
            "Distance between the same negative points should be 0.0",
        )

    def test_same_point(self):
        """Test when both points are the same."""
        self.assertEqual(
            calculate_distance(2, 3, 2, 3),
            0.0,
            "Distance between the same points (2, 3) should be 0.0",
        )

    def test_invalid_arguments(self):
        """Test defensive assertions for invalid arguments."""
        with self.assertRaises(
            AssertionError, msg="Should raise AssertionError for non-numeric inputs"
        ):
            calculate_distance("a", 0, 3, 4)
        with self.assertRaises(
            AssertionError, msg="Should raise AssertionError for None inputs"
        ):
            calculate_distance(None, 0, 3, 4)
        with self.assertRaises(
            TypeError, msg="Should raise TypeError for missing arguments"
        ):
            calculate_distance(0, 0, 3)
        with self.assertRaises(
            TypeError, msg="Should raise TypeError for too many inputs"
        ):
            calculate_distance(0, 0, 3, 4, 5)
