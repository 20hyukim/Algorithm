from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, vertex, location):
        self.vertex = vertex
        self.location = [-1] + location
        self.v_list = defaultdict(list)
        self.v_list_location = defaultdict(list)
        self.paths = 0
        self.black_cnt = 0
        self.visited = [False] * (self.vertex + 1)

    def add_edges(self):
        u, v = map(int, input().split())
        self.v_list[u].append(v)
        self.v_list[v].append(u)
        self.v_list_location[u].append(self.location[v])
        self.v_list_location[v].append(self.location[u])


    def dfs(self, i):
        self.visited[i] = True
        for near_v in self.v_list[i]:
            if self.location[near_v]:
                self.black_cnt += 1
            elif not self.visited[near_v]:
                self.dfs(near_v)
    def get_path(self):
        #print(self.v_list)
        #print(self.location)

        for i in range(1, self.vertex+1, 1):
            #print(self.paths)
            if self.location[i]:
                self.paths += sum(self.v_list_location[i])
            elif not self.visited[i]:
                self.black_cnt = 0
                self.dfs(i)
                self.paths += math.comb(self.black_cnt, 2) * 2

        return self.paths



if __name__ == "__main__":
    vertex = int(input())
    location = list(map(int, input()))
    g = Graph(vertex, location)
    for i in range( vertex - 1 ):
        g.add_edges()
    print(g.get_path())