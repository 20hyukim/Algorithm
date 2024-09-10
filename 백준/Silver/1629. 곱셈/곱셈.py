from collections import defaultdict
import sys


def remainder(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = remainder(a, b//2, c)
        return (half * half) % c
    else:
        return (a * remainder(a, b-1, c)) % c



if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())
    print(remainder(a, b, c))
