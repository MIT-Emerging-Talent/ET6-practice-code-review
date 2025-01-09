""""
## Challenge Overview
Identify all prime numbers up to a given integer \( N \). A prime number is greater than 1 and only divisible by 1 and itself.

 Steps to Solve
1. Understand Prime Numbers:
   - Prime numbers: 2, 3, 5, 7, 11, etc.

2. Input:
   - Single integer \( N \), e.g., \( N = 20 \).

3. **Output**:
   - List of primes up to \( N \), e.g., [2, 3, 5, 7, 11, 13, 17, 19].


----------------------------------------------------------------------------------------------------------------------------------------
""""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_up_to_n(n):
    """Find all prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
N = 20
print("Prime numbers up to", N, ":", find_primes_up_to_n(N))
