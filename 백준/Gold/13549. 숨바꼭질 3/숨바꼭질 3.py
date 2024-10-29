import sys
from collections import deque


def bfs(x, y):
    visited = [sys.maxsize] * 100001
    dq = deque()

    dq.append((x, 0))
    while dq:
        length = len(dq)

        for _ in range(length):
            x, cnt = dq.popleft()
            if visited[x] <= cnt:
                continue

            visited[x] = cnt

            if x == y:
                return cnt

            if 0 <= x*2 <= 100000 and visited[x*2] == sys.maxsize:
                dq.append((x*2, cnt))

            if 0 <= x-1 <= 100000 and visited[x-1] == sys.maxsize:
                dq.append((x-1, cnt+1))

            if 0 <= x+1 <= 100000 and visited[x+1] == sys.maxsize:
                dq.append((x+1, cnt+1))


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(bfs(x, y))