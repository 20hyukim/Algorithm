def jump_game(n, arr):
    # DP 테이블 초기화: dp[i][j]는 (i, j) 위치에서 (N-1, N-1)까지 가는 경로의 수
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1  # 시작점에서의 경로 수는 1

    # DP 테이블 채우기
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0 or (i == n - 1 and j == n - 1):
                continue

            jump = arr[i][j]
            if i + jump < n:  # 아래로 이동
                dp[i + jump][j] += dp[i][j]
            if j + jump < n:  # 오른쪽으로 이동
                dp[i][j + jump] += dp[i][j]

    return dp[n - 1][n - 1]  # 도착지에서의 경로 수 반환


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(jump_game(n, arr))