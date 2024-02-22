import math


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def possible_location(d, r1, r2):
    if d == 0:
        if r1 != r2:
            return 0
        return -1

    elif d >= r1 + r2:
        if r1 + r2 == d:
            return 1
        return 0

    elif abs(r1 - r2) >= d:
        if abs(r1 - r2) > d:
            return 0
        return 1
    return 2



for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = calculate_distance(x1, y1, x2, y2)

    print(possible_location(d, r1, r2))