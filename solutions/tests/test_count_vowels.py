#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unit tests for the count_vowels function.


import unittest
from ..count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    # Unit tests for the count_vowels function.

    def test_basic_vowels(self):
        # Test that vowels are correctly counted in a basic string.

        self.assertEqual(count_vowels("hello"), 2)

    def test_uppercase_vowels(self):
        # Test that uppercase vowels are correctly counted.

        self.assertEqual(count_vowels("HELLO"), 2)

    def test_mixed_content(self):
        # Test that vowels are counted in a string with mixed content.

        self.assertEqual(count_vowels("123 abc XYZ"), 1)

    def test_no_vowels(self):
        # Test that a string with no vowels returns 0.

        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_all_vowels(self):
        # Test that a string with only vowels returns the correct count.

        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_empty_string(self):
        # Test that an empty string returns 0.

        self.assertEqual(count_vowels(""), 0)

    def test_special_characters(self):
        # Test that a string with special characters only returns 0.

        self.assertEqual(count_vowels("!@#$%^&*()"), 0)

    def test_assertion_error(self):
        # Test to ensure the function raises an AssertionError for non-string inputs.
        with self.assertRaises(AssertionError):
            count_vowels(12345)


if __name__ == "__main__":
    # This ensures that the unittest framework runs the test cases in this file
    unittest.main()
