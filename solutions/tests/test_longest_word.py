"""
Test module for longest_word function.
Tests standard cases, edge cases and input validation.
"""

import unittest
from ..longest_word import longest_word


class TestLongestWord(unittest.TestCase):
    """
    Unit tests for the longest_word function.

    These tests ensure that the function works as expected across a variety
    of cases, including edge cases, and handles errors appropriately.
    """

    def test_normal_case(self):
        """
        Test the function with a regular sentence.

        The longest word should be correctly identified from the sentence.
        """
        result = longest_word("I love programming with Python with my classmates")
        self.assertEqual(result, "programming")

    def test_multiple_longest_words(self):
        """
        Test the function when there are multiple longest words.

        If there are multiple longest words, the first one encountered should be returned.
        """
        result = longest_word("I am learning Python and programming")
        self.assertEqual(result, "programming")

    def test_empty_sentence(self):
        """
        Test the function with an empty sentence.

        An empty sentence should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            longest_word("")

    def test_non_string_input(self):
        """
        Test the function with a non-string input.

        The function should raise a ValueError if the input is not a string.
        """
        with self.assertRaises(ValueError):
            longest_word(123)

    def test_single_word(self):
        """
        Test the function with a single word.

        The word should be returned as the longest word.
        """
        result = longest_word("Hello")
        self.assertEqual(result, "Hello")

    def test_sentence_with_punctuation(self):
        """
        The function should ignore punctuation and return the correct longest word.
        """
        result = longest_word("Hello, world! Let's code.")
        self.assertEqual(result, "world")


if __name__ == "__main__":
    unittest.main()
