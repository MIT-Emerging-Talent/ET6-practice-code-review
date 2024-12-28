#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for verifying integer inputs.

Module contents:
    - only_ints: A function to check if two parameters are both integers.

Created on 12 28 2024
@author: Mohammad
"""
def only_ints(param1, param2):
    """
    Using this function, you will be able to take two parameters, and it will return True
    if both parameters are integers, and otherwise it is false

    Parameters:
    param1 (int): The first parameter to check, expected to be an integer.
    param2 (int): The second parameter to check, expected to be an integer.

    Returns:
    bool: True if both parameters are integers, False otherwise.

    Raises:
    TypeError: If any of the parameters is not an integer.
    """
    if not isinstance(param1, int) or not isinstance(param2, int):
        return False # If either parameter isn't an integer, return False

    return True  # If both parameters are integers, return True
