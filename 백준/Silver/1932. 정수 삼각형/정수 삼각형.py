dict_t = {}


def f(a, b):
    if (a, b) in dict_t:
        return dict_t[(a, b)]
    if a == height - 1:
        return triangle[a][b]
    dict_t[(a, b)] = triangle[a][b] + max(f(a + 1, b), f(a + 1, b + 1))
    return dict_t[(a, b)]


height = int(input())
triangle = []
for i in range(height):
    sub_triangle = [int(n) for n in input().split()]
    triangle.append(sub_triangle)

print(f(0, 0))
