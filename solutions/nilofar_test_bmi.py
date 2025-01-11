import unittest
from nilfersolution import calculate_bmi  # Import the function from the solution file

class TestBMICalculator(unittest.TestCase):
    def test_underweight(self):
        self.assertEqual(calculate_bmi(45, 1.7), "Underweight (BMI: 15.57)")

    def test_normal_weight(self):
        self.assertEqual(calculate_bmi(68, 1.75), "Normal weight (BMI: 22.20)")

    def test_overweight(self):
        self.assertEqual(calculate_bmi(80, 1.7), "Overweight (BMI: 27.68)")

    def test_obesity(self):
        self.assertEqual(calculate_bmi(95, 1.6), "Obesity (BMI: 37.11)")

    def test_invalid_input(self):
        self.assertEqual(calculate_bmi(-45, 1.7), "Invalid input. Height and weight must be greater than zero.")
        self.assertEqual(calculate_bmi(50, 0), "Invalid input. Height and weight must be greater than zero.")
