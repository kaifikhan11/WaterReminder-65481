import pytest
from water_reminder import calculate_water_intake

def test_valid_input_youth():
    result = calculate_water_intake(60, 16)
    assert "1.98" in result
    assert "Every 3 hours" in result

def test_valid_input_adult():
    result = calculate_water_intake(70, 30)
    assert "2.31" in result
    assert "Every 2 hours" in result

def test_valid_input_elder():
    result = calculate_water_intake(55, 65)
    assert "1.82" in result
    assert "Every 1.5 hours" in result

def test_invalid_weight_string():
    result = calculate_water_intake("abc", 25)
    assert "Invalid input" in result

def test_invalid_negative_age():
    result = calculate_water_intake(60, -5)
    assert "Invalid input" in result
