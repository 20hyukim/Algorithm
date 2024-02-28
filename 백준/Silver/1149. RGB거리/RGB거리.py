def find_min_cost(N, costs):
    # DP 테이블 초기화
    dp = [[0 for _ in range(3)] for _ in range(N)]

    # 첫 번째 집을 칠하는 비용 초기화
    for i in range(3):
        dp[0][i] = costs[0][i]

    # 두 번째 집부터 N번째 집까지 최소 비용 계산
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

    # 마지막 집을 칠하는 최소 비용 중 최솟값 반환
    return min(dp[N - 1])


costs = []
# 입력 예시
n = int(input())
for _ in range(n):
    line = list(map(int, input().split()))
    costs.append(line)

# 함수 실행
min_cost = find_min_cost(n, costs)
print(min_cost)
