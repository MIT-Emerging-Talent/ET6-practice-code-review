#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welcome to WIT International Bank.
This program operates the ATM system, allowing users to perform various banking transactions,
including checking their balance, depositing cash, and withdrawing money securely.

Thank you for choosing WIT International Bank. Your satisfaction is our priority.
Created on: 2025/01/02
By: Fikremichael Mamo
"""


def show_balance(balance):
    """
    Display the user's current account balance.

    Parameters:
        balance (float): The current balance in the user's account.

    Returns:
        str: A formatted string showing the balance.
    """
    return f"Your Balance is ${balance:.2f}"


def deposit(balance, amount):
    """
    Deposit a specified amount into the user's account.

    Parameters:
        balance (float): The current balance in the user's account.
        amount (float): The amount to deposit.

    Returns:
        float: The updated balance after the deposit.
        str: An error message if the amount is invalid.
    """
    if not isinstance(amount, (float, int)) or amount <= 0:
        return balance, "Invalid amount! Please enter a positive number."
    return balance + amount, "Deposit successful."


def withdraw(balance, amount):
    """
    Withdraw a specified amount from the user's account.

    Parameters:
        balance (float): The current balance in the user's account.
        amount (float): The amount to withdraw.

    Returns:
        float: The updated balance after withdrawal.
        str: An error message if the operation is invalid.
    """
    if amount > balance:
        return balance, "Insufficient balance."
    elif amount <= 0:
        return balance, "Amount must be greater than 0."
    return balance - amount, "Withdrawal successful."


def main():
    """
    Main function to operate the ATM system.

    Allows the user to perform actions such as checking balance, depositing funds,
    withdrawing funds, or exiting the system. Repeats until the user chooses to exit.
    """
    balance = 0.0

    while True:
        print("\nWIT ATM MENU!")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                print(show_balance(balance))
            elif choice == 2:
                try:
                    amount = float(input("Enter an amount to deposit: "))
                    balance, message = deposit(balance, amount)
                    print(message)
                except ValueError:
                    print("Invalid input! Please enter a numerical value.")
            elif choice == 3:
                try:
                    amount = float(input("Enter an amount to withdraw: "))
                    balance, message = withdraw(balance, amount)
                    print(message)
                except ValueError:
                    print("Invalid input! Please enter a numerical value.")
            elif choice == 4:
                print(
                    "Thank you for choosing WIT International Bank.\nThe Bank that you can always rely on."
                )
                break
            else:
                print("That is not a valid choice.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
