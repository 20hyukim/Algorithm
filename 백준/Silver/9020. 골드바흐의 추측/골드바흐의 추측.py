import math


def find_decimal(arr):
    for a in arr:
        if a == 1:
            return False

        for i in range(2, int(math.sqrt(a))+1, 1):
            if a % i == 0:
                return False
    return True


def find_possibilities(n):
    possibilities = []
    for i in range(2, int(n/2+1), 1):
        if find_decimal([i, n-i]):
            possibilities.append([n - 2 * i, i, n - i])
    possibilities.sort()
    return possibilities[0][1], possibilities[0][2]


def find_decimals(n):
    for i in range(n):
        a, b = find_possibilities(int(input()))
        print("%d %d" % (a, b))


if __name__ == "__main__":
    find_decimals(int(input()))