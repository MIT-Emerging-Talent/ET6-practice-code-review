#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether a given integer is a power of two.

Module contents:
    - is_power_of_two(n): Function to determine if `n` is a power of two.

Created on 2024-12-31
@author: Gennadii Ershov
"""


def is_power_of_two(n: int) -> bool:
    # Negative numbers and 0 cannot be powers of two
    if n <= 0:
        return False

    # Odd numbers (except 1) are not powers of two
    if n % 2 != 0 and n != 1:
        return False

    # Use a loop to check for powers of two
    potential_power = 1
    while potential_power < n:
        potential_power *= 2
    return potential_power == n
