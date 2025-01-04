import string
import random

def password_generator(length):
    """
    Create a secure password with a mix of letters and numbers.

    This function generates a random password using a combination of 
    letters and numbers. You firstly specify 
    the desired password lengths, however it must be between 4 and 10 
    characters long. If you provide an invalid input it will raise a value error.

    Example:
        >>> password_generator(8)
        "MuKunas7"

    Args:
        length (int): The desired length of the password. 
                      Must be an integer between 4 and 10.

    Returns:
        str: A randomly generated password of the specified length.

    Raises:
        ValueError: If `length` is not an integer or is outside the 
                    range of 4 to 10.

    """
    pass
