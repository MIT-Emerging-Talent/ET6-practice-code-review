"""
Test module for the word_comparator function.

Created on: 03 01 25
@author: MD Jubayer Khan
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from word_comparator import are_words_same


class TestWordComparator(unittest.TestCase):
    """
    Unit tests for the are_words_same function.
    """

    def test_same_words(self):
        """It should return True for words with the same sorted characters."""
        self.assertTrue(are_words_same("listen", "silent"))
        self.assertTrue(are_words_same("word", "wrdo"))

    def test_different_words(self):
        """It should return False for words with different characters."""
        self.assertFalse(are_words_same("hello", "world"))
        self.assertFalse(are_words_same("python", "java"))

    def test_empty_strings(self):
        """It should return True for two empty strings."""
        self.assertTrue(are_words_same("", ""))

    def test_case_sensitivity(self):
        """It should consider case sensitivity while comparing."""
        self.assertFalse(are_words_same("Listen", "silent"))
        self.assertFalse(are_words_same("Word", "word"))

    def test_partial_overlap(self):
        """It should return False for words with some common characters."""
        self.assertFalse(are_words_same("abcd", "abc"))


if __name__ == "__main__":
    unittest.main()
