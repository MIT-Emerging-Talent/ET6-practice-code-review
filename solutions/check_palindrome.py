"""
A module for checking if a given word is a palindrome.

Module contents:
    - is_palindrome: checks if a given word is a palindrome.

Created on 05/01/2025
@author: Maria Cedeño
"""


def is_palindrome(word: str) -> bool:
    """
    Checks if a given word is a palindrome.

    Args:
        word: The word to check.

    Returns:
        True if the word is a palindrome, False otherwise.

    Raises:
        TypeError: If the input 'word' is not a string.

    >>> is_palindrome("kayak")
    True

    >>> is_palindrome("hello")
    False

    >>> is_palindrome(123)
    Traceback (most recent call last):
        ...
    TypeError: Input 'word' must be a string.
    """

    if not isinstance(word, str):
        raise TypeError("Input 'word' must be a string.")

    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")

    # Check if the word is equal to its reverse
    return word == word[::-1]
