#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 01.01.2025
@author: Anna Shumylina

Function generates the list of even numbers extracted from the text.

Parameter:
    text (str): The function extracts even numbers from this string.

Returns:
    list: A list of even numbers pulled from the text.

Examples:
    >>> only_even_numbers("")
    []
    >>> only_even_numbers("2+2-4*7=-24")
    ["2", "2", "4", "24"]
    >>> only_even_numbers("Today is January 2nd 2025")
    ["2"]

Raises:
    ValueError: If the input is not a string.
"""

import re


def only_even_numbers(text: str) -> list[str]:
    """Extract even numbers from a given text string."""

    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    all_numbers = re.findall(r"\d+", text)  # extracting all numbers from text

    even_numbers = []  # defining result list

    # checking if the extracted number is even
    for number in all_numbers:
        if int(number) % 2 == 0:
            even_numbers.append(number)  # adding even number to the final list

    return even_numbers
