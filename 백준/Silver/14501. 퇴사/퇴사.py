
def get_max_profit(counsle, n):
    dp = [0] * (n+1)

    for i in range(n-1, -1, -1):
        if i + counsle[i][0] > n:
            dp[i] = dp[i+1]
            continue
        if dp[i + counsle[i][0]] + counsle[i][1] > dp[i+1]:
            dp[i] = dp[i + counsle[i][0]] + counsle[i][1]
        else:
            dp[i] = dp[i+1]
    return dp[0]


if __name__ == "__main__":
    n = int(input())
    counsle = [[0, 0] for _ in range(n)]

    for i in range(n):
        t, p = map(int, input().split())
        counsle[i][0] = t
        counsle[i][1] = p

    print(get_max_profit(counsle, n))
