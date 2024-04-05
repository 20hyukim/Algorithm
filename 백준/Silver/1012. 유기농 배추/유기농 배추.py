def setting():
    m, n, k = map(int, input().split())
    list_r = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        list_r[y][x] = 1
    return list_r, m, n

def white(x, y, list_r, m, n):
    if list_r[x][y] == 0:
        return 0
    
    # 초기 위치를 스택에 추가
    stack = [(x, y)]
    list_r[x][y] = 0  # 방문 처리
    
    while stack:
        cx, cy = stack.pop()
        # 상, 하, 좌, 우 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and list_r[nx][ny] == 1:
                list_r[nx][ny] = 0  # 방문 처리
                stack.append((nx, ny))

    return 1

def main():
    num = int(input())
    for _ in range(num):
        list_r, m, n = setting()
        total = 0
        for i in range(n):
            for j in range(m):
                if list_r[i][j] == 1:
                    total += white(i, j, list_r, m, n)
        print(total)

main()