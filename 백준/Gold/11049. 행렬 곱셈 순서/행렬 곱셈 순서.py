import sys


def get_min_val(x, y, row, column):
    if y-x <= 0:
        return 0

    if dp[x][y] != -1:
        return dp[x][y]

    min_val = sys.maxsize

    for k in range(x, y):
        min_val = min(min_val, row[x]*column[k]*column[y] + get_min_val(x, k, row, column) + get_min_val(k+1, y, row, column))

    dp[x][y] = min_val
    return dp[x][y]


if __name__ == "__main__":
    n = int(input())
    r = []
    c = []
    for _ in range(n):
        row, column = map(int, input().split())
        r.append(row)
        c.append(column)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    print(get_min_val(0, n-1, r, c))