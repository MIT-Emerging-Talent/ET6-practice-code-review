#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting vowels in a string.

Module contents:
    - count_vowels: counts the number of vowels in a string.

Created on XX XX XX
@author: Saliha Kalender
"""
import unittest


def count_vowels(input_string):
    """
    Counts the number of vowels in a given string.

    Behavior Description:
    - The function identifies all vowels (a, e, i, o, u) in the input string,
    regardless of case.
    - It returns the total count of vowels found.

    Parameter Description:
    - input_string (str): The string to be processed.
    It can contain letters, numbers, spaces, and special characters.

    Return Value Description:
    - int: The total number of vowels in the input string.

    Assumptions:
    - Input is always a string.
    - Vowels are defined as 'a', 'e', 'i', 'o', 'u', both uppercase and lowercase.

    Doctests:
    >>> count_vowels("hello")
    2
    >>> count_vowels("HELLO")
    2
    >>> count_vowels("123 abc XYZ")
    1

    Assertions:
    - Asserts that the input is of type str.

    Use Cases:
    1. Counting vowels in a user-provided string input.
    2. Processing text data to analyze vowel frequency.
    """
    assert isinstance(input_string, str), "Input must be a string."

    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count


# Example usage:
if __name__ == "__main__":
    EXAMPLE1 = "Programming is fun!"
    EXAMPLE2 = "AEIOUaeiou"

    print(f"Vowels in '{EXAMPLE1}': {count_vowels(EXAMPLE1)}")  # Output: 5
    print(f"Vowels in '{EXAMPLE2}': {count_vowels(EXAMPLE2)}")  # Output: 10


class TestCountVowels(unittest.TestCase):
    """
    Unit tests for the count_vowels function.
    """

    def test_basic_vowels(self):
        """
        Test that vowels are correctly counted in a basic string.
        """
        self.assertEqual(count_vowels("hello"), 2)

    def test_uppercase_vowels(self):
        """
        Test that uppercase vowels are correctly counted.
        """
        self.assertEqual(count_vowels("HELLO"), 2)

    def test_mixed_content(self):
        """
        Test that vowels are counted in a string with mixed content.
        """
        self.assertEqual(count_vowels("123 abc XYZ"), 1)

    def test_no_vowels(self):
        """
        Test that a string with no vowels returns 0.
        """
        self.assertEqual(count_vowels("bcdfg"), 0)

    def test_all_vowels(self):
        """
        Test that a string with only vowels returns the correct count.
        """
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_empty_string(self):
        """
        Test that an empty string returns 0.
        """
        self.assertEqual(count_vowels(""), 0)

    def test_special_characters(self):
        """
        Test that a string with special characters only returns 0.
        """
        self.assertEqual(count_vowels("!@#$%^&*()"), 0)

    def test_assertion_error(self):
        """
        Test that a non-string input raises an assertion error.
        """
        with self.assertRaises(AssertionError):
            count_vowels(12345)


if __name__ == "__main__":
    unittest.main()
