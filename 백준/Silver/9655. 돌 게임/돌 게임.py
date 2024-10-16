
def get_winner(n, name):
    if n > x:
        return
    if dp[n][name] > 0:
        return

    dp[n][name] += 1

    if name == 0:
        get_winner(n+1, 1)
        get_winner(n+3, 1)
    else:
        get_winner(n+1, 0)
        get_winner(n+3, 0)


if __name__ == "__main__":
    x = int(input())
    dp = [[0, 0] for _ in range(x+1)]
    get_winner(1, 0)
    get_winner(3, 0)

    #print(dp)
    if dp[x][0] > 0:
        print("SK")
    else:
        print("CY")