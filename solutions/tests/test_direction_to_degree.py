#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains unit tests for the `direction_to_degree` function.

The tests verify that the `direction_to_degree` function works as expected for a variety of
valid and invalid inputs, including boundary cases and case insensitivity.

Tests include:
- Valid direction inputs ("N", "NE", "SW", etc.)
- Invalid direction inputs (e.g., "INVALID")
- Non-string inputs (e.g., integers)
- Case insensitivity of the function

The tests ensure that the function returns the correct degree or an "Invalid direction" string,
and that it raises a `ValueError` when given a non-string input.
"""

import unittest

from solutions.direction_to_degree import direction_to_degree


class TestDirectionToDegree(unittest.TestCase):
    """Test the behavior of the direction_to_degree function."""

    def test_valid_directions(self):
        """Test valid direction inputs."""
        # Check cardinal directions
        self.assertEqual(direction_to_degree("N"), 0)
        self.assertEqual(direction_to_degree("E"), 90)
        self.assertEqual(direction_to_degree("S"), 180)
        self.assertEqual(direction_to_degree("W"), 270)

        # Check intercardinal directions
        self.assertEqual(direction_to_degree("NE"), 45)
        self.assertEqual(direction_to_degree("SE"), 135)
        self.assertEqual(direction_to_degree("SW"), 225)
        self.assertEqual(direction_to_degree("NW"), 315)

        # Check other intercardinal directions
        self.assertEqual(direction_to_degree("NNE"), 22)
        self.assertEqual(direction_to_degree("ENE"), 67)
        self.assertEqual(direction_to_degree("ESE"), 112)
        self.assertEqual(direction_to_degree("SSW"), 202)
        self.assertEqual(direction_to_degree("WSW"), 247)
        self.assertEqual(direction_to_degree("WNW"), 292)
        self.assertEqual(direction_to_degree("NNW"), 337)

    def test_invalid_direction(self):
        """Test invalid direction input."""
        self.assertEqual(direction_to_degree("INVALID"), "Invalid direction")

    def test_case_insensitivity(self):
        """Test case insensitivity."""
        self.assertEqual(direction_to_degree("n"), 0)
        self.assertEqual(direction_to_degree("se"), 135)
        self.assertEqual(direction_to_degree("ESE"), 112)

    def test_non_string_input(self):
        """Test non-string input."""
        with self.assertRaises(ValueError):
            direction_to_degree(123)  # Should raise ValueError

    def test_empty_string(self):
        """Test empty string input."""
        self.assertEqual(direction_to_degree(""), "Invalid direction")


if __name__ == "__main__":
    unittest.main()
