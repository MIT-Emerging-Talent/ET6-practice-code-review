#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains a function to generate a multiplication table.
module contents:
    - multiplication_table: Function to generate a multiplication table from 1 up to n.

created on 05/01/2025 #dd/mm/yyyy
@author: Mohamed Saeed
"""


def multiplication_table(number: int, length: int) -> list:
    """
    Function to generate a multiplication table.

    A multiplication table is a table of numbers that shows the results of
    multiplying two numbers together.

    Parameters:
    number (int): The number to generate the multiplication table for.
    length (int): The length or range of the multiplication table.

    Returns:
    list: A list of integers representing the multiplication table.

    Raises:
        assertionError: If the input number is not an integer.
        assertionError: If the input length (range) is not an integer.
        assertionError: If the input number is not a positive integer.
        assertionError: If the input length (range) is not a positive integer.
        ValueError: If the input number is too large.
        ValueError: If the input range is too large.

    Examples:
    >>> multiplication_table(1, 5)
    [1, 2, 3, 4, 5]
    >>> multiplication_table(5, 10)
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    >>> multiplication_table(7, 3)
    [7, 14, 21]
    """
    max_upper_limit = 1000

    assert isinstance(number, int), "Input number must be an integer"
    assert isinstance(length, int), "Input length must be an integer"
    assert number > 0, "Number input must be a positive integer"
    assert length > 0, "length input must be a positive integer"
    assert number is not None, "Number input must not be None"
    assert length is not None, "length input must not be None"
    if number > max_upper_limit:
        raise ValueError("Input number is too large")
    if length > max_upper_limit:
        raise ValueError("Input length is too large")

    table = []
    for j in range(1, length + 1):
        product = number * j
        table.append(product)
    return table
