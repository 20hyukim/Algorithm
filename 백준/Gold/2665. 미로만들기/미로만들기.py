import sys
from collections import deque

class Maze:
    def __init__(self, n):
        self.n = n
        self.cost = [[sys.maxsize] * n for i in range(n)]
        self.cost[0][0] = 0
        self.g = []

        for i in range(n):
            c = list(map(int, input()))
            self.g.append(c)

    def dij(self):
        dq = deque([(0, 0, 0)])
        udlr = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while dq:
            w, i, j = dq.popleft()

            if self.cost[i][j] < w:
                continue

            for l, r in udlr:
                if 0 <= i+l < n and 0 <= j+r < n:
                    if self.g[i+l][j+r] == 0:
                        renew_cost = self.cost[i][j] + 1
                        if self.cost[i+l][j+r] > renew_cost:
                            self.cost[i+l][j+r] = renew_cost
                            dq.append((renew_cost, i+l, j+r))

                    else:
                        if self.cost[i+l][j+r] > self.cost[i][j]:
                            self.cost[i+l][j+r] = self.cost[i][j]
                            dq.appendleft((self.cost[i+l][j+r], i+l, j+r))

        return self.cost[-1][-1]


if __name__ == "__main__":
    n = int(input())
    maze = Maze(n)
    print(maze.dij())