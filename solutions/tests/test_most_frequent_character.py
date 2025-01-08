"""
A module for testing the most_frequent_character function.

Tests included:
    - When a single character is the most frequent
    - When multiple characters have the same frequency
    - When the input string is empty
    - When the input is not a string

Created on 08/01/2025
@author: Mohamad Ziadah
"""

import unittest

from ..most_frequent_character import most_frequent_character


class TestMostFrequentCharacter(unittest.TestCase):
    """
    Tests the function "most_frequent_character" in the file character_analysis.
    """

    def test_single_most_frequent(self):
        """
        It should return 'a' as the most frequent character
        """
        actual = most_frequent_character("abracadabra")
        self.assertEqual(actual, "a")

    def test_multiple_characters_same_frequency(self):
        """
        It should return the first most frequent character found ('a' in this case)
        """
        actual = most_frequent_character("aabbcc")
        self.assertEqual(actual, "a")  # Assuming ties return the first character

    def test_empty_string(self):
        """
        It should return None for an empty string
        """
        actual = most_frequent_character("")
        self.assertIsNone(actual)

    def test_non_string_input(self):
        """
        It should raise an AssertionError if the input is not a string
        """
        with self.assertRaises(AssertionError):
            most_frequent_character(12345)

    def test_with_spaces_and_special_characters(self):
        """
        It should identify the most frequent character, ignoring whitespace or special cases
        """
        actual = most_frequent_character("Hello, World!")
        self.assertEqual(actual, "l")  # 'l' appears 3 times

    def test_case_insensitivity(self):
        """
        It should treat uppercase and lowercase characters equally
        """
        actual = most_frequent_character("AaBbAa")
        self.assertEqual(actual, "a")


if __name__ == "__main__":
    unittest.main()
