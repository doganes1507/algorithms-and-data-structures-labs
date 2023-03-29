def bubble_sort(array: list):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def selection_sort(array: list):
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[min_index], array[i] = array[i], array[min_index]


def insertion_sort(array: list):
    for i in range(1, len(array)):
        x = array[i]
        j = i - 1

        while j >= 0 and x < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = x


def shell_sort(array: list):
    interval = len(array) // 2

    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp

        interval //= 2


def quick_sort(array: list):
    if len(array) > 1:
        pivot = array[0]
        left, right = [], []

        for i in range(1, len(array)):
            if array[i] < pivot:
                left.append(array[i])
            else:
                right.append(array[i])

        quick_sort(left)
        quick_sort(right)
        array.clear()
        array += left + [pivot] + right
