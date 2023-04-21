import itertools


def compare(word1, word2):
    for i in range(len(word1)):
        if word1[i] < word2[i]:
            return False

    return True


def f(s1: str, s2: str):
    for word1 in itertools.permutations(s1, len(s1)):
        for word2 in itertools.permutations(s2, len(s2)):
            if compare(word1, word2) or compare(word2, word1):
                return True

    return False


print(f('abc', 'xya'))
print(f('abe', 'acd'))
