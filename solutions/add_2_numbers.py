"""
This module contains a function to add two numbers.

It defines a function called `add_numbers` which takes two numbers as input
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
    """
    return a + b


# Example usage:
result = add_numbers(3, 5)  # pylint: disable=C0103
print(result)  # Output: 8
