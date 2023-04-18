def special_comparator(a, b):
    return int(a + b) < int(b + a)


def max_number(numbers: list):
    array = numbers.copy()

    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i

            while j >= interval and special_comparator(str(array[j - interval]), str(temp)):
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp

        interval //= 2

    return ''.join(str(elem) for elem in array)


print(max_number([10, 2]))
print(max_number([3, 30, 34, 5, 9]))
print(max_number([1]))
print(max_number([10]))
