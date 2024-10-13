
def get_max_count(nums, n):
    dp = [0] * (n+1)

    for i in range(1, n+1, 1):
        if nums[i] >= 0:
            if dp[i-1] < 0:
                dp[i] = 0 + nums[i]
                continue
            dp[i] = dp[i-1] + nums[i]
            continue
        if dp[i-1] + nums[i] < 0:
            dp[i] = nums[i]
            continue
        dp[i] = dp[i-1] + nums[i]

    #print(dp)
    return max(dp[1:])


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    nums.insert(0, 0)
    print(get_max_count(nums, n))