"""
largest_element.py
This module contains the implementation of the largest_element function,
which checks values of numbers in the list and returns the largest value.
"""


def largest_element(numbers: list) -> int | float | None:
    """
    Returns the largest element in a list
    Parameter:
        numbers (list): list of numbers
    Returns:
        _int/float/None:  Returns the largest number from the list or None if the list is empty
    Raises:
        AssertionError: If any element in the list is not an integer or float
    Example:
    >>> largest_element([-1,0,1])
    1
    >>> largest_element([1,2,3])
    3
    >>> largest_element([-1,0,2.5])
    2.5
    >>> largest_element([])

    """
    assert all(
        isinstance(num, (int, float)) for num in numbers
    ), "num must be integer or float"

    if not numbers:  # Return None for empty lists as there is no largest element
        return None

    largest = numbers[
        0
    ]  #  # Initialize with the first element to have a comparison point

    for num in numbers:  # Compare each number to track the largest seen so far
        largest = max(largest, num)  # Update the largest when a larger number is found

    return largest  # return the largest number
