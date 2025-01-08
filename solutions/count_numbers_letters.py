#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module provides a function to find the number of
letters, numbers and other characters in a given string.
Created on: 2025/1/6
@author: Hamidullah Rajabi
"""


def count_numbers_letters(user_input):
    """
    Counts the number of letters, numbers, and other characters in a given string input.

    Args:
        user_input (str): A string input from the user.

    Returns:
        dict: A dictionary with the counts of "Letters", "Numbers", and "Others".

    Raises:
        AssertionError: If `user_input` is not a string.
        AssertionError: If `user_input` exceeds the maximum allowed length.
        ValueError: If `user_input` is None.
        ValueError: If `user_input` is List.

    Example:
        >>> count_numbers_letters("abc123!@#")
        {'Numbers': 3, 'Letters': 3, 'Others': 3}
        >>> count_numbers_letters("123abc")
        {'Numbers': 3, 'Letters': 3, 'Others': 0}
        >>> count_numbers_letters("!!@@##")
        {'Numbers': 0, 'Letters': 0, 'Others': 6}
    """

    # Define a maximum allowed length for the input
    MAX_LENGTH = 100

    # Validating User Inputs
    if user_input is None:
        raise ValueError("Input must not be None.")

    if isinstance(user_input, list):
        raise ValueError("Input must not be a list")

    if not isinstance(user_input, str):
        raise AssertionError("Input must be a string")

    if len(user_input) > MAX_LENGTH:
        raise AssertionError(f"Input string must not exceed {MAX_LENGTH} characters.")

    # Initialize the counts for numbers, letters, and other characters
    counted = {"Numbers": 0, "Letters": 0, "Others": 0}

    # Iterate through each character in the input string
    for char in user_input:
        if char.isalpha():
            counted["Letters"] += 1
        elif char.isdigit():
            counted["Numbers"] += 1
        else:
            counted["Others"] += 1

    # Return the dictionary with counts
    return counted
