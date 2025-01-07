"""
Module for determining if a string represents a valid number.

This module contains the following:
    - `Solution`: A class that provides a method to validate if a string is a numeric value.

Created on: January 3, 2025.

@author: ABRAHAM ANYAK

Challenge source: Leetcode.

Description:
    This module provides a method to determine whether a given string
    represents a valid number. The method handles various formats, such as
    integers, floating-point numbers, and scientific notation.

    The primary method is:
    - `is_number`: Determines if a given string is numeric.
"""


class Solution:
    """
    A class that provides a method to check if a string is a valid number.

    Methods:
        is_number(s): Determines if the given string represents a valid numeric value.
    """

    @staticmethod
    def is_number(s):
        """
        Determines if the given string represents a valid number.

        Parameters:
            s (str): The string to validate.

        Returns:
            bool: True if the string represents a valid number, False otherwise.

        Examples:
            >>> sol = Solution()
            >>> sol.is_number("42")
            True
            >>> sol.is_number("3.14")
            True
            >>> sol.is_number("1e10")
            True
            >>> sol.is_number("abc")
            False
            >>> sol.is_number("")
            False
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")

        # Regular expression to validate numeric strings
        number_regex = re.compile(r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$")
        return bool(number_regex.match(s))
