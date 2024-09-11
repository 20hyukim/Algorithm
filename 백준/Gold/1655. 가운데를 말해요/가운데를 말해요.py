import sys
import heapq
min_heap = []
max_heap = []
def find_median(i, n):
    global min_heap
    global max_heap

    if i % 2 == 1:
        heapq.heappush(min_heap, n)
        heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))
        return max_heap[0] * -1

    else:
        heapq.heappush(min_heap, n)
        heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))
        heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
        return max_heap[0]* -1


if __name__ == "__main__":
    for i in range(1, int(sys.stdin.readline())+1, 1):
        print(find_median(i, int(sys.stdin.readline())))