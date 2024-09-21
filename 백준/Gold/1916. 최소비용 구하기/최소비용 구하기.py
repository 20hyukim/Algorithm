import heapq
import sys


class Dij:
    def __init__(self, n, m):
        self.vertex = n
        self.graph = [[] for i in range(n+1)]
        for i in range(m):
            u, v, w = map(int, input().split())
            self.graph[u].append([v, w])


    def min_cost(self, start, end):
        cost = [sys.maxsize] * (self.vertex + 1)
        pq = []
        cost[start] = 0
        heapq.heappush(pq, (0, start))

        while pq:
            c_weight, u = heapq.heappop(pq)
            
            if c_weight > cost[u]:
                continue

            for near_node in self.graph[u]:
                v, w = near_node
                c = cost[u] + w
                if cost[v] > c:
                    cost[v] = c
                    heapq.heappush(pq, (c, v))

        return cost[end]


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    dij = Dij(n, m)
    start, end = map(int, input().split())
    print(dij.min_cost(start, end))