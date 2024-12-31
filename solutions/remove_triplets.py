def remove_triplets(text: str):
    if text == "":
        return ""

    prev = text[0]
    frequency = 1

    ans = text[0]

    for i in range(1, len(text)):
        if text[i] == prev:
            frequency += 1
        else:
            prev = text[i]
            frequency = 1
        if frequency < 3:
            ans += text[i]

    return ans


print(remove_triplets("aaabbb"))
