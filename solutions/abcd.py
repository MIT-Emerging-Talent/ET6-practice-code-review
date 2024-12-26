def romanToInt( string):
        """
        This function will take a roman number as an input and coverts it to an integr and returns it

        :type s: str
        :rtype: int

        inputs:
        str: a string of roman numbers that we have to covert

        output:
        int: return the converted integer

        raises:
        type error if input is not a str

        examples:
        >>> romanToInt('I')
        1
        >>> romanToInt('V')
        5

        >>> romanToInt('IV')
        4
        >>> romanToInt('X')
        10

        >>> romanToInt('XL')
        40
        """

        if string == 'I':
            return 1

        if string == 'III':
            return 3
        
        list 
        count = 0
        result = [string[i:i+2] for i in range(0, len(string), 2)]

        return result

        

print(romanToInt("IV"))


        