x, y, z = map(int, input().split())

dict_r = {}


def f(a, b, c):
    if (a, b, c) in dict_r:
        return dict_r[(a, b, c)]
    elif a <= 0 or b <= 0 or c <= 0:
        dict_r[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dict_r[(a, b, c)] = f(20, 20, 20)
    elif a < b < c:
        dict_r[(a, b, c)] = f(a, b, c - 1) + f(a, b - 1, c - 1) - f(a, b - 1, c)
    else:
        dict_r[(a, b, c)] = f(a - 1, b, c) + f(a - 1, b - 1, c) + f(a - 1, b, c - 1) - f(a - 1, b - 1, c - 1)

    return dict_r[(a, b, c)]


while x != -1 or y != -1 or z != -1:
    print("w({a}, {b}, {c}) = {d}".format(a=x, b=y, c=z, d=f(x, y, z)))
    x, y, z = map(int, input().split())
