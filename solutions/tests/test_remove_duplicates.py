#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for remove_duplicates function.

Created on 2024-12-30
Author: Heba Shaheen
"""

import unittest

from ..remove_duplicates import remove_duplicates


class TestCountBetween(unittest.TestCase):
    """Test remove_duplicates function"""

    # Standard test cases
    def test_numbers_list(self):
        """It should remove duplicates numbers"""
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 3, 4]), [1, 2, 3, 4])

    def test_letters_list(self):
        """It should remove duplicates letters"""
        self.assertEqual(
            remove_duplicates(["a", "v", "e", "e", "q"]), ["a", "v", "e", "q"]
        )

    def test_mix_list(self):
        """It should remove duplicates items"""
        self.assertEqual(
            remove_duplicates([1, 2, 3, "e", 2, 1, "e", 5, "a"]), [1, 2, 3, "e", 5, "a"]
        )

    # Edge cases
    def test_empty_list(self):
        """It should return empty list"""
        self.assertEqual(remove_duplicates([]), [])

    # Defensive tests
    def test_invalid_type(self):
        """It should raise AssertionError if numbers is not a list"""
        with self.assertRaises(AssertionError):
            remove_duplicates("1, 2, 2")


if __name__ == "__main__":
    unittest.main()
