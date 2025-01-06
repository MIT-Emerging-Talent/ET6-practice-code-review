"""
A module for testing the word_count_function.

Tests included:
    - When the string contains multiple words
    - When the string is empty
    - When the string contains only spaces or special characters
    - When the input is not a string
    - When the string contains mixed whitespace characters
    - When the string contains leading and trailing spaces

Created on 06/01/2025
@author: Mohamad Ziadah
"""

import unittest

from ..count_the_number_of_words import word_count_function


class TestWordCountFunction(unittest.TestCase):
    """
    Tests the function "word_count_function" in the file count_the_number_of_words.
    """

    def test_multiple_words(self):
        """
        It should correctly count the number of words in a string with multiple words.
        """
        actual = word_count_function("The quick brown fox jumps over the lazy dog")
        self.assertEqual(actual, 9)

    def test_empty_string(self):
        """
        It should return 0 for an empty string.
        """
        actual = word_count_function("")
        self.assertEqual(actual, 0)

    def test_only_spaces_or_special_characters(self):
        """
        It should return 0 for a string with only spaces or special characters.
        """
        actual = word_count_function("     !!! $$$ ")
        self.assertEqual(actual, 0)

    def test_non_string_input(self):
        """
        It should raise an AssertionError if the input is not a string.
        """
        with self.assertRaises(AssertionError):
            word_count_function(12345)

    def test_mixed_whitespace_characters(self):
        """
        It should correctly count words in a string with mixed whitespace characters.
        """
        actual = word_count_function("word1\tword2\nword3  word4")
        self.assertEqual(actual, 4)

    def test_leading_and_trailing_spaces(self):
        """
        It should correctly count words in a string with leading and trailing spaces.
        """
        actual = word_count_function("   leading and trailing spaces   ")
        self.assertEqual(actual, 4)


if __name__ == "__main__":
    unittest.main()
