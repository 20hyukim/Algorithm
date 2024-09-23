from collections import deque


def print_c_map(c_map, year):
    print("year: ", year)
    for i in range(r):
        print(c_map[i])
    print("hedge :", hedge)
    print()
    print()
def get_hour():
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    year = 0
    visited = []
    while True:
        #print_c_map(c_map, year)
        year += 1
        w_length = len(water)

        for w in range(w_length):
            i, j = water.popleft()
            for l, d in directions:
                if 0 <= i+l < r and 0 <= j+d < c and c_map[i+l][j+d] == '.':
                    c_map[i+l][j+d] = '*'
                    water.append((i+l, j+d))

        b_length = len(hedge)
        if b_length == 0:
            return "KAKTUS"

        for b in range(b_length):
            bi, bj = hedge.popleft()
            if (bi, bj) in visited:
                continue
            visited.append((bi, bj))
            for l, d in directions:
                if 0 <= bi + l < r and 0 <= bj + d < c:
                    if (bi + l, bj + d) == beaver:
                        return year
                    if c_map[bi+l][bj+d] == '.':
                        hedge.append((bi+l, bj+d))


if __name__ == "__main__":
    r, c = map(int, input().split())
    c_map = []
    stone = deque()
    water = deque()
    hedge = deque()
    for i in range(r):
        m = list(input())
        c_map.append(m)
        for j in range(c):
            if m[j] == 'X':
                stone.append((i, j))

            elif m[j] == 'S':
                m[j] = '.'
                hedge.append((i, j))

            elif m[j] == 'D':
                beaver = (i, j)

            elif m[j] == '*':
                water.append((i, j))

    print(get_hour())