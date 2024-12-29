#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-29

@author: Sukhrob Muborakshoev
"""


def count_character_occurrences(text: str, char: str | None) -> int | str:
    if char is None:
        return text

    if len(char) != 1:
        raise ValueError("The char parameter must be a single character.")

    count = 0
    for current_char in text:
        if current_char == char:
            count += 1

    return count
