"""Unit test for the ATM"""

import unittest
from atm import show_balance, deposit, withdraw


class TestATMFunctions(unittest.TestCase):
    """
    Unit test class for ATM functions.

    Contains test cases to validate the functionality of the deposit, withdraw,
    and show_balance functions under various conditions.
    """

    def test_show_balance(self):
        """
        Test the show_balance function to ensure it executes without raising exceptions.
        """
        try:
            show_balance(100.50)
        except Exception as e:
            self.fail(f"show_balance raised an exception: {e}")

    def test_deposit_valid_amount(self):
        """
        Test the deposit function with a valid amount to ensure the balance is updated correctly.
        """
        self.assertEqual(deposit(100, 50), 150)

    def test_deposit_invalid_amount(self):
        """
        Test the deposit function with an invalid (negative) amount to ensure the balance remains unchanged.
        """
        self.assertEqual(deposit(100, -20), 100)

    def test_withdraw_valid_amount(self):
        """
        Test the withdraw function with a valid amount to ensure the balance is updated correctly.
        """
        self.assertEqual(withdraw(100, 50), 50)

    def test_withdraw_insufficient_balance(self):
        """
        Test the withdraw function with an amount greater than the balance to ensure the balance remains unchanged.
        """
        self.assertEqual(withdraw(100, 150), 100)

    def test_withdraw_negative_amount(self):
        """
        Test the withdraw function with a negative amount to ensure the balance remains unchanged.
        """
        self.assertEqual(withdraw(100, -20), 100)


if __name__ == "__main__":
    unittest.main()
