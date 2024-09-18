from collections import defaultdict, deque
class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = defaultdict(list)
        self.color = [-1] * vertex
        self.visited = [False] * vertex

    def add_edges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, i, color_num):
        queue = deque([i])
        self.color[i] = color_num

        while queue:
            cur_v = queue.popleft()
            color_num = self.color[cur_v] + 1
            self.visited[cur_v] = True
            for v in self.graph[cur_v]:
                if self.color[v] != -1 and self.color[v] % 2 != color_num % 2:
                    return False

                if self.color[v] == -1:
                    self.color[v] = color_num
                    queue.append(v)

        return True

    def is_bipartite(self):
        for i in range(vertex):
            if not self.visited[i]:
                is_bip = self.bfs(i, 0)
                if not is_bip:
                    return 'NO'

        return 'YES'


if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        vertex, edge = map(int, input().split())
        g = Graph(vertex)
        for i in range(edge):
            u, v = map(int, input().split())
            g.add_edges(u-1, v-1)
        print(g.is_bipartite())