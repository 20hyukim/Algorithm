
class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.edges = []

    def add_edges(self, u, v, w):
        self.edges.append([u, v, w])
        #print(u, v, w)

    def get_parent(self, n, parent):
        if parent[n] != n:
            return self.get_parent(parent[n], parent)
        return parent[n]

    def union(self, x, y, parent, rank):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal(self):
        self.edges = sorted(self.edges, key=lambda item: item[2])
        result = []
        parent = []
        rank = []
        for i in range(self.vertex):
            parent.append(i)
            rank.append(0)
        i = 0
        e = 0

        while e < self.vertex - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.get_parent(u, parent)
            y = self.get_parent(v, parent)

            if x != y:
                e += 1
                self.union(x, y, parent, rank)
                result.append(w)

        return sum(result)


if __name__ == "__main__":
    vertex, e = map(int, input().split())
    g = Graph(vertex)
    for i in range(e):
        u, v, w = map(int, input().split())
        g.add_edges(u-1, v-1, w)

    print(g.kruskal())