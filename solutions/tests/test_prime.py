"""This module runs the test for prime_checker."""


def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def test_is_prime():
    # Test cases with assertions
    assert is_prime(7) == True, "Test failed for n=7"
    assert is_prime(4) == False, "Test failed for n=4"
    assert is_prime(17) == True, "Test failed for n=17"
    assert is_prime(20) == False, "Test failed for n=20"

    # Add more tests if necessary
    print("All tests passed!")  # This is for confirmation only


# Run the test cases
test_is_prime()
