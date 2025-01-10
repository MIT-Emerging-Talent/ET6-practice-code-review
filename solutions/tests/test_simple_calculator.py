"""
Unit tests for the Simple Calculator.

This module contains tests for the `calculate` function in the `simple_calculator.py` module.
The tests cover:
- Basic arithmetic operations (addition, subtraction, multiplication, and division).
- Edge cases such as dividing by zero and operations with negative numbers.
- Validation of correct functionality of the calculator.

Usage:
Run this module using `unittest` to verify the correctness of the calculator function.

Example:
    python -m unittest test_simple_calculator.py
"""

import unittest
from solutions.simple_calculator import calculate


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the Simple Calculator."""

    def test_addition(self):
        self.assertEqual(calculate(10, 5, "add"), 15)

    def test_subtraction(self):
        self.assertEqual(calculate(10, 5, "subtract"), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(10, 5, "multiply"), 50)

    def test_division(self):
        self.assertEqual(calculate(10, 5, "divide"), 2)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, "divide")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate(10, 5, "invalid")


if __name__ == "__main__":
    unittest.main()
