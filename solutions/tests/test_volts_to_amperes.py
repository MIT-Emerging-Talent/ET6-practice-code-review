import unittest
from volts_to_amperes import volts_to_amperes


class TestVoltsToAmperes(unittest.TestCase):
    """Test suite for the volts_to_amperes function."""

    def test_positive_number(self):
        """It should return the correct amperes for a positive number of volts."""
        self.assertEqual(volts_to_amperes(10, 2), 5.0)

    def test_large_positive_number(self):
        """It should return the correct amperes for a large number of volts."""
        self.assertEqual(volts_to_amperes(100, 2), 50.0)

    def test_zero(self):
        """It should return 0 for zero volts."""
        self.assertEqual(volts_to_amperes(0, 10), 0.0)

    def test_negative_number(self):
        """It should return the correct amperes for negative voltage."""
        self.assertEqual(volts_to_amperes(-10, 2), -5.0)

    def test_non_numeric_input(self):
        """It should raise an error for non-numeric input."""
        with self.assertRaises(ValueError):
            volts_to_amperes("10", 2)

    def test_zero_resistance(self):
        """It should raise an error if resistance is zero."""
        with self.assertRaises(ValueError):
            volts_to_amperes(10, 0)

    def test_negative_resistance(self):
        """It should raise an error if resistance is negative."""
        with self.assertRaises(ValueError):
            volts_to_amperes(10, -2)


if __name__ == "__main__":
    unittest.main()
