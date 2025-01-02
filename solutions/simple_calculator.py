# simple_calculator.py


def add(x: float, y: float) -> float:
    """
    Adds two numbers and returns the result.

    Arguments:
    x -- First number to be added
    y -- Second number to be added

    Returns:
    float -- Sum of x and y

    Example:
    >>> add(1, 2)
    3
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """
    Subtracts the second number from the first and returns the result.

    Arguments:
    x -- The number to subtract from
    y -- The number to subtract

    Returns:
    float -- The result of x - y

    Example:
    >>> subtract(5, 3)
    2
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    Multiplies two numbers and returns the result.

    Arguments:
    x -- The first number
    y -- The second number

    Returns:
    float -- The result of x * y

    Example:
    >>> multiply(3, 4)
    12
    """
    return x * y


def divide(x: float, y: float) -> float:
    """
    Divides the first number by the second and returns the result.

    Arguments:
    x -- The dividend
    y -- The divisor

    Returns:
    float -- The result of x divided by y, or a string if division by zero

    Raises:
    ValueError -- If y is zero

    Example:
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    'Error! Division by zero.'
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    """
    A simple interactive calculator program that supports addition, subtraction,
    multiplication, and division. The program runs until the user decides to exit.

    The user can input numeric values and select an operation. The result will be
    displayed, and the user can continue calculating or exit the program.

    Example:
    >>> calculator()
    Welcome to the Simple Calculator!
    Select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    Enter choice (1/2/3/4/5): 1
    Enter first number: 2
    Enter second number: 3
    The result is: 5
    """
    print("Welcome to the Simple Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == "5":
            print("Thank you for using the calculator! Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

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


if __name__ == "__main__":
    calculator()
