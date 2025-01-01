def FooBar_code(n: int):
    assert isinstance(n, int), "N must be integer"
    result = []
    for i in range(1, n + 1):
        if i % 4 == 0 and i % 6 == 0:
            result.append("FooBar")
        elif i % 4 == 0:
            result.append("foo")
        elif i % 6 == 0:
            result.append("Bar")
        else:
            result.append(i)
    return result
