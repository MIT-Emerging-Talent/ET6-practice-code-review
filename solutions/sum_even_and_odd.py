"""This module provides a function sum_even_and_odd
that calculates the sums of positive and negative,
even and odd numbers in a given list.
"""


def sum_even_and_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a list.

    Parameters:
        numbers (list of int or float): List of numbers to process.

    Returns:
        dict: Dictionary with sums of positive even, positive odd,
            ls  negative even, and negative odd numbers.

    Raises:
        ValueError: If input is not a list or contains non-numeric values.

    Examples:
    >>> sum_even_and_odd([1, -2, 3, 4, -5, 0])
    {'positive_even': 4, 'positive_odd': 4, 'negative_even': -2, 'negative_odd': -5}
    >>> sum_even_and_odd([])
    {'positive_even': 0, 'positive_odd': 0, 'negative_even': 0, 'negative_odd': 0}
    """
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be integers or floats.")

    result = {
        "positive_even": 0,
        "positive_odd": 0,
        "negative_even": 0,
        "negative_odd": 0,
    }

    for num in numbers:
        if num > 0 and isinstance(num, int) and num % 2 == 0:
            result["positive_even"] += num
        elif num > 0:
            result["positive_odd"] += num
        elif num < 0 and isinstance(num, int) and num % 2 == 0:
            result["negative_even"] += num
        elif num < 0:
            result["negative_odd"] += num

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
