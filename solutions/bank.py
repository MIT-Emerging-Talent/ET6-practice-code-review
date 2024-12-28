def main() -> None:
    """
    Main function to get user input and print the value based on the greeting.

    This function prompts the user for a greeting and then determines and prints the value 
    associated with that greeting using the `value` function.
    """
    greeting: str = input("Greetings: ")  # Get user input as a string
    print(value(greeting))  # Call the value function and print its result


def value(greeting: str) -> int:
    """
    Determine the value of a greeting based on certain conditions.

    This function returns an integer value based on the provided greeting. If the greeting 
    contains the word "hello", the value is 0. If the first character of the greeting is "h", 
    the value is 20. Otherwise, the value is 100.

    Parameters:
    greeting (str): The greeting input by the user.

    Returns:
    int: The value of the greeting based on specific conditions.
        - 0 if "hello" is in the greeting.
        - 20 if the first character of the greeting is "h".
        - 100 for all other cases.
    """
    greeting = greeting.lower()  # Convert the greeting to lowercase for case-insensitivity

    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":  # Check if the first character is 'h'
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
