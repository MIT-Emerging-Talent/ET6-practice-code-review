def find_largest_number(numbers: List[int]) -> int:
    """
    Finds the largest number in a list of integers.

    Parameters:
    numbers (list): A non-empty list of integers.

    Returns:
    int: The largest number in the list.

    Raises:
    ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    return max(numbers)


def test_find_largest_number():
    """
    Unit tests for the find_largest_number function.
    """
    # Test with a list of positive numbers
    assert find_largest_number([3, 1, 7, 0, 5]) == 7

    # Test with a list of negative numbers
    assert find_largest_number([-10, -20, -3, -50]) == -3

    # Test with a list of zeros
    assert find_largest_number([0, 0, 0, 0]) == 0

    # Test with a list of mixed positive and negative numbers
    assert find_largest_number([1, -1, 3, -5, 2]) == 3

    # Test with a single element
    assert find_largest_number([5]) == 5

    # Test with a sorted list
    assert find_largest_number([100, 200, 300]) == 300

    # Test with an empty list
    try:
        find_largest_number([])
    except ValueError as e:
        assert str(e) == "The list cannot be empty."


if __name__ == "__main__":
    # Run tests
    test_find_largest_number()
    print("All tests passed!")
