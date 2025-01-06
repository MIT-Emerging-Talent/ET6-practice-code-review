#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

"""
A module for multiplication of two numbers.

Module contents:
    multiply: multiply two numbers and returns the result.

Created on 06.01.2025
@author : Simi-Solola

"""


def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the result.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The result of multiplying `a` and `b`.
    """
    # Defensive assertion
    assert isinstance(a, (int, float)), "a must be a number"
    assert isinstance(b, (int, float)), "b must be a number"

    return a * b
