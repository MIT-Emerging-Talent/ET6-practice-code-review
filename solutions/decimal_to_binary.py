def decimal_to_binary(decimal):
    """
    Convert a decimal number to its binary representation.

    :param decimal: int, the decimal number to convert
    :return: str, binary representation of the decimal number
    """
    if not isinstance(decimal, int):
        raise ValueError("Input must be an integer.")
    if decimal < 0:  # Check for negative numbers
        raise ValueError("Negative numbers are not allowed.")
    return bin(decimal).replace("0b", "")


# Example usage
if __name__ == "__main__":
    # Get user input for the decimal number
    user_input_decimal = int(
        input("Enter a decimal number: ")
    )  # Take input from the user
    # Call the function to convert to binary
    print(
        f"The binary representation of {user_input_decimal} is {decimal_to_binary(user_input_decimal)}"
    )
