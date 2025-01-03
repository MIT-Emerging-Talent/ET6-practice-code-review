

def most_frequent_character(input_string: str) -> str:
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the character with the maximum frequency
    max_char = max(char_count, key=lambda char: (char_count[char], -input_string.index(char)))

    return max_char
print(most_frequent_character("asdfghjkl"))
