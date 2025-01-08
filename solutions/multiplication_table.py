#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating the multiplication table for a given number.

Module contents:
- multiplication_table: returns the multiplication table for input numbers in a specified range.

Created on 03 Jan 2025
Team Number: 28
Team Name: MIT Alpha
Author: Salih Adam
"""


def multiplication_table(n: int | float, first: int, last: int) -> str:
    """
    Returns the multiplication table for an input number in a defined range.

    Parameters:
    n: int | float, number for which the multiplication table is generated.
    first: int, first multiplier in the table, must be in the range (last >= first > 0).
    last: int, last multiplier in the table, must be greater than zero.

    Returns -> string: the output multiplication table

    Raises:
        AssertionError: if the number "n" is not integer or float.
        AssertionError: if the first  multiplier is not an integer.
        AssertionError: if the last  multiplier is not an integer.
        AssertionError: if the last multiplier is not greater than zero.
        AssertionError: if the first  multiplier is not within range (last >= first > 0).

    >>> print(multiplication_table(-3, 1, 2))
    Table:
            -3 x 1 = -3
            -3 x 2 = -6
            End
    >>> print(multiplication_table(11, 7, 9))
    Table:
            11 x 7 = 77
            11 x 8 = 88
            11 x 9 = 99
            End
    >>> print(multiplication_table(17, 6, 10))
    Table:
            17 x  6 = 102
            17 x  7 = 119
            17 x  8 = 136
            17 x  9 = 153
            17 x 10 = 170
            End
    """
    # Ensuring correct argument input

    assert isinstance(n, (int, float)), "Input number must be integer or float"
    assert isinstance(first, int), "First multiplier must be an integer"
    assert isinstance(last, int), "Last multiplier must be an integer"
    assert last > 0, "Last multiplier must be greater than zero"
    assert last >= first > 0, "First multiplier out of range"

    # Calculating width of the largest multiplier to set the table alignment.

    width = len(str(last))

    # Starting the table in a new line for proper alignment.

    table = """Table:\n"""

    # Generate each multiplication line separately and add it to the bottom of
    # the table until it is completed.

    for i in range(first, last + 1):
        if i == last:  # Handling last line separately to properly end the table
            table += f"""        {n} x {i:{width}} = {round(n * i, 2)}\n        End"""
        else:
            table += f"""        {n} x {i:{width}} = {round(n * i, 2)}\n"""

    return table
