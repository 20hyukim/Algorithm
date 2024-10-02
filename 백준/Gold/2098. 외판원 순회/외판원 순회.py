import sys


def get_min(i, mask):

    if mask == ((1 << i) | 3):
        return dist[1][i]

    if memo[i][mask] != -1:
        return memo[i][mask]

    res = sys.maxsize
    for j in range(1, n+1, 1):
        if j != i and j != 1 and (mask & (1 << j)) != 0 and dist[j][i] != sys.maxsize:
            res = min(res, get_min(j, (mask & (~(1 << i)))) + dist[j][i])

    memo[i][mask] = res
    return res


if __name__ == "__main__":
    n = int(input())
    memo = [[-1] * (1 << (n+1)) for _ in range(n+1)]

    dist = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        d = list(map(int, input().split()))
        for j in range(1, n+1):
            dist[i][j] = d[j-1] if d[j-1] != 0 else sys.maxsize

    min_cost = sys.maxsize
    for i in range(2, n+1, 1):
        min_cost = min(min_cost, get_min(i, (1 << (n+1))- 1) + dist[i][1])

    print(min_cost)