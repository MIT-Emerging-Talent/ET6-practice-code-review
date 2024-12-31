"""
This module provides a function to calculate the mean (average) of a list of numbers.

Date created: Dec 30,2024
Author: @Abel Teka
"""

from typing import List, Optional


def calculate_mean(numbers: List[float]) -> Optional[float]:
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        numbers (List[float]): A list of numbers (integers or floats).
            - The list can include positive, negative, or zero values.

    Returns:
        Optional[float]: The mean (average) of the numbers in the list.
            - Returns None if the list is empty.

    Raises:
        TypeError: If `numbers` is not a list or contains non-numeric elements.
        ValueError: If the list contains infinite or NaN values.

    Examples:
        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0
        >>> calculate_mean([10, 20, 30])
        20.0
        >>> calculate_mean([])
        None
        >>> calculate_mean([5])
        5.0
        >>> calculate_mean([1.5, 2.5, 3.5])
        2.5
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if any(not isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements in the list must be numbers.")
    if any(x != x or x in {float("inf"), float("-inf")} for x in numbers):
        raise ValueError(
            "List contains invalid numeric values (e.g., NaN or Infinity)."
        )

    if not numbers:
        return None

    return sum(numbers) / len(numbers)
