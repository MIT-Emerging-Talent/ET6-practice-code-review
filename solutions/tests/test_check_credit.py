#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for check_credit function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: typical 'AMEX', 'MASTERCARD', 'VISA' and 'INVALID' cases
    - Edge cases: strings with zeroes and very long numbers
    - Defensive tests: 
        - invalid inputs such as non-string and empty string
        - invalid strings with floats, negative integers, and alphanumeric inputs
    
Created on 4-Jan-2025

@author: Aung Myin Moe
"""

import unittest

from solutions.check_credit import check_credit

class TestCheckCredit(unittest.TestCase):
    """Test suite for the check_credit function."""

    # Standard test cases
    def test_amex_1(self):
        """A standard test case for an 'AMEX' card"""
        card_number = '378282246310005'
        self.assertEqual(check_credit(card_number), 'AMEX')
        
    def test_amex_2(self):
        """A standard test case for an 'AMEX' card"""
        card_number = '371449635398431'
        self.assertEqual(check_credit(card_number), 'AMEX')
    
    def test_mastercard_1(self):
        """A standard test case for a 'MASTERCARD' card"""
        card_number = '5555555555554444'
        self.assertEqual(check_credit(card_number), 'MASTERCARD')
        
    def test_mastercard_2(self):
        """A standard test case for a 'MASTERCARD' card"""
        card_number = '5105105105105100'
        self.assertEqual(check_credit(card_number), 'MASTERCARD')
        
    def test_visa_1(self):
        """A standard test case for a 'VISA' card"""
        card_number = '4111111111111111'
        self.assertEqual(check_credit(card_number), 'VISA')
        
    def test_visa_2(self):
        """A standard test case for a 'VISA' card"""
        card_number = '4012888888881881'
        self.assertEqual(check_credit(card_number), 'VISA')
        
    def test_invalid_1(self):
        """A standard test case for an 'INVALID' card"""
        card_number = '1234567890'
        self.assertEqual(check_credit(card_number), 'INVALID')
    
    def test_invalid_2(self):
        """A standard test case for an 'INVALID' card"""
        card_number = '0000170180'
        self.assertEqual(check_credit(card_number), 'INVALID')
    
    # Edge cases
    def test_long_string(self):
        """An edge case for a long string"""
        card_number = '1111111111111111111222222222222222233333333333334444444444444555555555555666666666666777777777777'
        self.assertEqual(check_credit(card_number), 'INVALID')
        
    def test_zero_string(self):
        """An edge case for a string of zeros"""
        card_number = '00000000000000000'
        self.assertEqual(check_credit(card_number), 'INVALID')
    
    # Defensive cases    
    def test_not_string_1(self):
        """A defensive case for a non-string input"""
        card_number = 1240
        with self.assertRaises(AssertionError):
            check_credit(card_number)
            
    def test_not_string_2(self):
        """A defensive case for a non-string input"""
        card_number = 123.04
        with self.assertRaises(AssertionError):
            check_credit(card_number)
            
    def test_empty_string(self):
        """A defensive case for an empty string input"""
        card_number = ''
        with self.assertRaises(ValueError):
            check_credit(card_number)
            
    def test_not_int_1(self):
        """A defensive case for an input string with alphanumeric characters"""
        card_number = 'HELLO_123'
        with self.assertRaises(ValueError):
            check_credit(card_number)
            
    def test_not_int_2(self):
        """A defensive case for an input string with floating points"""
        card_number = '123.890'
        with self.assertRaises(ValueError):
            check_credit(card_number)
            
    def test_not_int_3(self):
        """A defensive case for an input string containing characters other than 0-9"""
        card_number = '123-234'
        with self.assertRaises(ValueError):
            check_credit(card_number)
            
    def test_negative_int(self):
        """A defensive case for an input string with negative integers"""
        card_number = '-12345677'
        with self.assertRaises(ValueError):
            check_credit(card_number)
            