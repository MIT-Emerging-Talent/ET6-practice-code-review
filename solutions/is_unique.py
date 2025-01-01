def is_unique(s: str) -> bool:
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return len(set(s)) == len(s)


print(is_unique("3ss!20"))
