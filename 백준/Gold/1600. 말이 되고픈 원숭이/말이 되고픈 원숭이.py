from collections import deque

q = deque()


def bfs(k):
    monkey = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    horse = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
    visited = [[[0 for col in range(w)] for row in range(h)] for depth in range(k+1)]

    q.append((0, 0, k, 0))

    while q:
        i, j, k, cnt = q.popleft()
        if visited[k][i][j] == 1:
            continue

        visited[k][i][j] = 1

        if i == h - 1 and j == w - 1:
            return cnt

        for l, r in monkey:
            if 0 <= i + l < h and 0 <= j + r < w and plain[i + l][j + r] == 0 and visited[k][i+l][j+r] == 0:
                q.append((i+l, j+r, k, cnt+1))

        if k > 0:
            for l, r in horse:
                if 0 <= i + l < h and 0 <= j + r < w and plain[i + l][j + r] == 0 and visited[k-1][i+l][j+r] == 0:
                    q.append((i+l, j+r, k-1, cnt+1))

    return -1


if __name__ == "__main__":
    k = int(input())
    w, h = map(int, input().split())
    plain = []

    for _ in range(h):
        plain.append(list(map(int, input().split())))

    print(bfs(k))