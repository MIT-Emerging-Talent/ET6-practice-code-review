
"""
A module for converting Roman numerals to integers.

Module contents: Takes a Roman numeral as input and returns its integer value.

Created on 2025-01-12

@author: Karina
"""


def roman_to_int(roman_str: str) -> int:
    """
    Convert a Roman numeral to an integer.

    Parameters:
    roman_str (str): The Roman numeral string to convert

    Returns:
    int: The integer value of the Roman numeral

    Raises:
    AssertionError: If the input is not a valid Roman numeral string

    Examples:
    >>> roman_to_int('III')
    3
    >>> roman_to_int('IV')
    4
    >>> roman_to_int('IX')
    9
    >>> roman_to_int('LVIII')
    58
    >>> roman_to_int('MCMXCIV')
    1994
    """
    # Input validation
    assert isinstance(roman_str, str), "Input must be a string"
    assert roman_str, "Input cannot be empty"
    valid_chars = set('IVXLCDM')
    assert all(c in valid_chars for c in roman_str.upper()), "Invalid Roman numeral characters"

    # Map of Roman numeral values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    # Iterate through the string in reverse order
    for char in reversed(roman_str.upper()):
        curr_value = roman_values[char]
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
        prev_value = curr_value

    return result
