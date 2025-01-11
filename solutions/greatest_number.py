# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A  module for finding the largest number in a list

Module content:
    - greatest_number: Returns the largest number in a list.

Created on: 6/1/2025
@author: Razan Ibrahim
Group: Matrix (ET foundations group 16 )
"""


def greatest_number(data: list) -> float | int:
    """
    This function receives a list of values and returns the greatest numeric value
    within the list. The list may contain integers and floats. If the list contains
    valid numeric values, the greatest value is returned.

    Parameters:
        data: list, a list of values that can include integers, floats, and non-numeric elements.

    Returns-> float, the greatest numeric value is a list,
    which will represent either integer or float,
    depending on the input.

    Raises:
        AssertionError: if the list don't contain either integer or float value
        AssertionError: if the input is not a list.
        AssertionError: if the input is an empty list.

    >>> greatest_number ([10, -5, 3.2, 99, 0])
    99
    >>> greatest_number ([-2.5, -1.1, -100])
    -1.1
    >>> greatest_number ([ 19, 30, 29.8])
    30
    >>> greatest_number ([77, 2, 4, 7])
    77
    """

    assert isinstance(data, list), "The input isn't a list"
    assert data != [], "This is an empty list "
    assert any(
        isinstance(item, (int, float)) and not isinstance(item, bool) for item in data
    ), "The list doesn't contain any numeric value (integer or float, excluding bool)."

    # initialize the greatest value to None
    greatest_value = data[0]
    # Iterate through the list to determine the greatest number
    for item in data:
        if isinstance(item, (int, float)):
            if item >= greatest_value:
                greatest_value = item
    return greatest_value
