def minion_game(string):
    # your code goes here
    string = string.lower()
    kevin_score = 0
    stuart_score = 0
    vowels = ['a', 'u','o','i','e']
    kevin_words = {}
    stuart_words = {}
    for letter in string:
        if letter in vowels:
            kevin_words[letter] += 1
            kevin_score += kevin_words[letter]
        else:
            stuart_words[letter] += 1 
            stuart_score += stuart_words[letter]

    return max(kevin_score, stuart_score)

minion_game('BANANA')
