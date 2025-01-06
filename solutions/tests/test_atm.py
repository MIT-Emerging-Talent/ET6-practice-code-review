#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit test for the ATM
Created on: 2025/01/02
By: Fikremichael Mamo
"""

import unittest
from ..atm import show_balance, deposit, withdraw

"""
    Unit tests for ATM functions: show_balance, deposit, and withdraw.
"""


class TestATMFunctions(unittest.TestCase):
    def test_show_balance(self):
        """
        Test that show_balance correctly formats and returns the account balance.
        """
        self.assertEqual(show_balance(100.50), "Your Balance is $100.50")
        self.assertEqual(show_balance(0), "Your Balance is $0.00")

    def test_deposit(self):
        """
        Test that deposit correctly updates the balance and handles invalid inputs.
        """
        self.assertEqual(deposit(100, 50), (150, "Deposit successful."))
        self.assertEqual(
            deposit(100, -10), (100, "Invalid amount! Please enter a positive number.")
        )
        self.assertEqual(
            deposit(100, 0), (100, "Invalid amount! Please enter a positive number.")
        )

    def test_withdraw(self):
        """
        Test that withdraw correctly updates the balance and handles invalid and insufficient funds.
        """
        self.assertEqual(withdraw(100, 50), (50, "Withdrawal successful."))
        self.assertEqual(withdraw(100, 150), (100, "Insufficient balance."))
        self.assertEqual(withdraw(100, -10), (100, "Amount must be greater than 0."))
        self.assertEqual(withdraw(100, 0), (100, "Amount must be greater than 0."))


if __name__ == "__main__":
    unittest.main()
