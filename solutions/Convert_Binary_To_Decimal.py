# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Summery
this code is part of group 21 homework assignment for MIT-Emerging-Talent
Created 01/01/2025
Author : Taher Shaban
"""


def conv_bin_dec(biner: str) -> int:
    """this function convert binary numbers to decimal
    Parameters:
    bi [str] : this string contain 0's and 1's represent the binary number
    return:
    dec (str): a string represent the binary number as decimal
    Raises: AssertionError:
    if the figure contains characters other than '0' or '1'
    >>> conv_biner_dec("00000110")
    6
    >>> conv_biner_dec("00001111")
    15
    >>> conv_biner_dec("00010010")
    18
    >>> conv_biner_dec("001r001")
    AssertionError:"Argument is not a binary number."
    """
    biner = biner.replace(" ", "")  # remove spaces from the argument
    assert all(
        char in "01" for char in biner
    ), (
        "argument is not a binary number."
    )  # an assertion error raises if the argument is not a binary numbers
    rev_bin = biner[::-1]  # reverse the binary number from left to right

    bin_list = list(
        map(int, rev_bin)
    )  # convert the argue from a string to integer list

    i = len(bin_list)

    dec = 0

    for n in range(i):
        dec += bin_list[n] * pow(2, n)

    return dec
