import sys


def dfs(n):
    if dp[n] != 0:
        return dp[n]
    ans = [sys.maxsize] * 3

    if n % 3 == 0:
        ans[0] = 1 + dfs(n//3)
    if n % 2 == 0:
        ans[1] = 1 + dfs(n//2)
    ans[2] = 1 + dfs(n-1)

    dp[n] = min(ans)
    return dp[n]


if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+3)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for i in range(4, n+1):
        dfs(i)

    #print(dp)
    print(dp[n])