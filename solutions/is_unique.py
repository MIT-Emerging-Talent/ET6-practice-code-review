#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if all characters in a string are unique.

Module contents:
    - is_unique: Verifies if all characters in a given string are unique.

Created on 2025-01-01
Author: Ava Abdullah
"""


def is_unique(s: str) -> bool:
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return len(set(s)) == len(s)
