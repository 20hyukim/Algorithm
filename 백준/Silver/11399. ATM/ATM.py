def sort_wait_time():
    n = int(input())
    withdrawal = list(map(int, input().split()))
    withdrawal.sort()
    return withdrawal


def total_wait_time(withdrawal):
    wait_time = 0
    sum_time = 0
    for i in range(len(withdrawal)):
        wait_time = wait_time + withdrawal[i]
        sum_time += wait_time

    return sum_time


def main():
    withdrawal = sort_wait_time()
    print(total_wait_time(withdrawal))


if __name__ == "__main__":
    main()