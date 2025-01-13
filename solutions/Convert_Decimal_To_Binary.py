"""Summery
this code is part of group 21 homework assignment for MIT-Emerging-Talent
Created 01/01/2025
Author : Taher Shaban
"""


def conv_dec_bin(dec: float) -> int:
    """this function convert decimal numbers to binary
    Parameters:
    dec [int] : this string contain 0's and 1's represent the binary number

    return:

    bin (int): an integral represent the binary number as decimal

    Raises: AssertionError:

    if the figure is not an integral.

    >>> conv_dec_int(6)
    110
    >>> conv_dec_int(15)
    1111
    >>> conv_dec_int(18)
    "10"
    >>> conv_dec_int("new")
    AssertionError:"Argument is not a integral number."
    """
    assert isinstance(dec, int), "argument is not a decimal number."
    bin = []
    while dec > 0:
        bin.append(int(dec % 2))
        if dec % 2 == 0:
            dec = dec / 2
        else:
            dec = (dec - 1) / 2
    bin_str = "".join(map(str, bin))
    bin_str = bin_str[::-1]
    return bin_str


# print (conv_dec_bin(18))
