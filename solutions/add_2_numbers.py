"""
This module contains a function to add two numbers.

It defines a function called `add_2_numbers` which takes two numbers as input
and returns their sum.
"""


def add_2_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.

    Raises:
        AssertionError: If a or b are not int or float.
    """
    assert isinstance(a, (int, float)), "First argument must be an int or float"
    assert isinstance(b, (int, float)), "Second argument must be an int or float"
    return a + b


# Example usage:
if __name__ == "__main__":
    result = add_2_numbers(3, 5)  # pylint: disable=C0103
    print(result)  # Output: 8
