from collections import deque


def dfs(node):
    visited_dfs.add(node)
    result_dfs.append(node)

    for i in sorted(edges[node]):
        if i not in visited_dfs:
            dfs(i)


def bfs(node):
    q = deque([node])
    visited_bfs.add(node)
    result_bfs.append(node)

    while q:
        node = q.popleft()
        for i in sorted(edges[node]):
            if i not in visited_bfs:
                visited_bfs.add(i)
                result_bfs.append(i)
                q.append(i)


if __name__ == "__main__":
    n, m, start = map(int, input().split())
    edges = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    # DFS
    visited_dfs = set()
    result_dfs = []
    dfs(start)
    print(" ".join(map(str, result_dfs)))

    # BFS
    visited_bfs = set()
    result_bfs = []
    bfs(start)
    print(" ".join(map(str, result_bfs)))