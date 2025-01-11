def valid_anagram(str1: str, str2: str) -> bool:
    
    assert isinstance(str1, str), "First argument must be a string"
    assert isinstance(str2, str), "Second argument must be a string"

    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]

    return len(char_count) == 0
