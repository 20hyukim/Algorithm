from collections import deque
def longest(start, end):
    cost = [0] * (n+1)
    reverse_edges = [[] for i in range(n+1)]

    dq = deque()
    dq.append(start)

    while dq:
        u = dq.popleft()

        for v, w in edges[u]:
            if cost[v] < cost[u] + w:
                cost[v] = cost[u] + w
            ind[v] -= 1
            reverse_edges[v].append([u, w])
            if ind[v] == 0:
                dq.append(v)

    stack = []
    visited = [False] * (n+1)
    stack.append(end)
    critical_cnt = 0
    while stack:
        u = stack.pop()

        for v, w in reverse_edges[u]:
            if cost[u] == cost[v] + w:
                critical_cnt += 1
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

    print(cost[end])
    print(critical_cnt)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    edges = [[] for i in range(n+1)]
    ind = [0] * (n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        edges[u].append([v, w])
        ind[v] += 1

    start, end = map(int, input().split())
    longest(start, end)
