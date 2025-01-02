"""
unique_words_counter.py

This module provides a function to count the number of unique words in a string.

Functions:
    count_unique_words(text): Returns the count of unique words.
"""

def count_unique_words(text):
    """
    Counts the number of unique words in a string.

    Args:
        text (str): A string of words.

    Returns:
        int: The number of unique words in the string.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    words = text.split()
    unique_words = set(words)
    return len(unique_words)
    
