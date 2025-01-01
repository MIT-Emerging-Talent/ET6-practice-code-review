# Solution: Find the Largest Number in a List


def find_largest_number(numbers):
    """
    Finds the largest number in a list of integers.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: The largest number in the list.
    """
    # Initialize the largest number with the first element of the list
    largest = numbers[0]

    # Loop through each number in the list
    for num in numbers:
        # Update the largest number if a bigger number is found
        if num > largest:
            largest = num

    # Return the largest number
    return largest
