
def check_even_or_odd(number):
    """
    Function to check if a given number is even or odd.

    Parameters:
    number (int): The integer to check.

    Returns:
    str: "Even" if the number is even, otherwise "Odd".
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Testing the function
def test_check_even_or_odd():
    """
    Function to test the check_even_or_odd function with various cases.
    """
    test_cases = [4, 7, 0, -2, -3]  # Sample test cases including negative numbers

    for test in test_cases:
        result = check_even_or_odd(test)
        print(f"Input: {test}, Output: {result}")


# Run the test function
if __name__ == "__main__":
    test_check_even_or_odd()
