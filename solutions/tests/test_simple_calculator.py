import unittest
from simple_calculator import add, subtract, multiply, divide


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the Simple Calculator functions."""

    def test_add(self):
        """Test addition of two numbers."""
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        """Test subtraction of two numbers."""
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        """Test multiplication of two numbers."""
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        """Test division of two numbers."""
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        """Test division by zero."""
        self.assertEqual(divide(10, 0), "Error! Division by zero.")
