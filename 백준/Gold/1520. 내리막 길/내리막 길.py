import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(dp, directions, i, j):
    if (i == n-1 and j == m-1):
        return 1

    if dp[i][j] != -1:
        return dp[i][j]


    ways = 0
    for l, r in directions:
        if 0 <= i+l < n and 0 <= j+r < m and val[i][j] > val[i+l][j+r]:
            ways += dfs(dp, directions, i+l, j+r)

    dp[i][j] = ways
    return dp[i][j]


def get_routes(val, n, m):
    dp = [[-1] * m for _ in range(n)]

    dp[-1][-1] = 1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dfs(dp, directions, 0, 0)

    return dp[0][0]


if __name__ == "__main__":
    n, m = map(int, input().split())
    val = []
    for _ in range(n):
        val.append(list(map(int, input().split())))


    print(get_routes(val, n, m))