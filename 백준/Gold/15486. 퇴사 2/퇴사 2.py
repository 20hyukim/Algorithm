def get_max_profit(n, dp):
    profit = [0] * (n+1)
    if dp[n-1][0] == 1:
        profit[n-1] = dp[n-1][1]
    for i in range(n-2, -1, -1):
        if i + dp[i][0] > n:
            profit[i] = profit[i+1]
            continue
        if profit[dp[i][0] + i] + dp[i][1] > profit[i+1]:
            profit[i] = profit[dp[i][0] + i] + dp[i][1]
            continue
        profit[i] = profit[i+1]

    #print(profit)
    return profit[0]


if __name__ == "__main__":
    n = int(input())
    dp = []

    for _ in range(n):
        tp = list(map(int, input().split()))
        dp.append(tp)

    print(get_max_profit(n, dp))