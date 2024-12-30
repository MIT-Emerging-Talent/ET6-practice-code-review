def harmonic_sequence(a, d, n):
    """
    The function creates harmonic sequence, based on formula: A(n): 1/ (a +(n-1) *d)

    Parameters:
    a (int): First term
    d (int): Common difference
    n (int): Number of terms to generate

    Returns:
    List: List containing the harmonic sequence

    Assertions:
    - a must be integer
    - d must be integer
    - n must be integer

    Examples:
    >>> harmonic_sequence(1, 1, 1)
    [1.0]
    >>> harmonic_sequence(1, 1, 0)
    []
    >>> harmonic_sequence(0, 0, 5)
    [0.0, 0.0, 0.0, 0.0, 0.0]
    >>> harmonic_sequence(1, 1, -1)
    []
    >>> harmonic_sequence(1, 1, 5)
    [1.0, 0.5, 0.3333333333333333, 0.25, 0.2]
    >>> harmonic_sequence(2, 2, 3)
    [0.5, 0.3333333333333333, 0.25]
    >>> harmonic_sequence(1, 5, 10)
    [1.0, 0.2, 0.05, 0.02, 0.01, 0.004, 0.0016, 0.00064, 0.000256, 0.0001024]

    """
    # Assert an error if any input is not integer
    assert isinstance(a, int), "A must be integer"
    assert isinstance(d, int), "D must be integer"
    assert isinstance(n, int), "N must be integer"

    # Create an empty list to save the sequence
    sequence = []
    # If n is less than or equal to 0, return empty list
    if n <= 0:
        return sequence
    # If a and d are equal to 0, return a list of n zeros
    if a == 0 and d == 0:
        return [0] * n
    # If all inputs are greater than 1, return the sequence
    for i in range(1, n + 1):
        term = 1 / (a + (i - 1) * d)
        sequence.append(term)
    return sequence
