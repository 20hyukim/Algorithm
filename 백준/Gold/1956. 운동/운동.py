INF = int(1e9)


def floyd_warshall(n, e):
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for idx in range(1, n + 1):
        dist[idx][idx] = 0

    for i in range(e):
        a, b, c = map(int, input().split())
        dist[a][b] = c

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    total = []
    for a in range(1, n + 1, 1):
        for b in range(1, n + 1, 1):
            if dist[a][b] != 0 and dist[a][b] != INF and dist[b][a] != INF:
                total.append(dist[a][b] + dist[b][a])
    return total


n, e = map(int, input().split())

total = floyd_warshall(n, e)

if total != []:
    print(min(total))
else:
    print(-1)
