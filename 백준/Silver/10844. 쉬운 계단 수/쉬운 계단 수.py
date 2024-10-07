
def get_stair_num(n):
    dp = [[1] * 10 for _ in range(101)]

    dp[1][0] = 0

    for n in range(2, n+1, 1):
        for i in range(0, 10, 1):
            dp[n][i] = 0
            if 0 <= i-1 < 10:
                dp[n][i] += (dp[n-1][i-1]) % 1000000000
            if 0 <= i+1 < 10:
                dp[n][i] += (dp[n-1][i+1]) % 1000000000

    #print(dp)
    return sum(dp[n]) % 1000000000


if __name__ == "__main__":
    n = int(input())
    print(get_stair_num(n))

