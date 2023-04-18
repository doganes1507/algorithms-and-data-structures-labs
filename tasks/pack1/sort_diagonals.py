def sort_diagonals(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        diagonal = []
        r, c = i, 0
        while r < m and c < n:
            diagonal.append(matrix[r][c])
            r += 1
            c += 1
        diagonal.sort()
        r, c = i, 0
        for x in diagonal:
            matrix[r][c] = x
            r += 1
            c += 1

    for j in range(1, n):
        diagonal = []
        r, c = 0, j
        while r < m and c < n:
            diagonal.append(matrix[r][c])
            r += 1
            c += 1
        diagonal.sort()
        r, c = 0, j
        for x in diagonal:
            matrix[r][c] = x
            r += 1
            c += 1

    return matrix


print(sort_diagonals([
    [3, 3, 1, 1],
    [2, 2, 1, 2],
    [1, 1, 1, 2]
]
))
