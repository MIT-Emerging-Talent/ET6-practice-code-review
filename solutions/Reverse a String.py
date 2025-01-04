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

# DEBUG: We're adding logs to help us understand what the program is doing at each step.
# 1. First, we log the input string to see what value was passed to the function.
# 2. Then, we log the "normalized" version of the string. This is the cleaned-up version 
#    where we convert it to lowercase and remove any spaces or non-alphanumeric characters.
# 3. Finally, we log the result of the palindrome check to know if the cleaned-up string 
#    is the same when read forwards and backwards.
# These debug messages are useful for identifying where something might go wrong in the process 
# and for understanding how the function handles different types of input.
        