def min_coin(money, coins):
    cnt_all = 0
    for c in coins:
        if money == 0:
            return cnt_all
        cnt = money // c
        cnt_all += cnt
        money -= cnt * c

    return cnt_all


if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    coins.sort(reverse=True)
    print(min_coin(k, coins))