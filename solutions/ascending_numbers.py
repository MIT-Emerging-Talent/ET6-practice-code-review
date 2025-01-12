#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module that takes integers and arrange them in ascending order
It prints them in ascending order

Created on 25 12 2024

@author : Osei Agyemang Sarfo

"""


def ascending_numbers(number, final_list=None):
    """Generates list of number in ascending order

    Parameters:
    number -> list[int] of numbers
    final_list -> initialized to none


    Returns:
    list[int] of numbers in ascending order.

    >>> ascending_numbers([10,2,-5,7,5])
    [-5, 2, 5, 7, 10]

    >>> ascending_numbers([12,45,-54,8])
    [-54, 8, 12, 45]
    >>> ascending_numbers([-5,-8,34,55])
    [-8, -5, 34, 55]
    """
    # checks if number is not a string
    assert number is not str

    # checks if number is not a boolean
    assert number is not bool
    # Takes the minimum value in list.
    # Rearrange them in ascending order.

    if final_list is None:
        final_list = []
    while number:
        value_holder = min(number)
        number.remove(value_holder)
        final_list.append(value_holder)
    return final_list
