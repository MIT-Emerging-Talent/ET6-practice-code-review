def check_even_or_odd(number):
    """
    Check if a given number is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: "Even" if the number is even, "Odd" otherwise.
    """
    return "Even" if number % 2 == 0 else "Odd"


def run_tests():
    """
    Run test cases for the check_even_or_odd function.
    """
    test_cases = [4, 7, 0, -2, -3]
    expected_results = ["Even", "Odd", "Even", "Even", "Odd"]

    for idx, test in enumerate(test_cases):
        result = check_even_or_odd(test)
        assert result == expected_results[idx], f"Test failed for input {test}"
        print(f"Test passed for input {test}: {result}")


if __name__ == "__main__":
    run_tests()
