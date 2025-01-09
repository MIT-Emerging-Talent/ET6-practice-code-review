# Count the Prime Numbers in a List

Challenge Overview:

The goal of this challenge is to count how many prime numbers are present in a given list of integers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

### Steps to Solve
1. Understand Prime Numbers:
   - Prime numbers: 2, 3, 5, 7, 11, etc.

2. Input:
   - List of integers, e.g., [2, 3, 4, 5, 6, 7, 8, 9, 10].

3. Output:
   - Count of primes in the list, e.g., 4 for the above list.

### Implementation
1. Iterate through the List:
   - Loop through each number.

2. Check if Each Number is Prime:
   - Function to check if a number is prime:
     - Return False if < 2.
     - Check divisibility from 2 to sqrt(number).
     - Return True if no divisors found.

3. Count the Primes:
   - Use the function to count primes in the list.

  Created on: 09/01/25
@author: Zeinab Shadabshoar

