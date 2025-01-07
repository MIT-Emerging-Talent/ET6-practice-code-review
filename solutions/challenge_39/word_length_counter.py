#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the lengths of words in a sentence.
Created on 06 Jan 2025
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
    # Remove punctuation and split the sentence into words
    words = input_sentence.translate(str.maketrans("", "", string.punctuation)).split()
    # Return the lengths of the words
    return [len(word) for word in words]


if __name__ == "__main__":
    # Example usage for manual testing
    example_sentences = [
        "Hello world!",
        "Python is awesome.",
        "I love MIT.",
    ]

    for example_sentence in example_sentences:
        print(f"Input: {example_sentence}")
        print(f"Word lengths: {word_lengths(example_sentence)}")
        print("-" * 20)
