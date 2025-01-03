"""
Test module for the prime_checker function.add()

Created on: 04/01/2025
@author: Thilakan Jegatheeswaran
"""


# Define the is_prime function
def is_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False  # n is divisible by i, so it's not prime
    return True  # n is prime if no divisors were found


# Test cases for the is_prime function
def test_is_prime():
    # List to store the results
    results = []

    # Test cases with expected outputs
    results.append(("n=7", is_prime(7) == True))  # 7 is prime
    results.append(("n=4", is_prime(4) == False))  # 4 is not prime
    results.append(("n=17", is_prime(17) == True))  # 17 is prime
    results.append(("n=20", is_prime(20) == False))  # 20 is not prime

    # Edge cases
    results.append(("n=0", is_prime(0) == False))  # 0 is not prime
    results.append(("n=1", is_prime(1) == False))  # 1 is not prime
    results.append(("n=-5", is_prime(-5) == False))  # Negative numbers are not prime

    # Test case for a large prime number
    results.append(("n=104729", is_prime(104729) == True))  # 104729 is prime

    return results


# Run the test cases and capture results
test_results = test_is_prime()

# Display the results
for test, result in test_results:
    print(f"Test for {test}: {'Passed' if result else 'Failed'}")
