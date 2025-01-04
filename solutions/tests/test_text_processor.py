"""
test_text_processor

Description: This module tests the functions in the text_processor module, including counting vowels, reversing text, and converting text to uppercase.

Created on: 04/01/2025
# spell-checker: disable
@author: Thilakan Jegatheeswaran
# spell-checker: enable
"""


def count_vowels(text: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u) in the given text.

    Parameters:
        text (str): The string to analyze.

    Returns:
        int: The number of vowels in the text.

    Examples:
        >>> count_vowels("hello")
        2

        >>> count_vowels("HELLO")
        2
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def reverse_text(text: str) -> str:
    """
    Reverses the given text.

    Parameters:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.

    Examples:
        >>> reverse_text("hello")
        'olleh'

        >>> reverse_text("Python")
        'nohtyP'
    """
    return text[::-1]


def to_uppercase(text: str) -> str:
    """
    Converts the given text to uppercase.

    Parameters:
        text (str): The string to convert.

    Returns:
        str: The text in uppercase.

    Examples:
        >>> to_uppercase("hello")
        'HELLO'

        >>> to_uppercase("Python")
        'PYTHON'
    """
    return text.upper()


def test_count_vowels():
    """
    Tests the count_vowels function.

    Returns a list of results:
        - "hello": 2
        - "HELLO": 2
        - "Python": 1
        - "aeiou": 5
        - "bcdfg": 0
    """
    return [
        count_vowels("hello"),  # Expected: 2
        count_vowels("HELLO"),  # Expected: 2
        count_vowels("Python"),  # Expected: 1
        count_vowels("aeiou"),  # Expected: 5
        count_vowels("bcdfg"),  # Expected: 0
    ]


def test_reverse_text():
    """
    Tests the reverse_text function.

    Returns a list of results:
        - "hello": "olleh"
        - "Python": "nohtyP"
        - "12345": "54321"
        - "": ""
    """
    return [
        reverse_text("hello"),  # Expected: "olleh"
        reverse_text("Python"),  # Expected: "nohtyP"
        reverse_text("12345"),  # Expected: "54321"
        reverse_text(""),  # Expected: ""
    ]


def test_to_uppercase():
    """
    Tests the to_uppercase function.

    Returns a list of results:
        - "hello": "HELLO"
        - "Python": "PYTHON"
        - "12345": "12345"
        - "!@#$": "!@#$"
    """
    return [
        to_uppercase("hello"),  # Expected: "HELLO"
        to_uppercase("Python"),  # Expected: "PYTHON"
        to_uppercase("12345"),  # Expected: "12345"
        to_uppercase("!@#$"),  # Expected: "!@#$"
    ]


if __name__ == "__main__":
    results_vowels = test_count_vowels()
    results_reverse = test_reverse_text()
    results_uppercase = test_to_uppercase()

    # Displaying the results (you can inspect these directly or use any assertion testing)
    print("Vowel Count Test Results:", results_vowels)
    print("Reverse Text Test Results:", results_reverse)
    print("Uppercase Conversion Test Results:", results_uppercase)
