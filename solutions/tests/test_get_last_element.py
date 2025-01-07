"""
Module: test_get_last_element
The unit tests for the get_last_element function check different cases,
including lists with multiple elements, one element, empty lists, and invalid inputs.

Created on 01.04.2024
@author: Mohammad Mohseni

"""

import unittest

from ..get_last_element import get_last_element


class TestGetLastElement(unittest.TestCase):
    """Unit tests for the get_last_element function."""

    def test_non_empty_list(self):
        """Test with a non-empty list."""
        actual = get_last_element([1, 2, 3, 4])
        expected = 4
        self.assertEqual(actual, expected)

    def test_single_element_list(self):
        """Test with a single-element list."""
        self.assertEqual(get_last_element([42]), 42)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(get_last_element([]))  # Should return None

    def test_string_list(self):
        """Test with a list of strings."""
        actual = get_last_element(["Mohammad", "Ali", "Meklit"])
        expected = "Meklit"
        self.assertEqual(actual, expected)

    def test_mixed_data_types(self):
        """Test with a list containing different data types."""
        actual = get_last_element([1, "Jawid", 3.14, "Mohammad"])
        expected = "Mohammad"
        self.assertEqual(actual, expected)

    def test_invalid_input(self):
        """Test with an invalid input (non-list)."""
        with self.assertRaises(TypeError):
            get_last_element("not a list")


if __name__ == "__main__":
    unittest.main()  # Run all the test cases
