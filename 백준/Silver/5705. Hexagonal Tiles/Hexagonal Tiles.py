import sys


def create_grid(n):
    grid = [[0 for _ in range(n // 2 + 1)] for _ in range(2)]

    for i in range(0, n + 1, 1):
        if i % 2 == 0:
            even_y = int(i / 2)
            grid[1][even_y] = i
        else:
            odd_y = int((i - 1) / 2)
            grid[0][odd_y] = i

    if n % 2 == 0:
        grid[0][int(n // 2)] = -1

    return grid


def find_cases(n, x, y, num):
    key = (n, x, y)
    if key in memo:
        return memo[key]

    if n == -1 or y > (num // 2):
        memo[key] = 0
        return 0

    if n == num:
        memo[key] = 1
        return 1

    if n % 2 == 0:
        result = find_cases(n + 1, x - 1, y, num) + find_cases(n + 2, x, y + 1, num)
    if n % 2 == 1:
        result = find_cases(n + 1, x + 1, y + 1, num) + find_cases(n + 2, x, y + 1, num)

    memo[key] = result
    return result


memo = {}
nums = []
total = 0
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    num = int(line)
    if num == 0:
        break
    nums.append(num)

for num in nums:
    grid = create_grid(num)
    memo.clear()
    total = find_cases(0, 1, 0, num)
    print(total)
