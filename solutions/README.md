# Find All Prime Numbers Up to N

## Challenge Overview
Identify all prime numbers up to a given integer \( N \). A prime number is greater than 1 and only divisible by 1 and itself.

### Steps to Solve
1. **Understand Prime Numbers**:
   - Prime numbers: 2, 3, 5, 7, 11, etc.

2. **Input**:
   - Single integer \( N \), e.g., \( N = 20 \).

3. **Output**:
   - List of primes up to \( N \), e.g., [2, 3, 5, 7, 11, 13, 17, 19].

### Implementation
1. **Iterate Through Numbers**:
   - Loop from 2 to \( N \).

2. **Check if Each Number is Prime**:
   - Function to check if a number is prime:
     - Return False if < 2.
     - Check divisibility from 2 to sqrt(number).
     - Return True if no divisors found.

3. **Collect Prime Numbers**:
   - Use the function to collect primes up to \( N \).


