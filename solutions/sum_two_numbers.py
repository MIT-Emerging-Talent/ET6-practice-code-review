def sum_two_numbers(num1: int | float, num2: int | float) -> str:
    """
    This function sums up two given numbers.

    Parameters:
    num1 (int | float): The first number to add.
    num2 (int | float): The second number to add.

    Returns:
    str: A string indicating the sum of num1 and num2.

    Raises:
        TypeError: If either argument is not an integer or float.
        ValueError: If either argument is None or an empty value.

    Example:
    >>> sum_two_numbers(7, 10)
    'The sum of 7 and 10 is 17'
    """
    if num1 is None or num2 is None or num1 == "" or num2 == "":
        raise ValueError("Enter two numbers to use this function")

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both arguments must be int or float.")

    summation = num1 + num2
    return f"The sum of {num1} and {num2} is {round(summation, 2)}"


# print(sum_two_numbers(3))
