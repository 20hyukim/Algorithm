def lcs(word1, word2, m, n, save):
    if m == 0 or n == 0:
        return 0

    if save[n][m] != -1:
        return save[n][m]

    elif word1[m - 1] == word2[n - 1]:
        save[n][m] = lcs(word1, word2, m - 1, n - 1, save) + 1

    else:
        save[n][m] = max(lcs(word1, word2, m - 1, n, save), lcs(word1, word2, m, n - 1, save))

    return save[n][m]


def lcs2(word1, word2, n, m, dp):
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            elif word1[j - 1] == word2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    word1 = input()
    word2 = input()
    n = len(word1)
    m = len(word2)

    save = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    print(lcs2(word1, word2, n, m, save))
