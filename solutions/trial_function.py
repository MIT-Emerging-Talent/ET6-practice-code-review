def factorial_calc(number: int) -> int:
    assert isinstance(number, int)
    assert number >= 0

    factorial = 1
    for x in range(1, number + 1):
        factorial = x * factorial

    return factorial


print(factorial_calc(5))
