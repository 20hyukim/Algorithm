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


def input_nodes(n, e):
    nodes = []
    for _ in range(e):
        nodes.append(list(map(int, input().split())))
    return nodes


def print_nodes(dist, n):
    for i in range(1, n + 1):
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])


def main():
    n, e = map(int, input().split())
    start = int(input())
    dist = findCheapestPrice(n, start, input_nodes(n, e))
    print_nodes(dist, n)


if __name__ == "__main__":
    main()
