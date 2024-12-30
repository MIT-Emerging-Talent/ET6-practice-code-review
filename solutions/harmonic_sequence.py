def harmonic_sequence(a, d, n):
    """
    The function creates harmonic sequence, based on formula: A(n): 1/ (a +(n-1) *d)

    Parameters:
    a (int): First term
    d (int): Common difference
    n (int): Number of terms to generate

    Returns:
    List: List containing the harmonic sequence

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
    sequence = []
    if n <= 0:
        return sequence
    if a == 0 and d == 0:
        return [0] * n
    for i in range(1, n + 1):
        term = 1 / (a + (i - 1) * d)
        sequence.append(term)
    return sequence
