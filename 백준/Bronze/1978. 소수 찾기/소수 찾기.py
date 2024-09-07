import math


def find_decimal(n):
    if n == 1:
        return 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0

    return 1


def find_decimals(n):
    total_decimal = 0
    arr = map(int, input().split())
    for a in arr:
        total_decimal += find_decimal(a)

    return total_decimal


if __name__ == "__main__":
    print(find_decimals(int(input())))