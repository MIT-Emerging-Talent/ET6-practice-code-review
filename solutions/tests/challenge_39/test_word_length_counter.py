#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the word_lengths function.
Created on 06 Jan 2025
@author: Arthur (Mr-Glucose)
"""

import unittest

from word_lengths import word_lengths


class TestWordLengths(unittest.TestCase):
    def test_regular_sentences(self):
        self.assertEqual(word_lengths("Hello world!"), [5, 5])
        self.assertEqual(word_lengths("Python is awesome."), [6, 2, 7])

    def test_single_word(self):
        self.assertEqual(word_lengths("Amazing!"), [7])

    def test_empty_string(self):
        self.assertEqual(word_lengths(""), [])

    def test_only_punctuation(self):
        self.assertEqual(word_lengths("...?!"), [])

    def test_mixed_content(self):
        self.assertEqual(word_lengths("123 and 4567!"), [3, 3, 4])

    def test_special_characters_in_words(self):
        self.assertEqual(word_lengths("co-op re-enter."), [4, 7])


if __name__ == "__main__":
    unittest.main()
