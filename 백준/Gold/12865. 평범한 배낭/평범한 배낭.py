def ks(w, weights, prices, n):

    if w == 0 or n == 0:
        return 0

    elif weights[n-1] > w:
        return ks(w, weights, prices, n-1)

    return max(ks(w - weights[n-1], weights, prices, n-1) + prices[n-1], ks(w, weights, prices, n-1))

def ks1(max_w, weights, prices, n):

    dp = [[0 for _ in range(max_w+1)] for _ in range(n+1)]

    for i in range(n+1):
        for w in range(max_w + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + prices[i-1])

    return dp[n][max_w]


if __name__ == "__main__":
    weights = []
    prices = []
    n, max_w = map(int, input().split())
    for _ in range(n):
        w, p = map(int, input().split())
        weights.append(w)
        prices.append(p)

    print(ks1(max_w, weights, prices, n))


