def f(text):
    result = set()

    for i in range(len(text) - 1):
        for j in range(i + 1, len(text), 2):
            substring = text[i:j+1]
            if substring[:len(substring) // 2] == substring[len(substring) // 2:]:
                result.add(substring)

    return len(result)


print(f('abcabcabc'))
