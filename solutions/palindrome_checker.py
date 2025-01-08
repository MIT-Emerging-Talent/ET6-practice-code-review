"""
This module contains a function to check if a string is a palindrome.

A palindrome is a string that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
"""


def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces, punctuation, and capitalization.

    Parameters:
        s (str): The input string to check.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.

    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("Hello")
        False
    """
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized = "".join(char.lower() for char in s if char.isalnum())
    # Check if the normalized string is equal to its reverse
    return normalized == normalized[::-1]


# Example usage
if __name__ == "__main__":
    test_strings = [
        "A man, a plan, a canal: Panama",
        "Racecar",
        "Hello",
        "",
        "12321",
        "Not a palindrome",
    ]

    for test in test_strings:
        print(f"'{test}' is a palindrome: {is_palindrome(test)}")
