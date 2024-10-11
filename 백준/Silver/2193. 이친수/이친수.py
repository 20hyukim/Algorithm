def get_nums(n, dp):
    dp[1] = [0, 1]
    dp[2] = [1, 0]

    for i in range(3, n+1, 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

    #print(dp)
    return sum(dp[n])


if __name__ == "__main__":
    n = int(input())
    dp = [[0,0] for _ in range(92)]
    print(get_nums(n, dp))