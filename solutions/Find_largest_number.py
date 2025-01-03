def largest_num(numbers):
    """
    This function takes a list of numbers as input and returns the largest number.

    Parameters:
       A list of numbers.

    Returns:
        float: The largest number in the list.
    """

    if not numbers:
        raise ValueError("The  list is empty.")
    return max(numbers)


# Example How it will work
numbers = [3, 5, 7, 2, 8, 10]
print("The largest number is:", largest_num(numbers))
