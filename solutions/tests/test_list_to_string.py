#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: test_list_to_string.

Description:
    This module contains test cases for the `list_to_string` function defined
    in the `list_to_string_converter.py` module. It tests the function's behavior
    with various input scenarios, ensuring that it handles different edge cases and
    returns the expected concatenated string.

Test Categories:
    - Standard cases: List of integers, floats, strings, and booleans.
    - Edge cases:  single-element list, list with mixed data types.
    - Defensive tests: None input, Non-list inputs, Empty list.

Author: Falaq Youniss
Date: 30/12/2024
"""

import unittest
from ..list_to_string import list_to_string


class TestListToString(unittest.TestCase):
    """Test cases for the `list_to_string` function."""

    # Standard test cases
    def test_integers(self):
        """It should return a concatenated string of integers."""
        self.assertEqual(list_to_string([1, 2, 3]), "123")

    def test_floats(self):
        """It should return a concatenated string of floats."""
        self.assertEqual(list_to_string([1.1, 2.2, 3.3]), "1.12.23.3")

    def test_strings(self):
        """It should return a concatenated string of strings."""
        self.assertEqual(list_to_string(["cat", "hat", "bat"]), "cathatbat")

    def test_booleans(self):
        """It should return a concatenated string of booleans."""
        self.assertEqual(list_to_string([True, False]), "TrueFalse")

    # Edge cases
    def test_mixed_types(self):
        """It should return a concatenated string of mixed types."""
        self.assertEqual(list_to_string([1, "cat", 3.5, True]), "1cat3.5True")

    def test_single_element(self):
        """It should return the same single element as a string."""
        self.assertEqual(list_to_string([42]), "42")

    def test_repeated_element(self):
        """It should return repeated elements"""
        self.assertEqual(list_to_string([1, 1, 1, 1]), "1111")

    def test_empty_element(self):
        """It should ignore empty elements"""
        self.assertEqual(list_to_string(["cat", "", "dog", ""]), "catdog")

    def test_space_element(self):
        """It should return elements with space elements"""
        self.assertEqual(list_to_string(["cat", " ", "dog", " "]), "cat dog ")

    # Defensive tests
    def test_none_input(self):
        """It should raise an AssertionError for None input."""
        with self.assertRaises(AssertionError):
            list_to_string(None)

    def test_non_list_input(self):
        """It should raise an AssertionError for non-list input."""
        with self.assertRaises(AssertionError):
            list_to_string("not a list")

    def test_empty_list(self):
        """It should raise an AssertionError for empty list."""
        with self.assertRaises(AssertionError):
            list_to_string([])


if __name__ == "__main__":
    unittest.main()
