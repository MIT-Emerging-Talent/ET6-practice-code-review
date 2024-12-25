""" sum numbers 
sum numbers is a recursive function return the sum of count down numbers 

created: 25/12/2024
Team number:28
Team name:MIT Alpha
The author: Maab Mohamedkhair"""


def sum_numbers(n):
    
    """ sum numbers 
sum numbers is a recursive function return the sum of count down numbers 
from n -> 1

Base case: n == 1 
    return 1

recursion case: for n > 1
    smaller_result of n + the value of sum_numbers(n - 1)

parameters: n = any positive integer less than 1000 because python limitation in recursion 

return : the sum of all numbers less than n inclusive and greater than or equal one

Examples:

>>> sum_numbers(4)
10

>>> sum_numbers(5)
15

>>> sum_numbers(0)
Traceback (most recent call last):
...
Exception: Input must be greater than 0
"""


    #checks n is less than 1000
    if (n>1000):
        raise RecursionError
    assert isinstance(n, int), "input must be integer"
    
    #checks if the value is greater than Zero
    if n<=0:
        raise Exception("Input must be greater than 0")
    
    
    # Base Case
    #the function smallest version
    if n == 1:
        return 1
    
    # Recursive Case  |  breakdown to smaller problem and turn around
    smaller_result = n+ sum_numbers(n - 1)
    
    # Recursive Build up all the parts from the stack
    return smaller_result
    
