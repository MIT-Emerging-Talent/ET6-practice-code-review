#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Write a function that takes a list and returns the sum of that list.

"""
A module for getting the sum of numbers in a list

Module contents:
    sum_of_list: returns the sum of numbers in a list.

Created on 02/01/2025
@author: Ndubuisi Agbo
"""


def sum_of_list(numbers: list) -> int | float:
    """Gives the sum of the elements in a list.

    Parameters:
        numbers (list): the list of numbers to sum.

    Returns:
        int or float: the sum of the numbers in the list.

    Raises:
        AssertionError: if the list contains a non-numeric element.
        AssertionError: if the argument is not a list.

    >>> sum_of_list([3,6,9])
    18

    >>> sum_of_list([4.2, 6.9, 7.1])
    18.2

    >>> sum_of_list([8, 3.8, 1, 9])
    21.8
    """

    assert isinstance(numbers, list), "numbers must be a list"

    # checks that all the elements in the list are a number
    for num in numbers:
        assert isinstance(num, int | float)

    return sum(numbers)
