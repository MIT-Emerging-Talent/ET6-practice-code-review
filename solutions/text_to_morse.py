#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting texts into Morse code

Module contents:
- morse_code: corresponding Morse code for each letter, number and some symbols.

Created on 4 Jan 2025
@author: Ahmed Hussein
"""


def text_to_morse(text: str) -> str:
    """The function converts a given text into Morse code. It processes each character of the input text and and concerts it to its corresponding Morse code representation.
    Letters: A - Z, Numbers: Positive integrs and zero, Symbols: , . ? / - ( )

    Parameters:
        text: string, the text that needs converting


    Returns -> string, the corresponding Morse code

    Raises:
        AssertionError: if the argument is not a string
        TypeError: if the character has no corresponding Morse code

    >>> text_to_morse("A")
    '.-'

    >>> text_to_morse("Hi")
    '.... ..'

    >>> text_to_morse("forza milan")
    '..-. --- .-. --.. .- / -- .. .-.. .- -.'

    >>> text_to_morse("CQD DE MGY")
    '-.-. --.- -.. / -.. . / -- --. -.--'

    >>> text_to_morse("/-)")
    '-..-. -....- -.--.-'

    """

    assert isinstance(text, str)

    morse_code_dic = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ",": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
        " ": "/",
    }

    morse_code = []

    # Iterate through each character and give corresponding Morse code
    for char in text.upper():
        if char in morse_code_dic:
            morse_code.append(morse_code_dic[char])
        else:
            raise ValueError(f"character: {char} has no corresponding Morse code ")

    return " ".join(morse_code)
