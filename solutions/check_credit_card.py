#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if a credit card number is a valid American Express, MasterCard, or Visa card number.

Module contents:
    - check_credit_card function

Created on 4-Jan-2025
@author: Aung Myin Moe
"""


# ---- define function ----
def check_credit_card(card_number: str) -> str:
    """Checks if a credit card number is a valid American Express, MasterCard, or Visa card number

    Strategy:
        1. check the validity of the credit card number
            - multiply every other digit by 2, starting with second-to-last digit
            - add those products' digits together
            - add the sum to the sum of the digits that weren't multiplied by 2
            - if the total's last digit is 0, number is valid

        2. differentiate the type of credit card based on the structure of its number
            - American Express
                - 15 digits, starts with 34 or 37
            - MasterCard
                - 16 digits, starts with 51, 52, 53, 54 or 55
            - Visa
                - 13 or 16 digits, starts with 4

    Args: card_number (str)
        - the credit card number to validate
        - must be a string containing only digits (0-9), with an appropriate length for the card type

    Returns: str
        - return 'AMEX', 'MASTERCARD', 'VISA', or 'INVALID' according to the validity and the structure of card number

    Raises:
        AssertionError: if card_number is not a string
        ValueError: if card_number contains other than numeric characters (0-9)

    >>> check_credit_card('378282246310005')
    'AMEX'

    >>> check_credit_card('5555555555554444')
    'MASTERCARD'

    >>> check_credit_card('4111111111111111')
    'VISA'

    >>> check_credit_card('1234567890')
    'INVALID'
    """
    # Ensure the input is in the correct format and contains only numbers
    assert isinstance(card_number, str), "Card number must be formatted as a string"

    if not card_number.isdigit():
        raise ValueError("Card number must only contain numeric characters (0-9)")

    # Check the validity of the credit card number
    sum_1 = 0
    sum_2 = 0

    # Multiply every other digit by 2, starting with second-to-last digit
    for char in card_number[-2::-2]:
        digit_product = int(char) * 2

        # Sum each digit of the result number after multiplying by 2
        digit_sum = 0
        digit_sum = sum(int(digit) for digit in str(digit_product))

        sum_1 += digit_sum

    # Sum every other digit by 2, starting with the last digit
    for char in card_number[-1::-2]:
        sum_2 += int(char)

    # If the total sum's last digit is 0, then the number is valid
    total_sum = sum_1 + sum_2

    if str(total_sum)[-1] != "0":
        return "INVALID"

    # For a valid card number, differentiate the type of credit card based on its structure
    else:
        # American Express numbers have 15 digits that starts with digits '34' or '37'
        if len(card_number) == 15 and card_number.startswith(("34", "37")):
            return "AMEX"

        # MasterCard numbers have 16 digits that starts with digits '51', '52', '53', '54' or '55'
        elif len(card_number) == 16 and card_number.startswith(
            ("51", "52", "53", "54", "55")
        ):
            return "MASTERCARD"

        # Visa numbers have 13 or 16 digits that starts with the digit '4'
        elif len(card_number) in [13, 16] and card_number.startswith("4"):
            return "VISA"

        # We will return 'INVALID' for other types of cards
        else:
            return "INVALID"
