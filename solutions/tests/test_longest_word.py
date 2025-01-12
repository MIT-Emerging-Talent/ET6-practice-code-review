#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module contains unit tests for the `longest_word` function.

The tests verify that the `longest_word` function works as expected for a variety of
valid and invalid inputs, including boundary cases.

Tests include:
- Valid sentence inputs containing multiple words.
- Sentences with a single word.
- Empty strings to test for error handling.
- Non-string inputs to ensure a `ValueError` is raised.
- Sentences with multiple longest words to check if the first encountered word is returned.

The tests ensure that the function returns the correct longest word, and that it raises an
`AssertionError` when given invalid inputs such as non-string values or empty strings.
"""

import unittest
from solutions.longest_word import longest_word


class TestLongestWord(unittest.TestCase):
    """
    Test the behavior of the longest_word function.
    """

    def test_sentence_with_punctuation(self):
        """
        Test case for sentences containing punctuation.
        The function should return the longest word, ignoring punctuation.
        """
        result = longest_word("Hello, world!")
        self.assertEqual(result, "Hello")

    def test_non_string_input(self):
        """
        Test case for non-string input to ensure defensive assertion raises the error.
        """
        with self.assertRaises(AssertionError):
            longest_word(123)  # Pass a non-string value

    def test_empty_string(self):
        """
        Test case for an empty string to ensure the correct error is raised.
        """
        with self.assertRaises(AssertionError):
            longest_word("")  # Pass an empty string

    def test_single_word(self):
        """
        Test case for a sentence with a single word.
        The function should return the single word.
        """
        result = longest_word("Python")
        self.assertEqual(result, "Python")

    def test_multiple_longest_words(self):
        """
        Test case for multiple words of the same maximum length.
        The function should return the first encountered word.
        """
        result = longest_word("apple banana cherry")
        self.assertEqual(result, "banana")


if __name__ == "__main__":
    unittest.main()
