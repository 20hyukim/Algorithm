from collections import deque


def bfs():
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and tomato[nx][ny] == 0:
                    tomato[nx][ny] = 1
                    queue.append((nx, ny))
    return days


def check_zero():
    for x in range(m):
        for y in range(n):
            if tomato[x][y] == 0:
                return True

    return False


n, m = map(int, input().split())

tomato = []
for _ in range(m):
    line = list(map(int, input().split()))
    tomato.append(line)

queue = deque()
for x in range(m):
    for y in range(n):
        if tomato[x][y] == 1:
            queue.append((x, y))

answer = bfs()

if check_zero():
    print(-1)
else:
    print(answer)
