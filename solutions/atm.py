"""
Welcome to WIT International Bank.
This program is designed to operate the ATM system, allowing users to perform
various banking transactions such as checking their account balance, depositing cash,
withdrawing money, and managing their accounts securely.

Thank you for choosing WIT International Bank. Your satisfaction is our priority.
"""


def show_balance(balance):
    """
    Display the user's current account balance.

    Parameters:
        balance (float): The current balance in the user's account.
    """
    print(f"Your Balance is ${balance:.2f}")


def deposit(balance, amount):
    """
    Deposit a specified amount into the user's account.

    Parameters:
        balance (float): The current balance in the user's account.
        amount (float): The amount to deposit.

    Returns:
        float: The updated balance after deposit.
    """
    if amount < 0:
        print("That is not a valid amount!")
        return balance
    else:
        return balance + amount


def withdraw(balance, amount):
    """
    Withdraw a specified amount from the user's account.

    Parameters:
        balance (float): The current balance in the user's account.
        amount (float): The amount to withdraw.

    Returns:
        float: The updated balance after withdrawal, or the original balance if the operation is invalid.
    """
    if amount > balance:
        print("Invalid amount! Insufficient balance.")
        return balance
    elif amount < 0:
        print("Amount must be greater than 0.")
        return balance
    else:
        return balance - amount


def main():
    """
    Main function to operate the ATM system.

    Allows the user to perform actions such as checking balance, depositing funds,
    withdrawing funds, or exiting the system. Repeats until the user chooses to exit.
    """
    balance = 0
    is_running = True

    while is_running:
        print("\nWIT ATM MENU!")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                show_balance(balance)
            elif choice == 2:
                try:
                    amount = float(input("Enter an amount to deposit: "))
                    balance = deposit(balance, amount)
                except ValueError:
                    print("Invalid input! Please enter a numerical value.")
            elif choice == 3:
                try:
                    amount = float(input("Enter an amount to withdraw: "))
                    balance = withdraw(balance, amount)
                except ValueError:
                    print("Invalid input! Please enter a numerical value.")
            elif choice == 4:
                is_running = False
            else:
                print("That is not a valid choice.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

    print(
        "Thank you for choosing WIT International Bank.\nThe Bank that you can always rely on."
    )


if __name__ == "__main__":
    main()
