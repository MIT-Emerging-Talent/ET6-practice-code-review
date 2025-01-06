#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the number of distinct subsequences of one
string (target_str) in another string (source_str).
(LeetCode problem copied from
https://leetcode.com/problems/distinct-subsequences/)

Module contents:
    - distinct_subsequences: Computes the number of
    distinct subsequences of target_str in source_str using recursion
    with memoization.
    - _count_subsequences_recursive: A helper function to compute subsequences
    using recursion and memoization.

Dependencies:
    - functools: Used for the `cache` decorator for memoization.

Notes:
    - Implements a recursive approach with memoization to
    avoid recalculating overlapping subproblems.
    - Time complexity: O(len(source_str) * len(target_str)).
    - Space complexity: O(len(source_str) * len(target_str)).

Created on 26 12 2024
@author: Mohamed-Elnageeb
"""

import sys
from functools import cache  # Importing cache for memoization

sys.setrecursionlimit(10**6)  # Increase the limit to support deep recursion


def distinct_subsequences(source_str: str, target_str: str) -> int:
    """
    Computes the number of distinct subsequences of string target_str
    in string source_str.

    This function uses a recursive approach with memoization to efficiently
    calculate the number of ways string target_str can appear as a
    subsequence in source_str.

    Time Complexity:
        O(len(source_str) * len(target_str)): Each subproblem is solved
        once due to memoization.

    Space Complexity:
        O(len(source_str) * len(target_str)): Memoization table stores
        intermediate results.

    Parameters:
        source_str: str
            The source string in which to find subsequences.
        target_str: str
            The target string to match as a subsequence.

    Returns:
        int: The number of distinct subsequences of target_str in source_str.

    Raises:
        TypeError: If the inputs are not strings.

    Examples:
    >>> distinct_subsequences("rabbbit", "rabbit")
    3

    >>> distinct_subsequences("abc", "abc")
    1

    >>> distinct_subsequences("abc", "def")
    0

    >>> distinct_subsequences("aaa", "aa")
    3
    """
    # Validate input
    if not isinstance(source_str, str):
        raise TypeError("Input source_str must be a string.")
    if not isinstance(target_str, str):
        raise TypeError("Input target_str must be a string.")

    @cache
    def _count_subsequences_recursive(source_idx: int, target_idx: int) -> int:
        """
        A helper function to recursively compute the number of subsequences
        with memoization.

        This function calculates how many distinct ways
        the substring target_str[target_idx:] can appear as a subsequence
        in the substring source_str[source_idx:].

        Parameters:
            source_idx: int
                Current index in string source_str.
            target_idx: int
                Current index in string target_str.

        Returns:
            int: The number of ways target_str[target_idx:] can appear
            as a subsequence in source_str[source_idx:].

        Explanation of Recursion:
            - Base Case 1: If target_idx == len(target_str), all
            characters of target_str have been matched, so return 1.
            - Base Case 2: If `source_idx == len(source_str)`, the
            end of source_str is reached without matching
            all of target_str, so return 0.
            - Recursive Steps:
                - Exclude the current character of source_str
                (`_count_subsequences_recursive(source_idx + 1, target_idx)`).
                - Include the current character of source_str
                if it matches target_str[target_idx]
                `_count_subsequences_recursive(source_idx + 1,target_idx + 1)`.

        Notes on @cache:
            - The `cache` decorator is used to memoize the
            results of function calls.
            - It ensures that the function does not recompute the result
            for the same arguments (source_idx, target_idx) more than once.
            - This optimization is crucial for reducing the time complexity
            from exponential (O(2^len(source_str))) to
              polynomial (O(len(source_str) * len(target_str))).
            - The cached results are stored in memory, so repeated calls with
            the same parameters are extremely fast.

        """

        # All characters of target_str are matched, so increment the count
        if target_idx == len(target_str):
            return 1
        # Reached the end of source_str without matching
        # all characters of target_str
        if source_idx == len(source_str):
            return 0

        # Exclude the current character of source_str and continue
        result = _count_subsequences_recursive(source_idx + 1, target_idx)

        # Include the current character of source_str if it
        # matches target_str[target_idx]
        if source_str[source_idx] == target_str[target_idx]:
            result += _count_subsequences_recursive(source_idx + 1, target_idx + 1)

        return result

    # Start the recursion from the beginning of both strings
    return _count_subsequences_recursive(0, 0)
