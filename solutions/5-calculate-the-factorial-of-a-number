def calculate_factorial(n):
    """
    Function to calculate the factorial of a given non-negative integer.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the number.
    """
    # Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial


# Testing the function
test_cases = [5, 0, 7, -1, 10]  # Adding a negative number to check error handling

# Displaying the results
for num in test_cases:
    try:
        if num < 0:
            raise ValueError(f"Factorial is not defined for negative numbers: {num}")
        result = calculate_factorial(num)
        print(f"Input: {num}, Output: {result}")
    except ValueError as e:
        print(e)
