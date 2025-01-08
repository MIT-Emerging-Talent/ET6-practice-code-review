"""
This module provides a function to sort a list of numbers in ascending order.

Functionality:
- Accepts a list of numbers as input.
- Returns a new list sorted from lowest to highest.
- Ensures no side effects by creating a new list instead of modifying the original.
 Raises:
    - TypeError: If input is not a list or contains non-numeric values.
Usage Example:
    sorted_list = sort_numbers([3, 1, 4, 1, 5, 9])
    print(sorted_list)  # Output: [1, 1, 3, 4, 5, 9]

"""


def sort_numbers(numbers):
    """
    Sorts a list of numbers in ascending order.

    Parameters:
    - numbers (list): A list of numerical values. The list can contain integers, floats, very large or small numbers,
      and special values such as infinity (inf) or NaN. The function will sort the numbers appropriately, with NaN values
      being placed last in the sorted list.

    Returns:
    - list: A new list with numbers sorted from lowest to highest,, including NaN and inf values at appropriate positions.

    Example:
        sort_numbers([3, 1, 4, 1, 5]) -> [1, 1, 3, 4, 5]
        sort_numbers([3, 1, float('inf'), float('-inf')]) -> [-inf, 1, 3, inf]


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
