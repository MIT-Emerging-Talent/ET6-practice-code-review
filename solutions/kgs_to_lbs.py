""" "
Created on 0084/01/2025
@author: Arwa Mohamed

"""


def kg_to_lbs(kg):
    """Converts a given weight from kilograms (kg) to pounds (lbs).

    Parameters:
        kg (float): Weight in kilograms.

    Returns:
        float: Equivalent weight in pounds.

    >>> kg_to_lbs(75):
    165.347

    >>> kg_to_lbs(34):
    74.957

    >>> kg_to_lbs(10):
    22.046

    Raises:
        ValueError: If the input is not a positive number.
    """
    if kg < 0:
        raise ValueError("Weight cannot be negative.")
    return kg * 2.20462
