"""
Unit Tests for the `calculate` function in the `python_calculator` module.
"""

import unittest
from solutions.python_calculator import calculate


class TestPythonCalculator(unittest.TestCase):
    """
    Unit tests for the `calculate` function.
    """

    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(calculate(10, 4, "-"), 6)

    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(calculate(6, 3, "*"), 18)

    def test_division(self):
        """Test division operation."""
        self.assertEqual(calculate(9, 3, "/"), 3.0)

    def test_division_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, "/")

    def test_invalid_operator(self):
        """Test invalid operator raises ValueError."""
        with self.assertRaises(ValueError):
            calculate(10, 5, "%")

    def test_invalid_operand_type(self):
        """Test invalid operand types raise TypeError."""
        with self.assertRaises(TypeError):
            calculate("10", 5, "+")
        with self.assertRaises(TypeError):
            calculate(10, "5", "+")

    def test_boundary_cases(self):
        """Test boundary cases (e.g., very large or small numbers)."""
        self.assertAlmostEqual(calculate(1e308, 1e308, "+"), float("inf"))
        self.assertEqual(calculate(0, 0, "+"), 0)
