from functools import cmp_to_key


def special_comparator(a, b):
    return 1 if int(str(a) + str(b)) < int(str(b) + str(a)) else -1


def max_number(numbers: list):
    return ''.join(str(elem) for elem in sorted(numbers, key=cmp_to_key(special_comparator)))


print(max_number([10, 2]))
print(max_number([3, 30, 34, 5, 9]))
print(max_number([1]))
print(max_number([10]))
