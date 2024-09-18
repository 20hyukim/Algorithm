class Graph():
    def __init__(self, vertex):
        self.vertex = vertex
        self.g = []

    def add_edges(self, u, v):
        self.g.append([u, v])

    def get_parent(self, n, parent):
        if parent[n] != n:
            return self.get_parent(parent[n], parent)
        return parent[n]

    def get_union(self, x, y, parent, rank):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    def get_connected_edges(self):
        parent = []
        rank = []
        for i in range(self.vertex):
            parent.append(i)
            rank.append(0)

        for i in range(m):
            u, v = self.g[i]

            x = self.get_parent(u, parent)
            y = self.get_parent(v, parent)

            if x != y:
                self.get_union(x, y, parent, rank)

        #print(parent)
        #print(rank)

        for p in range(len(parent)):
            parent[p] = self.get_parent(p, parent)
        parent = set(parent)
        #print(parent)
        return len(parent)

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)
    for i in range(m):
        u, v = map(int, input().split())
        g.add_edges(u-1, v-1)
    print(g.get_connected_edges())