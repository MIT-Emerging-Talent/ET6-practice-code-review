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
    number = 1
    while number < n:
        number *= 2
    return number == n
