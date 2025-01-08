"""
This module provides a solution for checking if a number is a palindrome.
"""


class Solution(object):
    def is_palindrome(self, x: int) -> bool:
        """
        Check if the given integer is a palindrome.

        A palindrome is a number that reads the same backward as forward.

        :param x: Integer to check
        :type x: int
        :raises ValueError: If the input is not an integer.
        :return: True if the integer is a palindrome, False otherwise
        :rtype: bool

        Examples:
            >>> s = Solution()
            >>> s.is_palindrome(121)
            True
            >>> s.is_palindrome(-121)
            False
            >>> s.is_palindrome(10)
            False
        """

        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        # Comparing number's string with its reverse
        str_x = str(x)
        return str_x == str_x[::-1]
