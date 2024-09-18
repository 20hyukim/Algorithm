from collections import defaultdict
import math


class Graph:
    def __init__(self, n, inout):
        self.n = n
        self.inout = inout
        self.v_list = defaultdict(list)
        self.cnt = 0
        self.bb = 0

    def get_edges(self, u, v):
        self.v_list[u].append(v)
        self.v_list[v].append(u)
        if self.inout[u] and self.inout[v]:
            self.bb += 1


    def in_line(self):
        for i in range(1, self.n - 1, 1):
            if self.v_list[i] != [i - 1, i + 1]:
                return False

        if self.v_list[0] != [1]:
            return False

        if self.v_list[self.n - 1] != [self.n - 2]:
            return False

        return True

    def count_path(self):
        if sum(self.inout) == 0 or sum(self.inout) == 1:
            return 0

        if sum(self.inout) == 2:
            return 2

        if self.in_line():
            return (sum(self.inout) - 1) * 2

        return self.bb * 2 + math.comb((sum(self.inout) - self.bb), 2) * 2


if __name__ == "__main__":
    n = int(input())
    inout = list(map(int, input()))
    #print(inout)
    g = Graph(n, inout)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g.get_edges(u - 1, v - 1)

    print(g.count_path())
