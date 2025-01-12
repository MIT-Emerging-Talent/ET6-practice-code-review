#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the volts_to_amperes function.

Test categories:
    - Standard cases: Positive numbers and zero for voltage and resistance.
    - Edge cases: Negative voltage values.
    - Defensive tests: Non-numeric inputs and invalid resistance (zero/negative).
"""

import unittest
from ..volts_to_amperes import volts_to_amperes


class TestVoltsToAmperes(unittest.TestCase):
    """Test suite for the volts_to_amperes function.

    This test suite ensures that the volts_to_amperes function behaves correctly for a variety
    of input values, including positive, negative, and zero values for both voltage and
    resistance, as well as checks for invalid inputs.
    """

    # Standard test cases
    def test_positive_voltage(self):
        """Test case for a positive voltage and valid resistance.

        This test verifies that the function returns the correct amperes when a positive
        voltage and valid resistance are provided.
        """
        self.assertEqual(volts_to_amperes(10, 2), 5.0)

    def test_large_positive_voltage(self):
        """Test case for a large positive voltage.

        This test verifies that the function returns the correct amperes for a larger
        positive voltage.
        """
        self.assertEqual(volts_to_amperes(100, 2), 50.0)

    def test_zero_voltage(self):
        """Test case for zero voltage.

        This test verifies that the function correctly returns 0 amperes when the voltage
        is zero.
        """
        self.assertEqual(volts_to_amperes(0, 10), 0.0)

    # Edge cases
    def test_negative_voltage(self):
        """Test case for a negative voltage value.

        This test verifies that the function handles negative voltage inputs correctly.
        """
        self.assertEqual(volts_to_amperes(-10, 2), -5.0)

    # Defensive tests
    def test_non_numeric_voltage(self):
        """Test case for a non-numeric voltage input.

        This test ensures that the function raises a ValueError when the voltage is a
        non-numeric value.
        """
        with self.assertRaises(ValueError):
            volts_to_amperes("10", 2)

    def test_zero_resistance(self):
        """Test case for zero resistance value.

        This test ensures that the function raises a ValueError when the resistance is
        zero, as dividing by zero is not allowed in this context.
        """
        with self.assertRaises(ValueError):
            volts_to_amperes(10, 0)

    def test_negative_resistance(self):
        """Test case for negative resistance value.

        This test ensures that the function raises a ValueError when the resistance is
        negative, as negative resistance is not valid in this context.
        """
        with self.assertRaises(ValueError):
            volts_to_amperes(10, -2)


if __name__ == "__main__":
    unittest.main()
