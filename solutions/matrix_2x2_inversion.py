#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for calculating the inverse of a matrix that has two rows
and two columns.

Module contents:
    - matrix_2x2_inversion: returns the inverse of a 2x2 matrix.

Created on 2024-12-26
Author: Awaab98
"""

def matrix_2x2_inversion(matrix: list[list[float]]) -> list[list[float]]:
    """
    Calculates the inverse of a 2x2 matrix.

    Parameters:
        matrix: list, a list of lists representing a 2x2 matrix in which 
        every element is either int of float.

    Returns:
        list: a list of lists representing the inverse of the input matrix.
        
    Raises:
        AssertionError: if the input matrix is not a 2x2 matrix.
        ValueError: if the determinant of input matrix is zero.
        TypeError: if the input matrix is not a list of lists.
        TypeError: if one of the elements of the input matrix is not int or float.
        
    Examples:
    >>> matrix_2x2_inversion([[1, 2], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    >>> matrix_2x2_inversion([[1.0, 2.0], [3.0, 4.0]])
    [[-2.0, 1.0], [1.5, -0.5]]
    >>> matrix_2x2_inversion([[1, 2.0], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    """
    return matrix
