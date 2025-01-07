"""
This function asks the user to enter a number and checks if the number
is even or odd. It then returns the result as a string.

Created on 05 01 2025
@author: Eman Alfalouji.

"""


def check_number_type(user_input: str) -> str:
    """
    The function asks the user to enter a number and determines if it is even or odd.


    Parameters:
        user_input (str):  str
    Raises:
        AssertionError: if the argument is not a integer

    Returns:
        results will be a text whether "The number is even", "The number is odd"
        or "Enter a valid number "
        Examples :
        >>> check_odd_check("20")
        "The number is even"
        >>> check_odd_check("11")
        "The number is odd"
    """
    assert user_input.strip().isdigit(), "Enter a valid number"

    number = int(user_input.strip())
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"


if __name__ == "__main__":
    user_number = input("Hi! please enter a number: ")
    try:
        print(check_number_type(user_number))
    except AssertionError as e:
        print(e)
