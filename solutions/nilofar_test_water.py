import pytest
from nilofar_water_intake import calculate_water_intake

def test_low_activity_temperate():
    assert calculate_water_intake(70, "Low", "Temperate") == 2.31

def test_moderate_activity_hot():
    assert calculate_water_intake(70, "Moderate", "Hot") == 3.31

def test_high_activity_cold():
    assert calculate_water_intake(70, "High", "Cold") == 3.13

def test_invalid_activity():
    with pytest.raises(ValueError):
        calculate_water_intake(70, "Extreme", "Temperate")

def test_invalid_weight():
    with pytest.raises(ValueError):
        calculate_water_intake(-10, "Low", "Temperate")
