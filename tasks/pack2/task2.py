def is_palindrome(text):
    return text == text[::-1]


def f(text):
    for length in range(len(text), 1, -1):
        for i in range(0, len(text) - length + 1):
            if is_palindrome(text[i:i + length]):
                return text[i:i + length]


print(f('babad'))
