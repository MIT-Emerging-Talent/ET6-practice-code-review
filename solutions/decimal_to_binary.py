#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting a decimal number to binary.

Module contents:
    - decimal_to_binary: Generates a binary representation of a decimal number.

Created on Dec 25, 2025.
@author: AL-HASSEN SABEEH
"""


def decimal_to_binary(decimal_number: int) -> str:
    """Generates a binary representation of a decimal number as a string.

    Parameters:
        decimal_number: int, greater than or equal to zero

    Returns -> string shows the binary representation of a decimal number

    Raises:
        AssertionError: if the argument is not an integer
        AssertionError: if the argument is less than 0

    >>> decimal_to_binary(0)
    '0'

    >>> decimal_to_binary(1)
    '1'

    >>> decimal_to_binary(4)
    '100'

    >>> decimal_to_binary(8)
    '1000'

    >>> decimal_to_binary(7)
    '111'

    >>> decimal_to_binary(255)
    '11111111'
    
    >>> decimal_to_binary(2796202)
    '1010101010101010101010'
    """
    # the decimal number should be an integer greater than 0
    assert isinstance(decimal_number, int), "decimal number is not an integer"
    assert decimal_number >= 0, "decimal number is less than 0"
    #Implementation of the strategy using recursion.
    #The function recursively converts a decimal number to binary by
    #dividing the number by 2 and appending the remainder to the result.
    if decimal_number // 2 == 0:
        #Base case f(0)="0", f(1)="1"
        return str(decimal_number)
    #Recursive case 𝑓(𝑛)=𝑓(𝑛//2)+str(𝑛 mod  2)for 𝑛>1
    #       /Recursive Case/  /Reduction Step/    /Concatenating Result/
    return decimal_to_binary(decimal_number//2) + str(decimal_number%2)
