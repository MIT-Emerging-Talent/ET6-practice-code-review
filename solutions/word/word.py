#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the lengths of words in a sentence.
created: 01/07/2025
@author: Arthur (Mr-Glucose)

"""

import string


def word_lengths(input_sentence):
    """
    Takes a sentence and returns a list of word lengths, ignoring punctuation.

    Args:
        input_sentence (str): The input sentence.

    Returns:
        list: A list of integers representing word lengths.
    """
    words = input_sentence.translate(str.maketrans("", "", string.punctuation)).split()
    return [len(word) for word in words]
