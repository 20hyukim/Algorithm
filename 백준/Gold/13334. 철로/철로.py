import heapq

max_count = 0
min_heap = []
save_heap = []
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    heapq.heappush(min_heap, (y, x))

l = int(input())
while min_heap:
    y, x = heapq.heappop(min_heap)
    l_s = y - l

    while save_heap and save_heap[0] < l_s:
        heapq.heappop(save_heap)

    if l_s <= x:
        heapq.heappush(save_heap, x)

    if max_count < len(save_heap):
        max_count = len(save_heap)

print(max_count)