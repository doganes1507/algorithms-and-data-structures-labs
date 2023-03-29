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
    tree = [None] * (2 * n - 1)

    def build_tree(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build_tree(2 * node + 1, start, mid)
            build_tree(2 * node + 2, mid + 1, end)
            tree[node] = max(tree[2 * node + 1], tree[2 * node + 2])

    def query_tree(node, start, end, left, right):
        if left > end or right < start:
            return -float('inf')
        if left <= start and right >= end:
            return tree[node]
        mid = (start + end) // 2
        return max(query_tree(2 * node + 1, start, mid, left, right),
                   query_tree(2 * node + 2, mid + 1, end, left, right))

    def find_winner(l, r):
        return l if arr[l] < arr[r] else r

    def tournament(start, end):
        if start == end:
            return start
        mid = (start + end) // 2
        left = tournament(start, mid)
        right = tournament(mid + 1, end)
        return find_winner(left, right)
    build_tree(0, 0, n - 1)
    sorted_arr = []
    for i in range(n):
        winner_index = tournament(0, n - 1 - i)
        sorted_arr.append(arr[winner_index])
        arr.pop(winner_index)
    return sorted_arr
