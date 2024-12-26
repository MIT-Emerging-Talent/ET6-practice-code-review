"""
This function returns a string in which the first name is swapped with the last name.

parameters:
str: A string of name that we need swap

Output:
str: the swapped input 

Raises:
TypeError: if the input is not a str

Examples:
>>> name_shuffler('')
''

>>> name_shuffler('Mojtaba')
'Mojtaba"

>>> name_shuffler('Fatima Malik')
"Malik Fatima"

"""

def name_shuffler(string: str):

    assert isinstance(string, str), "Input should be a str"
    
    splitStr = string.split(' ')

    reverseStr = splitStr[::-1]
    return ' '.join(reverseStr)


name_shuffler('Mojtaba')