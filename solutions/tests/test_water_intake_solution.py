import unittest
from solutions.water_intake_solution import calculate_water_intake


class TestWaterIntakeCalculator(unittest.TestCase):
    """To test the calculate_water_intake function."""

    def test_low_activity_temperate(self):
        """Test for low activity in temperate climate."""
        self.assertEqual(
            calculate_water_intake(70, 30),
            "Recommended daily water intake: 2.67 liters",
        )

    def test_moderate_activity_hot(self):
        """Test for moderate activity in hot climate."""
        self.assertEqual(
            calculate_water_intake(50, 60),
            "Recommended daily water intake: 2.37 liters",
        )

    def test_invalid_weight(self):
        """Test for invalid weight input."""
        self.assertEqual(
            calculate_water_intake(-70, 30),
            "Invalid input. Weight and activity minutes must be greater than zero.",
        )
