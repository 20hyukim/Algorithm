from collections import defaultdict


class Pearl:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.heavier = defaultdict(set)
        self.lighter = defaultdict(set)
        self.visited = [False] * (n + 1)

    def weight_pearl(self):
        for _ in range(self.m):
            h, l = map(int, input().split())
            self.heavier[l].add(h)
            self.lighter[h].add(l)

        #print(self.heavier)
        #print(self.lighter)

    def dfs(self, i, compare):
        stack = [i]
        visited = set()

        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            for neighbor in compare[n]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    compare[i].add(neighbor)

    def compress(self):
        keys = list(self.heavier.keys())
        for k in keys:
            self.dfs(k, self.heavier)

        self.visited = [False] * (n+1)

        keys = list(self.lighter.keys())
        for k in keys:
            self.dfs(k, self.lighter)

        #print(self.heavier)
        #print(self.lighter)

    def not_in_middle(self):
        exceed = self.n // 2
        cnt = 0
        for h in self.heavier:
            if len(self.heavier[h]) > exceed:
                cnt += 1

        for h in self.lighter:
            if len(self.lighter[h]) > exceed:
                cnt += 1

        return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    pearl = Pearl(n, m)
    pearl.weight_pearl()
    pearl.compress()
    print(pearl.not_in_middle())
