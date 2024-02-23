import heapq

rooms = 0

end_times = []
total = []
n = int(input())
for i in range(n):
    total.append(list(map(int, input().split())))


total.sort()
loop = 0
for start, end in total:
    if end_times and end_times[0] <= start:
        heapq.heappop(end_times)
        heapq.heappush(end_times, end)
    else:
        heapq.heappush(end_times, end)
        rooms += 1

print(rooms)