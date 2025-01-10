"""
kronecker_product.py

This module provides a function to compute the Kronecker product (matrix_a ⊗ matrix_b)
of two matrices matrix_a and matrix_b, which combines them into a larger matrix by multiplying
each element of matrix_a by the entire matrix matrix_b.

Author: Fahed Daibes
Date: Thu Jan 9 2025
Group: ET6-foundations-group-16

Functions:
- kronecker_product(matrix_a, matrix_b):
Computes the Kronecker product (matrix_a ⊗ matrix_b) of two matrices.
"""


def kronecker_product(matrix_a, matrix_b):
    """
    Computes the Kronecker product of two matrices.

    Parameters:
    - matrix_a (list of lists): The first matrix (2D list).
    - matrix_b (list of lists): The second matrix (2D list).

    Returns:
    - list of lists: The Kronecker product of matrix_a and matrix_b.

    Raises:
    - AssertionError: If inputs are not lists, not 2D, or are empty.

    Examples:
        >>> matrix_a = [[1, 2], [3, 4]]
        >>> matrix_b = [[0, 5], [6, 7]]
        >>> kronecker_product(matrix_a, matrix_b)
        [[0, 5, 0, 10], [6, 7, 12, 14], [0, 15, 0, 20], [18, 21, 24, 28]]

        >>> matrix_a = [[1]]
        >>> matrix_b = [[1, 2], [3, 4]]
        >>> kronecker_product(matrix_a, matrix_b)
        [[1, 2], [3, 4]]

        >>> matrix_a = [[1, 0], [0, 1]]
        >>> matrix_b = [[2, 3], [4, 5]]
        >>> kronecker_product(matrix_a, matrix_b)
        [[2, 3, 0, 0], [4, 5, 0, 0], [0, 0, 2, 3], [0, 0, 4, 5]]

        >>> kronecker_product("matrix_a", matrix_b)
        Traceback (most recent call last):
            ...
        AssertionError: Inputs must be 2D lists.

        >>> kronecker_product([[]], matrix_b)
        Traceback (most recent call last):
            ...
        AssertionError: Input lists cannot be empty.

        >>> kronecker_product([[1, 2, 3]], matrix_b)
        Traceback (most recent call last):
            ...
        AssertionError: Inputs must be 2D lists.
    """
    # Defensive checks
    assert isinstance(matrix_a, list) and isinstance(matrix_b, list), (
        "Inputs must be 2D lists."
    )
    assert len(matrix_a) > 0 and len(matrix_b) > 0, "Input lists cannot be empty."
    assert isinstance(matrix_a[0], list) and isinstance(matrix_b[0], list), (
        "Inputs must be 2D lists."
    )
    assert all(len(row) == len(matrix_a[0]) for row in matrix_a), (
        "Each row in matrix_a must have the same number of columns."
    )
    assert all(len(row) == len(matrix_b[0]) for row in matrix_b), (
        "Each row in matrix_b must have the same number of columns."
    )

    # Dimensions of matrix_a and matrix_b
    a_rows, a_cols = len(matrix_a), len(matrix_a[0])
    b_rows, b_cols = len(matrix_b), len(matrix_b[0])

    # Resultant matrix dimensions
    result_rows = a_rows * b_rows
    result_cols = a_cols * b_cols

    # Initialize the result matrix
    result = [[0] * result_cols for _ in range(result_rows)]

    # Calculate the Kronecker product
    for i in range(a_rows):
        for j in range(a_cols):
            for k in range(b_rows):
                for n in range(b_cols):
                    result[i * b_rows + k][j * b_cols + n] = (
                        matrix_a[i][j] * matrix_b[k][n]
                    )

    return result
