def is_palindrome(s: str) -> str:
  """
  # palindrome_check.py

def is_palindrome(s: str) -> str:
    """
    Checks if a given string is a palindrome.

    :param s: Input string
    :return: "True" if the string is a palindrome, otherwise "False"
    """
    # Normalize the string: convert to lowercase and remove spaces
    normalized_str = ''.join(c.lower() for c in s if c.isalnum())
    # Compare the string with its reverse
    return "True" if normalized_str == normalized_str[::-1] else "False"

# Test cases
if __name__ == "__main__":
    test_cases = ["madam", "hello", "RaceCar"]
    for test in test_cases:
        print(f"Input: {test}, Output: {is_palindrome(test)}")

        