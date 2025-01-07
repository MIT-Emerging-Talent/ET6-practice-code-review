#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the word_lengths function.
Created on 06 Jan 2025
@author: Arthur (Mr-Glucose)
"""

# Import the word_lengths function
import os
import sys
import unittest

from word_length_counter import word_lengths

# Add the parent directory to the system path to import word_lengths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestWordLengths(unittest.TestCase):
    """
    Unit tests for the word_lengths function.
    Test cases:
    - test_regular_sentences: Tests sentences with regular words and punctuation.
    - test_single_word: Tests a single word with punctuation.
    - test_empty_string: Tests an empty string.
    - test_only_punctuation: Tests a string with only punctuation marks.
    - test_mixed_content: Tests a string with numbers and words.
    - test_special_characters_in_words: Tests words with special characters like hyphens.
    """

    def test_regular_sentences(self):
        """Test regular sentences with words and punctuation."""
        self.assertEqual(word_lengths("Hello world!"), [5, 5])
        self.assertEqual(word_lengths("Python is awesome."), [6, 2, 7])

    def test_single_word(self):
        """Test a single word with punctuation."""
        self.assertEqual(word_lengths("Amazing!"), [7])

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(word_lengths(""), [])

    def test_only_punctuation(self):
        """Test a string with only punctuation marks."""
        self.assertEqual(word_lengths("...?!"), [])

    def test_mixed_content(self):
        """Test a string with numbers and words."""
        self.assertEqual(word_lengths("123 and 4567!"), [3, 3, 4])

    def test_special_characters_in_words(self):
        """Test words with special characters like hyphens."""
        self.assertEqual(word_lengths("co-op re-enter."), [4, 7])


if __name__ == "__main__":
    unittest.main()
