def is_palindrome(s):
    """
    Check if the given string is a palindrome, ignoring case.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    normalized_str = s.lower()
    return normalized_str == normalized_str[::-1]


def test_is_palindrome():
    """
    Test the is_palindrome function with various cases.
    """
    test_cases = [
        ("madam", True),
        ("hello", False),
        ("RaceCar", True),
        ("", True),
        ("A", True),
        ("Noon", True),
        ("Palindrome", False),
    ]

    for input_str, expected in test_cases:
        result = is_palindrome(input_str)
        assert result == expected, f"Test failed for input: {input_str}"
        print(f"Input: '{input_str}', Expected: {expected}, Output: {result}")


test_is_palindrome()
