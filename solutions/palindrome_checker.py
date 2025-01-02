#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a given string is a palindrome.

This module provides a function to verify whether an input string reads 
the same backward as forward, ignoring spaces, punctuation, and case sensitivity.

Module contents:
    - is_palindrome: Determines if a string is a palindrome.

Created on 2/1/2025
@author: Caesar Ghazi
"""
def palindrome_checker(text: str) -> bool:

    assert isinstance(text, str), "Text must be a string."


    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    

    return cleaned_text == cleaned_text[::-1]
