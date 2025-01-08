def is_palindrome(s):
    """
    Function to check whether a given string is a palindrome.
    A palindrome reads the same backward as forward, ignoring case.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string: convert to lowercase
    normalized_str = s.lower()
    
    # Compare the string with its reverse
    return normalized_str == normalized_str[::-1]

# Test Cases
def test_is_palindrome():
    """
    Test the is_palindrome function with various cases.
    """
    test_cases = [
        ("madam", True),      # A simple palindrome
        ("hello", False),     # Not a palindrome
        ("RaceCar", True),    # Case-insensitive palindrome
        ("", True),           # An empty string is a palindrome
        ("A", True),          # A single character is a palindrome
        ("Noon", True),       # Mixed case palindrome
        ("Palindrome", False) # A non-palindrome
    ]
    
    # Run tests and print results
    for input_str, expected in test_cases:
        result = is_palindrome(input_str)
        assert result == expected, f"Test failed for input: {input_str}"
        print(f"Input: '{input_str}', Expected: {expected}, Output: {result}")
    print("All test cases passed!")

# Run Tests
test_is_palindrome()
