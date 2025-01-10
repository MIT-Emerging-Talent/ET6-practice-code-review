#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welcome to WIT International Bank.
This program operates the ATM system, allowing users to perform
various banking transactions,
including checking their balance, depositing cash, and withdrawing
money securely.

Thank you for choosing WIT International Bank. Your satisfaction is
our priority.
Created on: 2025/01/02
By: Fikremichael Mamo
"""


def show_balance(balance: float) -> str:
    """
    Returns the formatted balance as a string.

    >>> show_balance(0)
    'Your Balance is $0.00'
    >>> show_balance(100.50)
    'Your Balance is $100.50'
    >>> show_balance(1234.56)
    'Your Balance is $1234.56'
    """
    return f"Your Balance is ${balance:.2f}"


def deposit(balance: float, amount: float) -> tuple[float, str]:
    """
    Deposits an amount into the balance and returns the new balance
    with a message.

    >>> deposit(100, 50)
    (150, 'Deposit successful.')
    >>> deposit(100, -10)
    Traceback (most recent call last):
        ...
    ValueError: Amount must be a positive number.
    >>> deposit(100, 'fifty')
    Traceback (most recent call last):
        ...
    TypeError: Amount must be a number.
    """
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number.")
    if amount < 0:
        raise ValueError("Amount must be a positive number.")
    balance += amount
    return balance, "Deposit successful."


def withdraw(balance: float, amount: float) -> tuple[float, str]:
    """Withdraw a specified amount from the user's account.
    >>> withdraw(100, 50)
    (50, 'Withdrawal successful.')
    >>> withdraw(50, 50)
    (0, 'Withdrawal successful.')
    >>> withdraw(50, 60)
    (50, 'Insufficient balance.')
    >>> withdraw(100, -10)
    Traceback (most recent call last):
        ...
    ValueError: Amount must be a positive number.
    >>> withdraw(100, 'fifty')
    Traceback (most recent call last):
        ...
    TypeError: Amount must be a number.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    if amount > balance:
        return balance, "Insufficient balance."
    return balance - amount, "Withdrawal successful."


def main():
    """Main function to operate the ATM system."""
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
                amount = float(input("Enter an amount to deposit: "))
                balance, message = deposit(balance, amount)
                print(message)
            elif choice == 3:
                amount = float(input("Enter an amount to withdraw: "))
                try:
                    balance, message = withdraw(balance, amount)
                    print(message)
                except ValueError as e:
                    print(e)
            elif choice == 4:
                print("Thank you for choosing WIT International Bank.")
                break
            else:
                print("Invalid choice. Please choose between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
