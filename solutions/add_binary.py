"""
Module for adding and manipulating binary numbers.

This module contains the following:
    - `add_binary`: A method to compute the sum of two binary strings.
    - `is_valid_binary`: A method to validate a binary string.

Created on: January 7, 2025.

@author: ABRAHAM ANYAK

Challenge source: Leetcode.

Description:
    This module provides a class `Solution` containing methods for
    binary addition and validation.
"""


class Solution:
    """
    Class for binary operations, including addition and validation.

    Methods:
        add_binary(a: str, b: str) -> str:
            Computes the sum of two binary strings.

        is_valid_binary(s: str) -> bool:
            Checks if a given string is a valid binary number.
    """

    @staticmethod
    def add_binary(a, b):
        """
        Computes the sum of two binary strings.

        Parameters:
            a (str): The first binary string.
            b (str): The second binary string.

        Returns:
            str: The sum of the two binary strings as a binary string.

        Examples:
            >>> Solution.add_binary("11", "1")
            '100'
            >>> Solution.add_binary("1010", "1011")
            '10101'
            >>> Solution.add_binary("1101", "101")
            '10010'
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    @staticmethod
    def is_valid_binary(s):
        """
        Checks if a given string is a valid binary number.

        Parameters:
            s (str): The string to validate.

        Returns:
            bool: True if the string is a valid binary number, False otherwise.
        """
        return all(c in "01" for c in s)
