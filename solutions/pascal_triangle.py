#!/usr/bin/python3

"""
Pascal Triangle Interview Challenge

This script contains a function that generates Pascal's triangle up to the nth row.
Pascal's triangle is a mathematical concept where each number is the sum of the
two numbers directly above it. The first and last element in each row is always 1.
The function returns a list of lists representing the triangle, with each inner list
corresponding to a row.

Usage:
    Call the `pascal_triangle(n)` function with an integer `n` to generate
    the first `n` rows of Pascal's triangle.

Example:
    pascal_triangle(5)
    returns:
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
"""


def pascal_triangle(n):
    """
    Generates a list of lists representing the Pascal's triangle up to the nth row.

    Pascal's triangle is a triangular array where each number is the sum of the two
    numbers directly above it.The first and last element in each row is always 1.
    The function returns the triangle as a list of lists, where each inner list
    corresponds to a row in the triangle.

    Args:
        n (int): The number of rows of the Pascal's triangle to generate. Must be a +ve integer.

    Returns:
        list: A list of lists where each inner list contains the numbers of the corresponding
              row in Pascal's triangle.

    Example:
        pascal_triangle(5)
        returns:
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]

    If `n` is less than or equal to 0, the function returns an empty list.

    Example:
        pascal_triangle(0)
        returns: []
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
