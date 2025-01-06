"""
This module provides a function to sort a list of numbers in ascending order.

Functionality:
- Accepts a list of numbers as input.
- Returns a new list sorted from lowest to highest.
- Ensures no side effects by creating a new list instead of modifying the original.

Usage Example:
    sorted_list = sort_numbers([3, 1, 4, 1, 5, 9])
    print(sorted_list)  # Output: [1, 1, 3, 4, 5, 9]
"""


def sort_numbers(numbers):
    """
    Sorts a list of numbers in ascending order.

    Parameters:
    - numbers (list): A list of numerical values.

    Returns:
    - list: A new list with numbers sorted from lowest to highest.

    Example:
        sort_numbers([3, 1, 4, 1, 5]) -> [1, 1, 3, 4, 5]

    Raises:
    - TypeError: If input is not a list or contains non-numeric values.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numeric.")

    return sorted(numbers)


if __name__ == "__main__":
    # Example usage
    example_list = [3, 1, 4, 1, 5, 9]
    sorted_list = sort_numbers(example_list)
    print(f"Sorted List: {sorted_list}")
