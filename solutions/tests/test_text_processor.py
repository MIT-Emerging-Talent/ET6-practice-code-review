"""
Test for the text_processor module.
"""


def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in the given text.

    Args:
        text (str): The string to analyze.

    Returns:
        int: The number of vowels in the text.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def reverse_text(text: str) -> str:
    """
    Reverse the given text.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return text[::-1]


def to_uppercase(text: str) -> str:
    """
    Convert the given text to uppercase.

    Args:
        text (str): The string to convert.

    Returns:
        str: The text in uppercase.
    """
    return text.upper()


# Test functions
def test_count_vowels():
    print("Testing count_vowels:")
    print(count_vowels("hello"))  # Expected: 2
    print(count_vowels("HELLO"))  # Expected: 2
    print(count_vowels("Python"))  # Expected: 1
    print(count_vowels("aeiou"))  # Expected: 5
    print(count_vowels("bcdfg"))  # Expected: 0


def test_reverse_text():
    print("\nTesting reverse_text:")
    print(reverse_text("hello"))  # Expected: "olleh"
    print(reverse_text("Python"))  # Expected: "nohtyP"
    print(reverse_text("12345"))  # Expected: "54321"
    print(reverse_text(""))  # Expected: ""


def test_to_uppercase():
    print("\nTesting to_uppercase:")
    print(to_uppercase("hello"))  # Expected: "HELLO"
    print(to_uppercase("Python"))  # Expected: "PYTHON"
    print(to_uppercase("12345"))  # Expected: "12345"
    print(to_uppercase("!@#$"))  # Expected: "!@#$"


if __name__ == "__main__":
    test_count_vowels()
    test_reverse_text()
    test_to_uppercase()
