def longest_length(nums, n):
    tails = [0] * n
    size = 0
    for i in nums:
        start = 0
        end = size

        while start != end:
            m = (start + end) // 2

            if tails[m] < i:
                start = m + 1
            else:
                end = m

        tails[start] = i
        size = max(start + 1, size)

    return size


n = int(input())
nums = list(map(int, input().split()))
print(longest_length(nums, n))
