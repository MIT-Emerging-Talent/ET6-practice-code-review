"""
matrix_spiral_traversal.py

This module provides a function to traverse a 2D matrix in spiral order.

Author: Fahed Daibes
Date: Sat Jan 4 2025
Group: ET6-foundations-group-16

Functions:
- spiral_traverse(matrix): Traverses a matrix in spiral order and returns the result.
"""


def spiral_traverse(matrix):
    """
    Traverse a 2D matrix in spiral order.

    Parameters:
    - matrix (list of list of int): A 2D list representing the matrix to traverse.

    Returns:
    - list of int: A list of elements from the matrix in spiral order.

    Raises:
    - ValueError: If the input is not a valid 2D list or contains non-numeric elements.

    Example:
    >>> spiral_traverse([
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

    >>> spiral_traverse([
    ...     [1, 2],
    ...     [3, 4]
    ... ])
    [1, 2, 4, 3]

    >>> spiral_traverse([
    ...     [1]
    ... ])
    [1]

    >>> spiral_traverse([
    ...     [1, 2, 3, 4],
    ...     [5, 6, 7, 8],
    ...     [9, 10, 11, 12]
    ... ])
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    >>> spiral_traverse([
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ])
    [1, 2, 3, 6, 5, 4]

    >>> spiral_traverse([])
    []

    >>> spiral_traverse([
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9],
    ...     [10, 11, 12]
    ... ])
    [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]

    >>> spiral_traverse([
    ...     [1, 2, 3, 4, 5],
    ...     [6, 7, 8, 9, 10],
    ...     [11, 12, 13, 14, 15],
    ...     [16, 17, 18, 19, 20]
    ... ])
    [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

    >>> spiral_traverse([
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9],
    ...     [10, 11, 12]
    ... ])
    [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    """
    # Defensive assertions
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise ValueError("Input must be a 2D list (matrix).")
    if any(not all(isinstance(item, (int, float)) for item in row) for row in matrix):
        raise ValueError("All elements in the matrix must be numeric.")

    result = []

    while matrix:
        # Add the first row to the result
        result += matrix.pop(0)

        # Rotate the remaining matrix counter-clockwise
        if matrix and matrix[0]:
            matrix = [list(row) for row in zip(*matrix)][::-1]

    return result
