def sum_range(start, end):
    """
    Calculate the sum of all integers from start to end (inclusive).

    Args:
        start (int): The starting integer.
        end (int): The ending integer.

    Returns:
        int: The sum of all integers from start to end.

    Raises:
        TypeError: If start or end is not an integer.
    """
    assert isinstance(start, int), "start must be an integer"
    assert isinstance(end, int), "end must be an integer"
    # Ensure start is less than or equal to end
    if start > end:
        start, end = end, start
    # Calculate the sum of the range
    total = 0
    for number in range(start, end + 1):
        total += number
    return total
