# Simple Python Calculator
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def calculator():
    print("Welcome to the Simple Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user input
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user wants to exit
        if choice == "5":
            print("Thank you for using the calculator! Goodbye!")
            break

        # Make sure the user input is valid
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Perform the selected operation
            if choice == "1":
                print(f"The result is: {add(num1, num2)}")
            elif choice == "2":
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid input! Please choose a valid operation (1/2/3/4/5).")


# Run the calculator
calculator()
