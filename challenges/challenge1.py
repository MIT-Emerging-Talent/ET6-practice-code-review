from challenge1 import reverse_string

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("12345") == "54321"


