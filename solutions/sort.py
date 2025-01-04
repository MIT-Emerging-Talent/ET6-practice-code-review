"""
    A module for sorting numbers in a list in ascending order using Bubble Sort algorithm.

Module contents:
    - sort: A function to sort a list of integers in ascending order.

Created on 03 January 2025
@author: Safiya_Hash

"""


def sort(numbers: list[int]) -> list[int]:
    """
    The function takes an list of integers and returns a sorted list of integers from smallest to largest using bubble sort algorithm.
        numbers (list[int]): This is the list of numbers we want to sort
        list[int]: A sorted list of integers from smallest to largest
        numbers == [-float("inf"), 0, float("inf")]

    Parameters:
        Numbers (int): We will sort numbers list in this integer
        Numbers (list[int]): this is the list of numbers we want to sort

    Returns:
        List(int): The same list of integers sorted from smallest to largest

    Raises:
        AssertionError: if the argument is not an integer
        AssertionError: if the argument is not a list
        AssertionError: if the list contains a string
        AssertionError: if the value of integer is a float

    assert isinstance(numbers, list), "integers should be in a list form"
    assert all(isinstance(num, int) for num in numbers), "all list outputs must be integers"
    assert all(not isinstance(num, float) for num in numbers), "int should not be floats"

    Examples:
        >>> sort([3])
        [3]
        >>> sort([1, 2, 3])
        [1, 2, 3]
        >>> sort([5, 9, 4, 3, 7])
        [3, 4, 5, 7, 9]
        >>> sort([7, 7, 1, 2, 9])
        [1, 2, 7, 7, 9]
        >>> sort([6, 8, 4, 2, 10, 25, 19])
        [2, 4, 6, 8, 10, 19, 25]
        >>> sort([53, 5, 47, -6, -85, 32])
        [-85, -6, 5, 32, 47, 53]
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")

    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            # Compare adjacent elements up to the unsorted part
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
        # Stop iteration if the list is sorted.

    return numbers
