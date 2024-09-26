from collections import deque


def mark_house(i, j):
    stack = deque()
    stack.append([i, j])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cnt_h = 0
    visited[i][j] = True

    while stack:
        x, y = stack.pop()
        cnt_h += 1

        for dl, dr in directions:
            if 0 <= x+dl < n and 0 <= y+dr < n and not visited[x+dl][y+dr] and houses[x+dl][y+dr] == '1':
                stack.append([x+dl, y+dr])
                visited[x+dl][y+dr] = True

    return cnt_h

def count_house():
    marked_house = []
    for i in range(n):
        for j in range(n):
            if houses[i][j] == '1' and not visited[i][j]:
                marked_house.append(mark_house(i, j))

    print(len(marked_house))
    for m in sorted(marked_house):
        print(m)



if __name__ == "__main__":
    n = int(input())
    houses = []
    visited = [[False]*n for _ in range(n)]

    for _ in range(n):
        h = list(input())
        houses.append(h)

    count_house()