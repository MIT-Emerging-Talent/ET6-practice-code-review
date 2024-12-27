#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Test module for the function count_unique_words.
Includes intentionally flawed tests for debugging practice.

Test categories:
    - General cases: A set of typical sentences to check standard functionality.
    - Boundary cases: Empty string, sentences with all distinct words.
    - Robustness tests: Handling invalid input types and assertion errors.

Created on Dec 27, 2024.

@author: Pyae Linn
"""

import unittest
from ..unique_words_counter import count_unique_words


class TestCountUniqueWords(unittest.TestCase):
    """Unit tests for the function `count_unique_words`."""

    def test_regular_sentence(self):
        """Test with a standard sentence containing both repeated and unique words."""
        self.assertEqual(count_unique_words("This is a test test case"), 5)

    def test_empty_string(self):
        """Test case for an empty input string."""
        self.assertEqual(count_unique_words(""), 0)

    def test_all_unique_words(self):
        """Test case with all words being unique in the sentence."""
        self.assertEqual(count_unique_words("Python is fun"), 3)

    def test_case_insensitivity(self):
        """Test case where words should be counted case-insensitively."""
        self.assertEqual(count_unique_words("Python python PYTHON"), 3)

    def test_invalid_input(self):
        """Test case for invalid input (non-string types)."""
        with self.assertRaises(TypeError):
            count_unique_words(123)

if __name__ == "__main__":
    unittest.main()
