def sum_range(start, end):
    """Calculates the sum of all integers from start to end, inclusive."""
    # Ensure start is less than or equal to end
    assert isinstance (start, int), "start must be an integer" 
    assert isinstance (end, int), "end must be an integer"
    if start > end:
        start, end = end, start
    total = 0
    for number in range(start, end + 1):
        total += number
    return total
