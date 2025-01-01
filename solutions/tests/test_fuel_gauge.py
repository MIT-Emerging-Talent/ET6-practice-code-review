import unittest

from ..fuel_gauge import fuel_gauge


class TestFuelGauge(unittest.TestCase):
    """Test cases for the fuel_gauge function."""

    def test_full(self):
        """Test cases where the percentage is 99% or more."""
        self.assertEqual(fuel_gauge(99, 100), "F")
        self.assertEqual(fuel_gauge(100, 100), "F")

    def test_empty(self):
        """Test cases where the percentage is 1% or less."""
        self.assertEqual(fuel_gauge(1, 100), "E")
        self.assertEqual(
            fuel_gauge(
                0,
                100,
            ),
            "E",
        )

    def test_percentage(self):
        """Test cases where the result is a percentage."""
        self.assertEqual(fuel_gauge(50, 100), 50)
        self.assertEqual(fuel_gauge(25, 50), 50)

    def test_invalid_input(self):
        """Test cases for invalid inputs."""
        with self.assertRaises(ValueError):
            fuel_gauge(3, 0)
        with self.assertRaises(ValueError):
            fuel_gauge(4, 3)
        with self.assertRaises(ValueError):
            fuel_gauge("abc", "def")
