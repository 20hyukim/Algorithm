
def coin_case(n, k, coins):
    dp = [0] * (k+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, k+1, 1):
            if i >= coin:
                dp[i] += dp[i-coin]

    return dp[k]


if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    coins.sort(reverse=True)
    print(coin_case(n, k, coins))