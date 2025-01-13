#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test for the ATM
Created on: 2025/01/02
By: Fikremichael Mamo
"""

import unittest
from solutions.atm import show_balance, deposit, withdraw

"""
    Unit tests for ATM functions: show_balance, deposit, and withdraw.
"""


class TestATMFunctions(unittest.TestCase):
    def test_show_balance_zero_balance(self):
        """Test show_balance formats zero balance."""
        self.assertEqual(show_balance(0), "Your Balance is $0.00")

    def test_show_balance_positive_balance(self):
        """Test show_balance formats a positive balance."""
        self.assertEqual(show_balance(100.50), "Your Balance is $100.50")

    def test_deposit_success(self):
        """Test deposit adds funds correctly."""
        self.assertEqual(deposit(100, 50), (150, "Deposit successful."))

    def test_deposit_negative_amount(self):
        """Test deposit with negative amount raises ValueError."""
        with self.assertRaises(ValueError):
            deposit(100, -10)

    def test_deposit_invalid_type(self):
        """Test deposit with a non-numeric input raises TypeError."""
        with self.assertRaises(TypeError):
            deposit(100, "fifty")

    def test_withdraw_success(self):
        """Test withdraw reduces balance correctly."""
        self.assertEqual(withdraw(100, 50), (50, "Withdrawal successful."))

    def test_withdraw_exact_balance(self):
        """Test withdraw with exact balance leaves zero."""
        self.assertEqual(withdraw(50, 50), (0, "Withdrawal successful."))

    def test_withdraw_insufficient_funds(self):
        """Test withdraw when balance is insufficient."""
        self.assertEqual(withdraw(50, 60), (50, "Insufficient balance."))

    def test_withdraw_negative_amount(self):
        """Test withdraw with negative amount raises ValueError."""
        with self.assertRaises(ValueError):
            withdraw(100, -10)

    def test_withdraw_invalid_type(self):
        """Test withdraw with a non-numeric input raises TypeError."""
        with self.assertRaises(TypeError):
            withdraw(100, "fifty")


if __name__ == "__main__":
    unittest.main()
