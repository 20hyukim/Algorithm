import itertools

def count_sum(n, sum_up):
    nums = list(map(int, input().split()))
    count = 0
    for c in range(1, n+1, 1):
        combinations = itertools.combinations(nums, c)

        for comb in combinations:
            if sum(comb) == sum_up:
                count += 1

    return count


if __name__ == "__main__":
    n, sum_up = map(int, input().split())
    print(count_sum(n, sum_up))