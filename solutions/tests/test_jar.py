import pytest
from solutions.jar import Jar


def test_initialization():
    """Test that the jar is initialized with the correct capacity and zero cookies."""
    jar = Jar(10)
    assert jar.capacity == 10  # Ensure capacity is set correctly
    assert jar.size == 0  # Ensure size starts at zero


def test_deposit():
    """Test depositing cookies into the jar."""
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5  # Ensure size is updated correctly after deposit
    jar.deposit(3)
    assert jar.size == 8  # Ensure size is updated correctly after another deposit


def test_capacity_exceeded():
    """Test that depositing more cookies than the jar's capacity raises a ValueError."""
    jar = Jar(3)
    with pytest.raises(ValueError):
        jar.deposit(4)  # Should raise ValueError as the capacity is exceeded


def test_withdraw():
    """Test withdrawing cookies from the jar."""
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3  # Ensure size is updated correctly after withdrawal


def test_not_enough_cookies():
    """Test that withdrawing more cookies than available raises a ValueError."""
    jar = Jar(2)
    jar.deposit(1)
    with pytest.raises(ValueError):
        jar.withdraw(3)  # Should raise ValueError as not enough cookies are available


def test_str_representation():
    """Test that the string representation of the jar is correct."""
    jar = Jar(5)
    jar.deposit(3)
    assert (
        str(jar) == "🍪🍪🍪"
    )  # Ensure the string output correctly shows the number of cookies


def test_invalid_capacity():
    """Test that initializing the jar with a negative capacity raises a ValueError."""
    with pytest.raises(ValueError):
        Jar(-2)  # Should raise ValueError as the capacity is negative
