def lis_length(nums):
    if not nums:
        return 0

    # DP 테이블 초기화
    dp = [1] * len(nums)  # 각 위치를 끝으로 하는 LIS의 길이를 저장. 최소 길이는 1이므로 1로 초기화.

    # 모든 위치에 대해 LIS 계산
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # DP 테이블에서 최대 값을 찾음
    return max(dp)


height = int(input())
# 입력 예시
nums = list(map(int, input().split()))
print(lis_length(nums))
