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
    try:
        decimal = int(input("Enter a decimal number: "))  # Take input from the user
        binary = decimal_to_binary(decimal)
        print(f"The binary representation of {decimal} is {binary}")
    except ValueError as e:
        print(e)
