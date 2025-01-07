#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test the friend function.

Test categories:
    - Standard cases: Filter a list with friends and non-friends.
    - Edge cases: Handle invalid input types and boundary conditions.

Created on 2025-01-04
Author: Cynthia Wairimu
"""

import unittest
from ..friend_or_foe import friend


class TestFriendOrFoe(unittest.TestCase):
    """Tests for the friend function."""

    def test_two_friends(self):
        """It should return all strings with exactly 4 characters."""
        result = friend(["Nimo", "Brian", "Joe", "Joan"])
        self.assertEqual(result, ["Nimo", "Joan"])

    def test_no_friend(self):
        """It should return an empty list when no names have 4 characters."""
        result = friend(["Ron", "Brian", "Sixisveryfunny", "namey"])
        self.assertEqual(result, [])

    def test_not_list(self):
        """It should raise a TypeError for non-list input."""
        with self.assertRaises(TypeError):
            friend("Four")

    def test_non_string_elements(self):
        """It should raise a TypeError for lists containing non-string elements."""
        with self.assertRaises(TypeError):
            friend(["Nimo", 123, "Joan"])

    def test_empty_list(self):
        """It should return an empty list for an empty input list."""
        result = friend([])
        self.assertEqual(result, [])

    def test_edge_case_boundary_conditions(self):
        """It should handle edge cases like a list with only 4-character names."""
        result = friend(["Anna", "John", "Mark", "Emma"])
        self.assertEqual(result, ["Anna", "John", "Mark", "Emma"])


if __name__ == "__main__":
    unittest.main()
