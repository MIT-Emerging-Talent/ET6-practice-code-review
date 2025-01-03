"""This module contains a function that takes a list of numbers and returns the largest number from that list.

The `largest_num` function checks if the input list is empty and raises a ValueError if so. Otherwise, it
returns the maximum number in the list using the built-in `max` function."""


def largest_num(numbers):
    """
    This function takes a list of numbers as input and returns the largest number.

    Parameters:
    A list of numbers.

    Returns:
        float: The largest number in the list.
    """

    if not numbers:
        raise ValueError("The  list is empty.")
    return max(numbers)
