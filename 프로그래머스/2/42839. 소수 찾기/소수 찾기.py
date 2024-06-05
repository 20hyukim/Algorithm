import math


def solution(numbers):
    possibility = set()

    def dfs(created, n, l):
        if len(created) == l:
            return

        for i in range(0, len(n), 1):
            possibility.add(int(created + n[i]))
            dfs(created + n[i], n[:i] + n[i + 1:], l)

    def isprime(n):
        if n <= 1:
            return False

        for i in range(2, int(math.sqrt(n))+1, 1):
            if n % i == 0:
                return False

        return True

    def primes(p):
        cnt = 0
        for i in p:
            if isprime(i):
                cnt += 1

        return cnt

    l = len(numbers)
    dfs("", numbers, l)

    # print(possibility)

    return primes(possibility)