"""
Created on 08/01/2025
@author: Arwa Mohamed


 A function to convert weights from kilograms (kg) to pounds (lbs).

The kg_to_lbs function accepts a weight in kilograms and returns the equivalent weight in pounds.
It raises a ValueError for invalid inputs like negative numbers.

"""

import unittest


def kg_to_lbs(kg):
    """Converts a given weight from kilograms (kg) to pounds (lbs).

    Parameters:
        kg (float): Weight in kilograms.

    Returns:
        float: Equivalent weight in pounds.

    Examples:
        >>> kg_to_lbs(75)
        165.3465

        >>> kg_to_lbs(34)
        74.95708

        >>> kg_to_lbs(10)
        22.0462

    Raises:
        ValueError: If the input is not a positive number.
    """
    if kg < 0:
        raise ValueError("Weight cannot be negative.")
    return kg * 2.20462


class TestKgToLbs(unittest.TestCase):
    """Unit tests for the kg_to_lbs function.

    The tests verify the following:
    - Correct conversion of positive weights.
    - Conversion of zero to zero pounds.
    - Handling of negative input values by raising a ValueError.
    - Accuracy of conversion for large values.
    """

    def test_positive_conversion(self):
        """Test conversion for positive weights."""
        self.assertAlmostEqual(kg_to_lbs(1), 2.20462, places=5)
        self.assertAlmostEqual(kg_to_lbs(5), 11.0231, places=4)

    def test_zero_conversion(self):
        """Test conversion for zero weight."""
        self.assertEqual(kg_to_lbs(0), 0)

    def test_negative_input(self):
        """Test handling of negative weights."""
        with self.assertRaises(ValueError):
            kg_to_lbs(-1)

    def test_large_value(self):
        """Test conversion for large values."""
        self.assertAlmostEqual(kg_to_lbs(1000), 2204.62, places=2)


if _name_ == "_main_":
    unittest.main()
