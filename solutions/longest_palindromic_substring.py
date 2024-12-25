"""
This module provides a solution for finding the longest palindromic substring
in a given string using the "expand around center" technique.

A palindrome is a sequence of characters that reads the same backward as forward.
This implementation efficiently finds the longest palindromic substring in
O(n^2) time complexity with O(1) space complexity.
"""


class Solution:
    """
    A class that provides a method to find the longest palindromic substring in a string.

    The `longest_palindrome` method in this class implements the "expand around center"
    technique to identify and return the longest substring of a given string `s`
    that is a palindrome.

    Methods:
        longest_palindrome(s: str) -> str:
            Finds and returns the longest palindromic substring.
    """

    def longest_palindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in a given string.

        A palindrome is a sequence of characters that reads the same
        backward as forward. This function uses the "expand around center"
        technique to efficiently find the longest palindromic substring.

        Args:
            s (str): The input string to search for a palindromic substring.

        Returns:
            str: The longest palindromic substring found in the input string.
                If there are multiple substrings of the same maximum length,
                any one of them can be returned.

        Example:
            >>> solution = Solution()
            >>> solution.longest_palindrome("babad")
            'bab'  # 'aba' is also a valid answer
            >>> solution.longest_palindrome("cbbd")
            'bb'
            >>> solution.longest_palindrome("a")
            'a'
            >>> solution.longest_palindrome("")
            ''

        Time Complexity:
            O(n^2): For each character in the string, the algorithm potentially
                    expands to check all substrings centered around it.
        Space Complexity:
            O(1): No extra data structures proportional to the input size are used.
        """

        if not s or len(s) == 0:
            return ""

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes
            odd_palindrome = expand_around_center(i, i)
            # Even length palindromes
            even_palindrome = expand_around_center(i, i + 1)

            # Update the longest palindrome found so far
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest
