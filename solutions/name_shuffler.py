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
    
    assert isinstance(string, str) and string.strip(), "Input must be a non-empty string"
    
    split_str = string.split(' ')
    
    reverse_str = split_str[::-1]
    
    return ' '.join(reverse_str)

name_shuffler('Mojtaba')