from collections import defaultdict

class Graph:
    def __init__(self, n, inout):
        self.n = n
        self.inout = inout
        self.v_list = defaultdict(list)
        self.visited = [False] * n
        self.cnt = 0


    def get_edges(self, u, v):
        self.v_list[u].append(v)
        self.v_list[v].append(u)


    def find_path(self, i, start, path):

        if i != start and inout[i]:
            #print(path)
            self.cnt += 1
            return

        for v in self.v_list[i]:
            if not self.visited[v]:
                self.visited[v] = True
                self.find_path(v, start, path + [v])
                self.visited[v] = False
    def reset_visited(self):
        self.visited = [False] * self.n

    def count_path(self):
        #print(self.v_list)
        for i in range(self.n):
            #print("i", i)
            if self.inout[i]:
                self.visited[i] = True
                self.find_path(i, i, [i])

            self.reset_visited()

        return self.cnt


if __name__ == "__main__":
    n = int(input())
    inout = list(map(int, input()))
    #print(inout)
    g = Graph(n, inout)
    for _ in range(n-1):
        u, v = map(int, input().split())
        g.get_edges(u-1, v-1)


    print(g.count_path())



