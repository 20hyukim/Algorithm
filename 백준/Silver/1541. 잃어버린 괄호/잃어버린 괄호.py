import sys
from collections import deque


def add_all(nums, ops):
    plus_n = ops.count('+')

    for _ in range(plus_n):
        i = ops.index('+')
        if ops[i] == '+':
            comb = nums[i] + nums[i+1]
            nums = nums[:i] + [comb] + nums[i+2:]
            ops = ops[:i] + ops[i+1:]

    return nums, ops


def sub_all(nums, ops):
    total = nums[0]
    for i in range(1, len(nums)):
        total -= nums[i]
    return total


if __name__ == "__main__":
    exp = input()
    nums = []
    ops = []

    num = ''
    for e in exp:
        if e == '-' or e == '+':
            nums.append(int(num))
            ops.append(e)
            num = ''
            continue
        num += e
    nums.append(int(num))

    nums, ops = add_all(nums, ops)

    print(sub_all(nums, ops))