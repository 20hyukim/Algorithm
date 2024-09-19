def dfs(cur, left):
    if len(cur) == num_cnt - 1:
        total.append(cur)
        return

    for i in range(4):
        if left[i] > 0:
            left[i] -= 1
            dfs(cur+[i], left)
            left[i] += 1


def op_calculate(nums, total):
    values = []
    base_num = nums.pop(0)
    for t in total:
        value = base_num

        for i in range(num_cnt - 1):
            if t[i] == 0:
                value += nums[i]
                continue
            elif t[i] == 1:
                value -= nums[i]
                continue
            elif t[i] == 2:
                value *= nums[i]
                continue
            else:
                if value < 0:
                    value *= -1
                    value = value // nums[i]
                    value *= -1
                    continue
                value = value // nums[i]
        values.append(value)

    return min(values), max(values)


if __name__ == "__main__":
    num_cnt = int(input())
    nums = list(map(int, input().split()))
    op = list(map(int, input().split()))
    total = []
    dfs([], op)
    min_v, max_v = op_calculate(nums, total)
    print(max_v)
    print(min_v)