import heapq
import sys

min_heap = []
for i in range(int(input())):
    n = int(sys.stdin.readline()) * -1
    if n == 0 and not min_heap:
        print(0)
    elif n == 0 and min_heap:
        print(-1 * heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, n)
