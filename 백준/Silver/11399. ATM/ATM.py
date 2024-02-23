
n = int(input())
withdrawal = list(map(int, input().split()))
withdrawal.sort()

wait_time = 0
sum_time = 0
for i in range(n):
    wait_time = wait_time + withdrawal[i]
    sum_time += wait_time


print(sum_time)