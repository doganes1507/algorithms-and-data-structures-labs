def is_triangle_exist(a, b, c):
    return a + b > c and b + c > a and c + a > b


def max_triangle_perimeter(sides: list):
    results = [0]

    for i in range(0, len(sides) - 2):
        for j in range(i + 1, len(sides) - 1):
            for k in range(j + 1, len(sides)):
                if is_triangle_exist(sides[i], sides[j], sides[k]):
                    results.append(sides[i] + sides[j] + sides[k])

    return max(results)


print(max_triangle_perimeter([2, 1, 2]))
print(max_triangle_perimeter([1, 2, 1]))
print(max_triangle_perimeter([3, 2, 3, 4]))
print(max_triangle_perimeter([3, 6, 2, 3]))
