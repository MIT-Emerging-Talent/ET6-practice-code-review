#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 01.01.2025

@author: Anna Shumylina

Function generates the list of even numbers extracted from the text

Parameter:
text (str): function extracts even numbers from this string

Returns -> list of even numbers pulled from the text

>>> only_even_numbers('')
[]

>>> only_even_numbers('2+2-4*7=-24')
['2', '2', '4', '24']

>>> only_even_numbers('Today is January 2nd 2025')
['2']

"""


def only_even_numbers(text: str) -> str:
    import re  # importing Regular Expressions package

    even_numbers = []  # defining result list

    # extracting all numbers from the string and adding them to the list
    all_numbers = re.findall("\\d+", text)

    # checking if the extracted number is even
    for number in all_numbers:
        if int(number) % 2 == 0:
            even_numbers.append(number)  # adding even number to the final list

    return even_numbers
