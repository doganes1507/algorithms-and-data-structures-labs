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


def tournament_sort(arr):
    n = len(arr)
    tree_size = 2 * n - 1
    tree = [None] * tree_size

    for i in range(n):
        tree[tree_size - n + i] = arr[i]

    for i in range(tree_size - n, -1, -1):
        left = tree[2 * i - 1]
        right = tree[2 * i - 2]
        if left is not None and right is not None:
            tree[i] = max(left, right)
        elif left is not None:
            tree[i] = left
        elif right is not None:
            tree[i] = right

    sorted_arr = []
    for i in range(n):
        winner = tree[0]
        sorted_arr.append(winner)

        j = tree.index(winner)
        tree[j] = None
        while j > 0:
            parent = (j - 1) // 2
            sibling = j + 1 if j % 2 == 0 else j - 1
            if tree[sibling] is not None:
                loser = tree[sibling]
            else:
                loser = tree[parent]
            tree[parent] = max(tree[parent], loser)
            j = parent

    return sorted_arr
