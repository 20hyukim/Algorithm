
class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []

    def add_edges(self, u, v):
        self.graph.append([u, v])

    def get_parent(self, n, parent):
        if parent[n] != n:
            return self.get_parent(parent[n], parent)
        return parent[n]

    def union(self, x, y, rank, parent):
        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            rank[x] += 1

    def count_virus(self):
        parent = []
        rank = []
        for i in range(vertex):
            parent.append(i)
            rank.append(0)

        for i in range(edges):
            u, v = self.graph[i]

            x = self.get_parent(u, parent)
            y = self.get_parent(v, parent)

            if x != y:
                self.union(x, y, rank, parent)

        for i in range(self.vertex):
            parent[i] = self.get_parent(i, parent)

        virus_computer = parent[0]
        cnt = 0
        for p in parent[1:]:
            if p == virus_computer:
                cnt += 1
        #print(parent)

        return cnt


if __name__ == "__main__":
    vertex = int(input())
    edges = int(input())
    g = Graph(vertex)
    for _ in range(edges):
        u, v = map(int, input().split())
        g.add_edges(u-1, v-1)
    print(g.count_virus())