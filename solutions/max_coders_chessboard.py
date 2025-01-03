"""
This module provides a function to calculate the maximum number of Coders
that can be placed on an n x n chessboard such that no two Coders attack
each other. It also generates the configuration of the chessboard.
"""

from typing import List, Tuple


def max_coders_chessboard(n: int) -> Tuple[int, List[str]]:
    """
    Calculates the maximum number of Coders that can be placed on an n x n
    chessboard without any two Coders attacking each other.

    Arguments:
    n : int
        The size of the chessboard (1 ≤ n ≤ 1000).

    Returns:
    Tuple[int, List[str]]
        - The maximum number of Coders that can be placed.
        - The configuration of the chessboard as a list of strings.

    Raises:
    ValueError: If `n` is not in the range 1 to 1000 inclusive.

    Examples:
    >>> max_coders_chessboard(3)
    (5, ['C.C', '.C.', 'C.C'])

    >>> max_coders_chessboard(4)
    (8, ['C.C.', '.C.C', 'C.C.', '.C.C'])

    >>> max_coders_chessboard(1)
    (1, ['C'])
    """
    if not (1 <= n <= 1000):
        raise ValueError(
            "The size of the chessboard must be between 1 and 1000 inclusive."
        )

    count = 0
    board = []

    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:  # Checkerboard pattern
                row.append("C")
                count += 1
            else:
                row.append(".")
        board.append("".join(row))

    return count, board
