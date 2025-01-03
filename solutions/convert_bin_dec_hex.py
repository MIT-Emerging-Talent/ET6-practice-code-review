#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""convert_bin_dec_hex

A program to convert binary to decimal, hexadecimal, and vice versa.

Created on 3/1/2025
Author: Aziz Azizi

"""


def convert_bin_dec_hex(
    number: int | str = None, from_base: int = None, to_base: int = None
) -> str:
    """Convert a number from one base to another.

    Parameters:
    number (int or str): The number to convert.
    from_base (int): The base of the input number.
    to_base (int): The base to convert the number to.

    Returns:
    str: The converted number as a string.

    doctest:
    >>> convert_bin_dec_hex(1010, 2, 10)
    '10'
    >>> convert_bin_dec_hex(1010, 2, 16)
    'A'
    >>> convert_bin_dec_hex(10, 10, 2)
    '1010'
    >>> convert_bin_dec_hex('A', 16, 10)
    '10'
    >>> convert_bin_dec_hex(10, 16, 2)
    '10000'
    >>> convert_bin_dec_hex('FFFFFF', 16, 2)
    '111111111111111111111111'
    >>> convert_bin_dec_hex(0, 16, 10)
    '0'
    >>> convert_bin_dec_hex(102, 2, 10)
    Traceback (most recent call last):
        ...
    ValueError: Invalid digit '2' for base 2
    >>> convert_bin_dec_hex(10, 10, 20)
    Traceback (most recent call last):
        ...
    ValueError: Invalid target base. Valid: 2(binary), 10(decimal), and 16(hexadecimal).
    >>> convert_bin_dec_hex('G', 16, 10)
    Traceback (most recent call last):
        ...
    ValueError: Invalid digit 'G' for base 16
    >>> convert_bin_dec_hex(10, 'B', 16)
    Traceback (most recent call last):
        ...
    ValueError: Invalid source base. Valid: 2(binary), 10(decimal), and 16(hexadecimal).
    >>> convert_bin_dec_hex(10, 16, 'A')
    Traceback (most recent call last):
        ...
    ValueError: Invalid target base. Valid: 2(binary), 10(decimal), and 16(hexadecimal).
    >>> convert_bin_dec_hex()
    Traceback (most recent call last):
        ...
    ValueError: All arguments (number, from_base, to_base) must be provided.
    """

    # Validate if all arguments are provided
    if number is None or from_base is None or to_base is None:
        raise ValueError("All arguments (number, from_base, to_base) must be provided.")

    # Validating bases
    valid_bases = {2, 10, 16}  # Binary, decimal, and hexadecimal
    if from_base not in valid_bases:
        raise ValueError(
            "Invalid source base. Valid: 2(binary), 10(decimal), and 16(hexadecimal)."
        )

    if to_base not in valid_bases:
        raise ValueError(
            "Invalid target base. Valid: 2(binary), 10(decimal), and 16(hexadecimal)."
        )

    # Convert the input number to a decimal (base 10) integer
    decimal_number = 0
    if from_base == 2:  # Binary to decimal
        binary_str = str(number)
        for digit in binary_str:
            if digit not in "01":  # Check if the digit is a valid binary digit
                raise ValueError(f"Invalid digit '{digit}' for base {from_base}")
            decimal_number = decimal_number * 2 + int(digit)
            # Multiply the current decimal number by 2 and add the binary digit
    elif from_base == 10:  # Decimal to decimal
        decimal_number = int(number)
    elif from_base == 16:  # Hexadecimal to decimal
        hex_str = str(number).upper()
        hex_digits = "0123456789ABCDEF"  # Valid hexadecimal digits
        for digit in hex_str:
            if digit not in hex_digits:
                raise ValueError(f"Invalid digit '{digit}' for base {from_base}")
            decimal_number = decimal_number * 16 + hex_digits.index(digit)
            # Multiply the current decimal number by 16 and add the hexadecimal digit

    # Convert the decimal number to the target base
    if to_base == 2:
        if decimal_number == 0:
            return "0"
        binary_number = ""
        while decimal_number > 0:
            binary_number = str(decimal_number % 2) + binary_number
            # Append the remainder of decimal_number divided by 2 to the binary_number string
            decimal_number //= 2
        return binary_number
    elif to_base == 10:
        return str(decimal_number)
    elif to_base == 16:
        if decimal_number == 0:
            return "0"
        hex_number = ""
        hex_digits = "0123456789ABCDEF"
        while decimal_number > 0:
            hex_number = hex_digits[decimal_number % 16] + hex_number
            # Append the corresponding hex digit
            decimal_number //= 16
        return hex_number
