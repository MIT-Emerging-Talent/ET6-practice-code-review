#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 12.26.2024

@author: Anna Shumylina

Function generates the list the characters that
are located at odd positions in the string

Parameter:
text (str): function takes characters from this string

Returns -> (str) list of characters that are located
at odd positions in the string

>>> odd_position_elements('')
''

>>> odd_position_elements('1234567')
'1357'

>>> odd_position_elements('1234567')
'1357'

>>> odd_position_elements('Hello World!')
'HloWrd'

"""


def odd_position_elements(text: str) -> str:
    # raising Value error if input is not a string
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    final_text = ""  # defining result string
    char_index = 1  # defining character index in the string

    for char in text:
        if char_index % 2 != 0:  # checking if the index is odd (1-based index)
            final_text += char  # adding element to the final string

        char_index += 1

    return final_text
