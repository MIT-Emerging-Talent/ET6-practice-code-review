import unittest
from solutions.water_solutions import calculate_water_intake


def test_low_activity_temperate():
    """Test for low activity in temperate climate."""
    assert calculate_water_intake(70, "Low", "Temperate") == 2.31


def test_moderate_activity_hot():
    """Test for moderate activity in hot climate."""
    assert calculate_water_intake(70, "Moderate", "Hot") == 3.31


def test_high_activity_cold():
    """Test for high activity in cold climate."""
    assert calculate_water_intake(70, "High", "Cold") == 3.13


def test_invalid_weight():
    """Test for invalid weight input."""
    with unittest.raises(ValueError, match="Weight must be a positive number."):
        calculate_water_intake(-10, "Low", "Temperate")


def test_invalid_activity_level():
    """Test for invalid activity level input."""
    with unittest.raises(ValueError, match="Invalid activity level: InvalidActivity."):
        calculate_water_intake(70, "InvalidActivity", "Cold")


def test_invalid_climate():
    """Test for invalid climate input."""
    with unittest.raises(ValueError, match="Invalid climate: InvalidClimate."):
        calculate_water_intake(70, "Low", "InvalidClimate")
