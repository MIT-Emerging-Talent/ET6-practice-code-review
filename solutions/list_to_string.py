#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: List to String Converter

Description:
    This module provides a function to convert a list of elements (integers, floats,
    strings, booleans) into a single concatenated string. It handles various data
    types and ensures that all elements are appropriately converted to strings and joined together.

Module Contents:
    - list_to_string(lst: list) -> str:
        Converts a list of elements into a single concatenated string.
        Ensures proper handling of different data types and raises appropriate errors
        for invalid inputs.

Author: Falaq Youniss
Date: 30/12/2024
"""


def list_to_string(lst: list) -> str:
    """
    Converts a list of elements into a single concatenated string.

    Args:
        lst (list): A list of items which can include integers, floats, strings,
                    or booleans.

    Returns:
        str: A string that combines all elements of the list.

    Raises:
        AssertionError:
            - If the input is not a list.
            - If the input is `None`.
            - If the list is empty.

    >>> list_to_string([1, -4, 3.14])
    '1-43.14'

    >>> list_to_string([True, 'hello'])
    'Truehello'

    >>> list_to_string(['cat', 'hat', 'bat'])
    'cathatbat'
    """
    # Validate Input
    assert isinstance(lst, list), "Input must be a list."
    assert lst is not None, "The input cannot be None."
    assert len(lst) > 0, "The list cannot be empty."

    # Initialize an empty result string
    result = ""

    # Iterate through the list and convert each element to a string
    for element in lst:

        result += str(element)  # Convert each element to string and concatenate

    return result
