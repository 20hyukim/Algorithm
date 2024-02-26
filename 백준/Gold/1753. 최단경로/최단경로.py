import heapq

INF = int(1e9)


def findCheapestPrice(n, src, nodes):
    dist = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    q = []
    # print(nodes)

    for a, b, c in nodes:
        graph[a].append((b, c))

    heapq.heappush(q, (0, src))

    dist[src] = 0

    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist


n, e = map(int, input().split())
start = int(input())
nodes = []
for _ in range(e):
    nodes.append(list(map(int, input().split())))

dist = findCheapestPrice(n, start, nodes)

for i in range(1, n + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
