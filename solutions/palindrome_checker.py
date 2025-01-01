def palindrome_checker(text: str) -> bool:

    assert isinstance(text, str), "Text must be a string."


    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    

    return cleaned_text == cleaned_text[::-1]
