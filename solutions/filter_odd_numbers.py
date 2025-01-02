"""
Module: print_odd_numbers_in_list

Description: This module provides a function to filter odd numbers from a given list.
The function handles various types of inputs, adheres to constraints, and returns a list
containing only odd integers.

Created on: 01 01 25
@author: Muhammad Shahroz
"""

from typing import List, Union


def filter_odd_numbers(input_list: List[Union[int, float, str, None]]) -> List[int]:
    """
    Filters and returns a list of odd integers from the given input list.

    Parameters:
       input_list (List[Union[int, float, str, None]]): A list containing elements of various types.

    Returns:
        List[int]: A list containing only the odd integers from the input.

    Raises:
        AssertionError: If the input is not a list.

    Examples:
        >>> filter_odd_numbers([1, 2, -3, 4.5, 5])
        [1, -3, 5]

        >>> filter_odd_numbers([1, 2, "three", 4.5, None])
        [1]

        >>> filter_odd_numbers([])
        []
    """
    # Ensure the input is a list
    assert isinstance(input_list, list), "Input must be a list."

    # Step 1: Filter only integers
    integer_list = []
    for element in input_list:
        if isinstance(element, int):
            integer_list.append(element)

    # Step 2: Filter only odd numbers from the integers
    odd_number_list = []
    for number in integer_list:
        if number % 2 != 0:
            odd_number_list.append(number)

    return odd_number_list
