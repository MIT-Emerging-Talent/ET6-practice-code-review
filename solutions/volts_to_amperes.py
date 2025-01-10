#!/usr/bin/env python3
"""
This module contains a function to convert voltage to amperes using Ohm's law.
The formula used is: I = V / R


Created on Fri 10/1/2024
@author: Obay Salih
Group: ET foundations group 16 (Matrix)
Module contents:

Where:
- V is the voltage in volts
- R is the resistance in ohms
- I is the current in amperes

Function:
volts_to_amperes(volts, resistance) -> float

Arguments:
volts (float): The voltage in volts (V)
resistance (float): The resistance in ohms (Ω)

Returns:
float: The current in amperes (A)

Raises:
ValueError: If the resistance is zero or negative, or if the input values are not numeric
"""


def volts_to_amperes(volts: float, resistance: float) -> float:
    """
    Convert voltage (V) to amperes (A) using Ohm's law.

    Parameters:
    volts (float): The voltage in volts.
    resistance (float): The resistance in ohms.

    Returns:
    float: The current in amperes.

    Raises:
    ValueError: If resistance is zero or negative.
    """

    if not isinstance(volts, (int, float)) or not isinstance(resistance, (int, float)):
        raise ValueError("Both voltage and resistance must be numeric values.")

    if resistance <= 0:
        raise ValueError("Resistance must be a positive number.")

    # Ohm's law: I = V / R
    current = volts / resistance
    return current
