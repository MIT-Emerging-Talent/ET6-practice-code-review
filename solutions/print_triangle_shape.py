"""
This function prints a triangle shape made of asterisks ("*").

Module: print_triangle_shape

Functions:
    triangle_printer(user_input):

@Author: Mukuna Kabeya
@Date: 2024-01-06
"""


def triangle_printer(user_input):
    """
    This function prints a triangle shape made of asterisks ("*"), where the number of rows
    corresponds to the integer value provided by the user. The triangle is printed with the
    top-most row having one asterisk, and each subsequent row increases the number of asterisks
    in an odd-numbered sequence, centered according to the total number of rows.

    Parameters
    ----------
    user_input : str
        The number of rows for the triangle shape. This input should be a string representation
        of a positive integer greater than 1. The function expects an integer input, which
        will determine the height of the triangle.

    Raises
    ------
    TypeError
        If the input is not an integer or a string that can be converted to an integer.
    ValueError
        If the input is an integer less than or equal to 1, as the triangle shape requires
        at least two rows.

    Returns
    -------
    list
        A list of strings, where each string represents a row of the triangle. Each row
        contains a combination of leading spaces and asterisks that form the desired shape.
        The list is ordered such that the first element is the top row, and the last element
        is the bottom-most row.

    Example
    -------
    >>> triangle_printer(3)
    [
        "  *",
        " ***",
        "*****"
    ]

    This function first validates the input, ensuring that the provided value is a positive integer
    greater than 1. If the input is invalid, the function raises appropriate exceptions. It then
    calculates the necessary spaces and asterisks for each row and appends each row to a list.
    Finally, the triangle is printed line by line and the list of rows is returned.

    Variables:
    ----------
    s : str
        A string representing the leading spaces required for each row of the triangle.
        The number of spaces is determined by subtracting the current row index from the
        total number of rows, ensuring that the triangle is centered.

    x : str
        A string representing the asterisks for each row of the triangle. The number of
        asterisks follows an odd-numbered sequence (1, 3, 5, 7, etc.), calculated as
        `2 * i - 1`, where `i` is the current row index.

    holder : list
        A list that stores each row of the triangle as a string. Each row contains
        a combination of spaces (`s`) and asterisks (`x`) that form the desired shape.
        This list is returned after the triangle is printed.
    """
    if not str(user_input).isdigit():
        raise TypeError("Please enter an integer only!")
    rows = int(user_input)
    if rows <= 1:
        raise ValueError("Please provide an integer greater than 1.")
    holder = []
    for i in range(1, rows + 1):
        s = " " * (rows - i)
        x = "*" * (2 * i - 1)
        holder.append(s + x)
    # print("\n".join(holder))
    return holder
